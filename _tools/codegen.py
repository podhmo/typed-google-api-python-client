import itertools
from prestring.python import Module
from prestring.utils import LParams, reify
from prestring.naming import titleize
from dictknife import loading


class Accessor:
    def __init__(self, d, m, *, disable_docstring=False):
        self.d = d
        self.m = m
        self.disable_docstring = disable_docstring

    @reify
    def version(self):
        return self.d["id"].split(":")[1]

    @reify
    def name(self):
        return self.d["id"].split(":")[0]

    @reify
    def resources(self):
        return self.d.get("resources") or {}

    def iterate_methods(self, resource):
        for mname, method in resource.get("methods", {}).items():
            params = LParams()
            for is_positional, (pname, parameter) in itertools.zip_longest(method.get("parameterOrder", []), method.get("parameters", {}).items()):
                if is_positional:
                    params.append(pname)  # TODO type:
                else:
                    params[pname] = None  # TODO type:
            yield mname, method, params

    def iterate_nested_resources(self, resource):
        for mname, subresource in resource.get("resources", {}).items():
            yield mname, subresource

    def emit_docstring(self, doc):
        if not self.disable_docstring:
            self.m.docstring(doc)


def run(*, path: str, disable_docstring) -> None:
    d = loading.loadfile(path)
    m = Module()
    a = Accessor(d, m, disable_docstring=disable_docstring)

    m.import_("typing", as_="t")
    m.sep()
    m.stmt("AnyService = t.Any  # TODO")
    m.stmt("AnyResource = t.Any  # TODO")
    m.sep()
    for rname, resource in a.resources.items():
        with m.class_(titleize(rname), ""):

            with m.method("__init__", "resource: AnyResource"):
                m.stmt("self.internal = resource")

            m.stmt("# methods")
            for mname, method, params in a.iterate_methods(resource):
                with m.method(mname, params):
                    a.emit_docstring(method["description"])
                    m.stmt(f"""# {method["httpMethod"]}: {method["flatPath"]}""")
                    m.stmt(f"""# id: {method["id"]}""")
                    m.stmt(f"return self.internal.{mname}({params})")

            m.stmt("# nested resources")
            for srname, subresource in a.iterate_nested_resources(resource):
                with m.method(srname):
                    m.stmt(f"return self.internal.{srname}({params})")

            # m.stmt("# nested resources")
            # for mname, subresource in resource.get("resources", {}).items():
            #     params = LParams()
            #     for is_positional, (pname, parameter) in itertools.zip_longest(subresource.get("parameterOrder", []), subresource.get("parameters", {}).items()):
            #         if is_positional:
            #             params.append(pname)  # TODO type:
            #         else:
            #             params[pname] = None  # TODO type:
            #     with m.method(mname, params):
            #         docstring(subresource["description"])
            #         m.stmt(f"""# id: {subresource["id"]}""")
            #         m.stmt(f"return self.{mname}({params})")

    with m.class_("Service"):
        with m.method("__init__", "service: AnyService"):
            m.stmt("self.internal = service")

        for rname in a.resources.keys():
            with m.method(rname, return_type=titleize(rname)):
                m.stmt(f"return {titleize(rname)}(self.internal.{rname}())")

    with m.def_("build", "*args", "**kwargs", return_type="Service"):
        m.stmt("# TODO: use the signature of googleapiclient.discovery.build")
        m.submodule().from_("googleapiclient.discovery", "build")
        m.stmt(f"return Service(build({a.name!r}, {a.version!r}, *args, **kwargs))")

    print(m)


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("path", default=None, nargs="?")
    parser.add_argument("--disable-docstring", action="store_true")
    args = parser.parse_args()
    run(**vars(args))


if __name__ == "__main__":
    main()
