#!/usr/bin/env bash
spectral lint openapi.json &> "openapi.$(date +%FT%H%M).log"
