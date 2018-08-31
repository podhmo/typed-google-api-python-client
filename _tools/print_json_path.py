import os


def run(path, outdir):
    for root, ds, fs in os.walk(path):
        for f in fs:
            if f.endswith(".json"):
                jsonpath = os.path.join(root, f)
                print(
                    f"mkdir -p {outdir}/{os.path.dirname(jsonpath.split('/', 1)[1])} && cp {jsonpath} {outdir}/{jsonpath.split('/', 1)[1]}"
                )


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--outdir")
    args = parser.parse_args()
    run(args.path, args.outdir)


if __name__ == "__main__":
    main()
