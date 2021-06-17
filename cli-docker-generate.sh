#!/usr/bin/env bash
# -*- coding: utf-8 -*-
docker run --rm \
    -v "$PWD:/local" \
    openapitools/openapi-generator-cli generate -i "/local/${1:-openapi.json}" -g java -o /local/out/java
