#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# java -jar modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate \
#   -i https://petstore.swagger.io/v2/swagger.json \
#   -l java \
#   -o samples/client/petstore/java

docker run -it --rm -v "${PWD}:/local" \
  swaggerapi/swagger-codegen-cli validate\
   -i /local/openapi.json
   # -i /local/primetrust-public-resolved.json

#     -l java \
#     -o /local/client/java


# docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli generate \
#     -i https://petstore.swagger.io/v2/swagger.json \
#     -l go \
#     -o /local/out/go


#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# docker run --rm \
#     -v "$PWD:/local" \
#     openapitools/openapi-generator-cli validate -i "/local/${1:-openapi.json}"
