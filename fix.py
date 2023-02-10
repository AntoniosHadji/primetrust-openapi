#!/usr/bin/env python3
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
# dict_keys(['openapi', 'info', 'paths', 'components', 'servers', 'x-tagGroups', 'tags']) # noqa: E501
# 	 openapi <class 'str'>
# 	 info <class 'dict'>
# 	 paths <class 'dict'>
# 	 components <class 'dict'>
# 	 servers <class 'list'>
# 	 x-tagGroups <class 'list'>
# 	 tags <class 'list'>

# duplicate paths
del data["paths"]["/v2/resource-tokens/{hash}"]
del data["paths"]["/v2/contributions/{hash}"]

# remove trailing slash in dictionary key
data["paths"]["/v2/contributions"] = data["paths"].pop("/v2/contributions/")
# fix missing right brace
data["paths"]["/v2/banks/{bank_id}/address"] = data["paths"].pop(
    "/v2/banks/{bank_id/address"
)

# empty enum TODO: DC is just a placeholder.  What should be here?
data["components"]["schemas"]["state_withholding_rule__states"]["enum"] = ["DC"]

# add discriminators
data["components"]["schemas"]["contacts__update"]["discriminator"] = {
    "propertyName": "contact-type"
}
data["components"]["schemas"]["contacts__create"]["discriminator"][
    "propertyName"
] = "contact-type"
data["components"]["schemas"]["contacts__create_new_account"]["discriminator"] = {
    "propertyName": "contact-type"
}
data["components"]["schemas"]["contacts__create_primary"]["discriminator"] = {
    "propertyName": "contact-type"
}

# required field (warning)
data["info"]["contact"] = {
    "name": "Prime Trust API Support",
    "url": "https://support.primetrust.com",
    "email": "support@primetrust.com",
}

# needs security field per redocly-cli lint
for p in [
    "/auth/password_reset",
    "/auth/password_reset/{hash}",
    "/v2/card-holder-verifications/{hash}",
    "/v2/card-holder-verifications/{hash}",
    "/v2/card-holder-verifications/{hash}/request-email-verification",
    "/v2/card-holder-verifications/{hash}/request-phone-number-verification",
    "/v2/card-holder-verifications/{hash}/verify-email",
    "/v2/card-holder-verifications/{hash}/verify-phone-number",
    "/v2/cards/{hash}/display",
    "/v2/credit-card-authorization/{hash}",
    "/v2/credit-card-authorization/{hash}",
    "/v2/credit-card-authorization/{hash}/verify",
    "/v2/resource-tokens/{hash}/create-account",
    "/v2/resource-tokens/{hash}/create-agreement-preview",
    "/v2/resource-tokens/{hash}/create-contacts",
    "/v2/resource-tokens/{hash}/upload-document",
    "/v2/resource-tokens/{hash}/validate",
]:
    for method in data["paths"][p]:
        data["paths"][p][method]["security"] = [{"JWT": []}]

# missing parameters
for p in [
    "/v2/account-cash-transfer-reviews/{account-cash-transfer-review-id}/from-account",
    "/v2/account-cash-transfer-reviews/{account-cash-transfer-review-id}/to-account",
]:
    for method in data["paths"][p]:
        data["paths"][p][method]["parameters"].append(
            uuid("account-cash-transfer-review-id")
        )


for p in [
    "/v2/accounts/{account-id}/account-cash-transfers",
    "/v2/accounts/{account-id}/account-histories",
    "/v2/accounts/{account-id}/authorized-transfer-accounts",
    "/v2/accounts/{account-id}/internal-asset-transfers",
    "/v2/accounts/{account-id}/policy",
    "/v2/accounts/{account-id}/sandbox/fund",
    "/v2/accounts/{account-id}/holds",
]:
    for method in data["paths"][p]:
        data["paths"][p][method]["parameters"].append(uuid("account-id"))

for p in [
    "/v2/internal-asset-transfer-reviews/{internal-asset-transfer-review-id}/from-account",  # noqa: E501
    "/v2/internal-asset-transfer-reviews/{internal-asset-transfer-review-id}/to-account",  # noqa: E501
]:
    for method in data["paths"][p]:
        data["paths"][p][method]["parameters"].append(
            uuid("internal-asset-transfer-review-id")
        )

for p in [
    "/v2/resource-tokens/{resource-token-id}/accounts",
    "/v2/resource-tokens/{resource-token-id}/contacts",
    "/v2/resource-tokens/{resource-token-id}/uploaded-documents",
]:
    for method in data["paths"][p]:
        data["paths"][p][method]["parameters"].append(uuid("resource-token-id"))

for p in [
    "/v2/user-invitation-reviews/{user-invitation-review-id}/from-account",
    "/v2/user-invitation-reviews/{user-invitation-review-id}/to-account",
]:
    for method in data["paths"][p]:
        data["paths"][p][method]["parameters"].append(uuid("user-invitation-review-id"))

p = "/v2/banks/{bank_id}/address"
for method in data["paths"][p]:
    data["paths"][p][method]["parameters"].append(uuid("bank_id"))

p = "/v2/contributions/{contribution-id}/failures"
for method in data["paths"][p]:
    data["paths"][p][method]["parameters"].append(uuid("contribution-id"))

p = "/v2/credit-card-resources/{credit-card-resource-id}/failures"
for method in data["paths"][p]:
    data["paths"][p][method]["parameters"].append(uuid("credit-card-resource-id"))

