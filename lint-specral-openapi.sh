#!/usr/bin/env bash
rm -f ./*.log
spectral lint openapi.json &> "openapi.$(date +%FT%H%M).log"
