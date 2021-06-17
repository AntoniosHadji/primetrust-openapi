#!/usr/bin/env bash
# -*- coding: utf-8 -*-
curl -X POST --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  -d '{"openAPIUrl": "https://leros-public.s3.amazonaws.com/openapi.json"}' \
  'http://api.openapi-generator.tech/api/gen/clients/java'
