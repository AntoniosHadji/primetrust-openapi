import json
import time

# TODO: Frequency Rule needs _

start = time.time()
with open("./primetrust-public-resolved.json", "r") as f:
    data = json.load(f)

final = data.copy()

print("finished load.", time.time() - start)
print(type(data))
print(dir(data))
print(data.keys())
for key in data.keys():
    if isinstance(data[key], dict):
        print(key, data[key].keys())
        if key == "paths":
            for p in data[key].keys():
                print(p)
                for method in data[key][p].keys():
                    k2 = data[key][p][method]
                    if "responses" in k2:
                        for response in k2["responses"]:
                            if "description" not in k2["responses"][response]:
                                final[key][p][method]["responses"][response][
                                    "description"
                                ] = "TODO"
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
                                    del final[key][p][method]["responses"][response][
                                        "content"
                                    ]["application/vnd.api+json"]["description"]

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
                                        final[key][p][method]["responses"][response][
                                            "content"
                                        ]["application/vnd.api+json"]["schema"][
                                            "title"
                                        ] = "string"

    # elif isinstance(data[key], list):
    #     for item in data[key]:
    #         print(item)
    # else:
    #     print(key, type(data[key]), len(data[key]))

with open("./openapi.json", "w") as f:
    json.dump(final, f, indent=2, default=str)
