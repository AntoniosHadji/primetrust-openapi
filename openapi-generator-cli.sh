#!/usr/bin/env bash
# openapi-generator-cli generate -i ./openapi.json -g "${1}" -o "${1}"
npx @openapitools/openapi-generator-cli generate -i openapi.json -g "${1}" -o "./generated/${1}"
