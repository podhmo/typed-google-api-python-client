download:
	git clone --depth 1 git@github.com:google/google-api-go-client

print-collect-json:
	python _tools/print_json_path.py google-api-go-client/ --outdir jsonfiles
collect-json:
	rm -rf jsonfiles
	$(MAKE) print-collect-json | grep -v '^make' | bash -x

codegen:
	python _tools/codegen.py --disable-docstring jsonfiles/sheets/v4/sheets-api.json
shape:
	dictknife shape --with-type --with-example jsonfiles/sheets/v4/sheets-api.json| tee docs/sheets.shape
