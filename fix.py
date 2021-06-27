import copy
import json


def uuid(name):
    return {
        "name": name,
        "in": "path",
        "required": True,
        "style": "simple",
        "schema": {"$ref": "#/components/schemas/types__uuid_v4"},
    }


with open("./primetrust-public-resolved.json", "r") as f:
    data = json.load(f)

print(data.keys())
final = copy.deepcopy(data)
# duplicate path with "/v2/resource-tokens/{resource-token-id}"
del final["paths"]["/v2/resource-tokens/{hash}"]
del data["paths"]["/v2/resource-tokens/{hash}"]

# missing parameter
for p in [
    "/v2/account-cash-transfer-reviews/{account-cash-transfer-review-id}/from-account",
    "/v2/account-cash-transfer-reviews/{account-cash-transfer-review-id}/to-account",
]:
    for method in final["paths"][p]:
        final["paths"][p][method]["parameters"].append(
            uuid("account-cash-transfer-review-id")
        )

for p in [
    "/v2/accounts/{account-id}/account-cash-transfers",
    "/v2/accounts/{account-id}/account-histories",
    "/v2/accounts/{account-id}/authorized-transfer-accounts",
    "/v2/accounts/{account-id}/internal-asset-transfers",
    "/v2/accounts/{account-id}/policy",
    "/v2/accounts/{account-id}/sandbox/fund",
]:
    for method in final["paths"][p]:
        final["paths"][p][method]["parameters"].append(uuid("account-id"))

p = "/v2/account-types/{account-type-id}/policy"
for method in final["paths"][p]:
    final["paths"][p][method]["parameters"].append(uuid("account-type-id"))

p = "/v2/card-transactions/{card-transactions-id}/sandbox"
for method in final["paths"][p]:
    final["paths"][p][method]["parameters"].append(uuid("card-transactions-id"))

p = "/v2/contact-funds-transfer-references/{contact-funds-transfer-reference-id}/sandbox/contribution"
for method in final["paths"][p]:
    final["paths"][p][method]["parameters"].append(
        uuid("contact-funds-transfer-reference-id")
    )

p = "/v2/funds-transfer-methods/{funds-transfer-method-id}/bank"
for method in final["paths"][p]:
    final["paths"][p][method]["parameters"].append(uuid("funds-transfer-method-id"))

for p in [
    "/v2/internal-asset-transfer-reviews/{internal-asset-transfer-review-id}/from-account",
    "/v2/internal-asset-transfer-reviews/{internal-asset-transfer-review-id}/to-account",
]:
    for method in final["paths"][p]:
        final["paths"][p][method]["parameters"].append(
            uuid("internal-asset-transfer-review-id")
        )

p = "/v2/disbursement-owner-verifications/{resource-token-hash}"
for method in final["paths"][p]:
    final["paths"][p][method]["parameters"].append(uuid("resource-token-hash"))

for p in [
    "/v2/resource-tokens/{resource-token-id}/accounts",
    "/v2/resource-tokens/{resource-token-id}/contacts",
    "/v2/resource-tokens/{resource-token-id}/ira-rollover-forms",
    "/v2/resource-tokens/{resource-token-id}/uploaded-documents",
]:
    for method in final["paths"][p]:
        final["paths"][p][method]["parameters"].append(uuid("resource-token-id"))

for p in [
    "/v2/user-invitation-reviews/{user-invitation-review-id}/from-account",
    "/v2/user-invitation-reviews/{user-invitation-review-id}/to-account",
]:
    for method in final["paths"][p]:
        final["paths"][p][method]["parameters"].append(
            uuid("user-invitation-review-id")
        )


for p in data["paths"]:
    key = "paths"
    print("path: ", p)
    for method in data[key][p]:
        k2 = data[key][p][method]
        if "responses" in k2:
            for response in k2["responses"]:
                if "description" not in k2["responses"][response]:
                    final[key][p][method]["responses"][response]["description"] = "TODO"
                elif k2["responses"][response]["description"] == "":
                    final[key][p][method]["responses"][response][
                        "description"
                    ] = "TODO-was-empty-string"

                if (
                    "content" in k2["responses"][response]
                    and "application/vnd.api+json"
                    in k2["responses"][response]["content"]
                ):

                    if (
                        "description"
                        in k2["responses"][response]["content"][
                            "application/vnd.api+json"
                        ]
                    ):
                        del final[key][p][method]["responses"][response]["content"][
                            "application/vnd.api+json"
                        ]["description"]

                    if (
                        "schema"
                        in k2["responses"][response]["content"][
                            "application/vnd.api+json"
                        ]
                        and "title"
                        in k2["responses"][response]["content"][
                            "application/vnd.api+json"
                        ]["schema"]
                    ):
                        if (
                            k2["responses"][response]["content"][
                                "application/vnd.api+json"
                            ]["schema"]["title"]
                            is None
                        ):
                            final[key][p][method]["responses"][response]["content"][
                                "application/vnd.api+json"
                            ]["schema"]["title"] = "string"