p = "/v2/trade-settlement-configs/{trade-settlement-config-id}/trade-settlements/{trade-settlement-id}"  # noqa: E501
for method in data["paths"][p]:
    data["paths"][p][method]["parameters"].append(uuid("trade-settlement-id"))

p = "/v2/account-types/{account-type-id}/policy"
for method in data["paths"][p]:
    data["paths"][p][method]["parameters"].append(uuid("account-type-id"))

p = "/v2/card-transactions/{card-transactions-id}/sandbox"
for method in data["paths"][p]:
    data["paths"][p][method]["parameters"].append(uuid("card-transactions-id"))

p = "/v2/contact-funds-transfer-references/{contact-funds-transfer-reference-id}/sandbox/contribution"  # noqa: E501
for method in data["paths"][p]:
    data["paths"][p][method]["parameters"].append(
        uuid("contact-funds-transfer-reference-id")
    )

p = "/v2/funds-transfer-methods/{funds-transfer-method-id}/bank"
for method in data["paths"][p]:
    data["paths"][p][method]["parameters"].append(uuid("funds-transfer-method-id"))

p = "/v2/disbursement-owner-verifications/{resource-token-hash}"
for method in data["paths"][p]:
    data["paths"][p][method]["parameters"].append(uuid("resource-token-hash"))


key = "paths"
for p in data[key]:  # noqa: C901
    print("path: ", p)
    for method in data[key][p]:
        k2 = data[key][p][method]
        if "description" in k2:
            if k2["description"] == "":
                data[key][p][method]["description"] = "TODO-method-description"

        # if "security" not in k2:
        #     print(f"Needs security field. {p}")
        # else:
        #     print(f"{k2['security']} {p}")

        if "responses" in k2:
            for response in k2["responses"]:
                if "description" not in k2["responses"][response]:
                    data[key][p][method]["responses"][response][
                        "description"
                    ] = "TODO-response-description"
                elif k2["responses"][response]["description"] == "":
                    data[key][p][method]["responses"][response][
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
                        del data[key][p][method]["responses"][response]["content"][
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
                            data[key][p][method]["responses"][response]["content"][
                                "application/vnd.api+json"
                            ]["schema"]["title"] = "string"


for tag in data["tags"]:
    if tag["description"] == "":
        tag["description"] = "TODO: Fill description."


fr = data["components"]["schemas"]["Frequency Rule"]
del data["components"]["schemas"]["Frequency Rule"]
data["components"]["schemas"]["Frequency_Rule"] = fr

for o in data["components"]["schemas"]["rules__rule_type_info"]["oneOf"]:
    if "$ref" in o:
        if o["$ref"] == "#/components/schemas/Frequency Rule":
            print(f"Replace {o['$ref']}")
            o["$ref"] = "#/components/schemas/Frequency_Rule"


key = "components"
subkey = "schemas"
for c in data[key]:  # noqa: C901
    for s in data[key][subkey]:
        # print(s)
        if s == "types__date":
            print(f"Found {s}")
            print(data[key][subkey][s])
            data[key][subkey][s]["nullable"] = True
            print(data[key][subkey][s])
        if s == "contacts__response":
            print(f"Found {s}")
            print(type(data[key][subkey][s]))
            print(
                data[key][subkey][s]["properties"]["attributes"]["properties"][
                    "date-of-birth"
                ]
            )
            if (
                "nullable"
                in data[key][subkey][s]["properties"]["attributes"]["properties"][
                    "date-of-birth"
                ]
            ):
                print("found nullable")
                del data[key][subkey][s]["properties"]["attributes"]["properties"][
                    "date-of-birth"
                ]["nullable"]
            if (
                "nullable"
                in data[key][subkey][s]["properties"]["attributes"]["properties"][
                    "date-of-incorporation"
                ]
            ):
                print("found nullable")
                del data[key][subkey][s]["properties"]["attributes"]["properties"][
                    "date-of-incorporation"
                ]["nullable"]

        if s == "uploaded_documents__create":
            print(f"Found {s}")
            for o in data[key][subkey][s]["allOf"]:
                if o.get("properties") and "extension" in o["properties"]:
                    o["properties"]["extension"]["pattern"] = r"/^\.?[a-z]{2,5}$/i"

        if s == "cip_checks__update_idm":
            print(f"Found {s}")
            regex = "/(^manual_review_required$)|(^(auto|manual)_check_failed$)/"
            data[key][subkey][s]["properties"]["exceptions"]["items"]["pattern"] = regex

#  58251:26    error  oas3-schema
# `pattern` property should match format `regex`.
# components.schemas.cip_checks__update_idm.properties.exceptions.items.pattern
# "pattern":
# "(?-mix:(\\Amanual_review_required\\Z)|(((\\A|_)auto|_manual)_check_failed\\Z))"
# 57957

# converted to javascript \A = ^ \Z = $ multiline off by default
# patterns errors
# for o in data["components"]["schemas"]["uploaded_documents__create"]["allOf"]:
#     if o.get("properties") and "extension" in o["properties"]:
#         o["properties"]["extension"]["pattern"] = r"/^\.?[a-z]{2,5}$/i"
#
# broken as of 2021-10-05
# regex = "/(^manual_review_required$)|(((^|_)auto|_manual)_check_failed$)/"


with open("./openapi.json", "w") as f:
    json.dump(data, f, indent=2, default=str)
