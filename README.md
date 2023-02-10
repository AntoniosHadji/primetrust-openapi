Working OPENAPI json file for generating SDK.
============================================

As of 2023-02-10 12:28:36 the openapi json that is automatically built contains several errors.
`fix.py` retrieves the user facing document and corrects all errors so that code
generation works.


Install:

https://openapi-generator.tech/docs/installation

Example Use:

`npx @openapitools/openapi-generator-cli generate -i openapi.json -g typescript-node -o /generated/ts-node-client/`