for tag in final["tags"]:
    if tag["description"] == "":
        tag["description"] = "TODO: Fill description."


fr = final["components"]["schemas"]["Frequency Rule"]
del final["components"]["schemas"]["Frequency Rule"]
final["components"]["schemas"]["Frequency_Rule"] = fr

for o in final["components"]["schemas"]["rules__rule_type_info"]["oneOf"]:
    if "$ref" in o:
        print("found $ref")
        if o["$ref"] == "#/components/schemas/Frequency Rule":
            o["$ref"] = "#/components/schemas/Frequency_Rule"

# patterns errors
for o in final["components"]["schemas"]["uploaded_documents__create"]["allOf"]:
    if o.get("properties") and "extension" in o["properties"]:
        o["properties"]["extension"]["pattern"] = "/^\.?[a-z]{2,5}$/i"

# converted to javascript \A = ^ \Z = $ multiline off by default
regex = "/(^manual_review_required$)|(((^|_)auto|_manual)_check_failed$)/"
final["components"]["schemas"]["cip_checks__update"]["properties"]["exceptions"][
    "items"
]["pattern"] = regex


with open("./openapi.json", "w") as f:
    json.dump(final, f, indent=2, default=str)


#      "cip_checks__update": {
#        "title": "Cip Checks: Update",
#        "type": "object",
#        "properties": {
#          "exception-details": {
#            "type": "string"
#          },
#          "exceptions": {
#            "type": "array",
#            "items": {
#              "type": "string",
#              "pattern": "((manual_review_required)|(((|_)auto|_manual)_check_failed))"
#            }
#          }
#        },
#        "description": ""
#      },


#       "uploaded_documents__create": {
#         "title": "Uploaded Documents: Create",
#         "allOf": [
#           {
#             "type": "object",
#             "properties": {
#               "allow-download": {
#                 "type": "boolean"
#               },
#               "public": {
#                 "type": "boolean"
#               },
#               "label": {
#                 "type": "string"
#               },
#               "description": {
#                 "type": "string"
#               }
#             }
#           },
#           {
#             "type": "object",
#             "properties": {
#               "file": {
#                 "$ref": "#/components/schemas/types__binary"
#               },
#               "extension": {
#                 "type": "string",
#                 "pattern": "/\.?[a-z]{2,5}/i"
#               },
#               "mime-type": {
#                 "type": "string"
#               }
#             },
#             "required": [
#               "file"
#             ]
#           },
#           {
#             "oneOf": [
#               {
#                 "type": "object",
#                 "properties": {
#                   "account-id": {
#                     "$ref": "#/components/schemas/types__uuid_v4"
#                   }
#                 },
#                 "required": [
#                   "account-id"
#                 ],
#                 "title": "For an Account"
#               },
#               {
#                 "type": "object",
#                 "properties": {
#                   "contact-id": {
#                     "$ref": "#/components/schemas/types__uuid_v4"
#                   }
#                 },
#                 "required": [
#                   "contact-id"
#                 ],
#                 "title": "For a Contact"
#               },
#               {
#                 "type": "object",
#                 "properties": {
#                   "account-risk-review-id": {
#                     "$ref": "#/components/schemas/types__uuid_v4"
#                   }
#                 },
#                 "required": [
#                   "account-risk-review-id"
#                 ],
#                 "title": "For an Account Risk Review"
#               },
#               {
#                 "type": "object",
#                 "properties": {
#                   "funds-transfer-id": {
#                     "$ref": "#/components/schemas/types__uuid_v4"
#                   }
#                 },
#                 "required": [
#                   "funds-transfer-id"
#                 ],
#                 "title": "For a Funds Transfer"
#               }
#             ]
#           }
#         ],
#         "description": ""
#       },
#
