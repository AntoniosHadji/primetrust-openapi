Working OPENAPI json file for generating SDK.
============================================

As of 2023-02-10 12:28:36 the openapi json that is automatically built contains several errors.
`clean_openapi.py` retrieves the user facing document and corrects all errors so that code
generation works.



Install:

https://openapi-generator.tech/docs/installation

`npm install @openapitools/openapi-generator-cli -g`


https://github.com/stoplightio/spectral

`npm install -g @stoplight/spectral-cli`


Notes:
------

Frequency Rule: These tokens are ruby specific
pattern: \\A \\Z ? 
