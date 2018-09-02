from: [../jsonfiles/sheets/v4/sheets-api.json](../jsonfiles/sheets/v4/sheets-api.json)

## service

```
>>> pp set(dir(service)).difference(dir(object))
{'__dict__',
 '__getstate__',
 '__module__',
 '__setstate__',
 '__weakref__',
 '_add_basic_methods',
 '_add_nested_resources',
 '_add_next_methods',
 '_baseUrl',
 '_developerKey',
 '_dynamic_attrs',
 '_http',
 '_model',
 '_requestBuilder',
 '_resourceDesc',
 '_rootDesc',
 '_schema',
 '_set_dynamic_attr',
 '_set_service_methods',
 'new_batch_http_request',
 'spreadsheets'}
```

## resources

- resources/spreadsheets

```
>>> dir(service.spreadsheets())
 'batchUpdate',
 'create',
 'developerMetadata',
 'get',
 'getByDataFilter',
 'sheets',
 'values
```

the resource have

- nested resources
- methods

sheets.spreadsheets.get

```json
        "get": {
          "description": "Returns the spreadsheet at the given ID.\nThe caller must specify the spreadsheet ID.\n\nBy default, data within grids will not be returned.\nYou can include grid data one of two ways:\n\n* Specify a field mask listing your desired fields using the `fields` URL\nparameter in HTTP\n\n* Set the includeGridData\nURL parameter to true.  If a field mask is set, the `includeGridData`\nparameter is ignored\n\nFor large spreadsheets, it is recommended to retrieve only the specific\nfields of the spreadsheet that you want.\n\nTo retrieve only subsets of the spreadsheet, use the\nranges URL parameter.\nMultiple ranges can be specified.  Limiting the range will\nreturn only the portions of the spreadsheet that intersect the requested\nranges. Ranges are specified using A1 notation.",
          "flatPath": "v4/spreadsheets/{spreadsheetId}",
          "httpMethod": "GET",
          "id": "sheets.spreadsheets.get",
          "parameterOrder": [
            "spreadsheetId"
          ],
          "parameters": {
            "includeGridData": {
              "description": "True if grid data should be returned.\nThis parameter is ignored if a field mask was set in the request.",
              "location": "query",
              "type": "boolean"
            },
            "ranges": {
              "description": "The ranges to retrieve from the spreadsheet.",
              "location": "query",
              "repeated": true,
              "type": "string"
            },
            "spreadsheetId": {
              "description": "The spreadsheet to request.",
              "location": "path",
              "required": true,
              "type": "string"
            }
          },
          "path": "v4/spreadsheets/{spreadsheetId}",
          "response": {
            "$ref": "Spreadsheet"
          },
          "scopes": [
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive.readonly",
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/spreadsheets.readonly"
          ]
        },
```

https://github.com/google/google-api-python-client/blob/781de4c8dd700a4a2cc820b2cdbf5ba31241bd6b/googleapiclient/discovery.py#L988

- required_params
- pattern_params
- enum_params

- method
- nested resource
