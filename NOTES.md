Frequency Rule
pattern: \\A \\Z ? 


replace resource-tokens/{hash with resource-tokens/{resource-token-id
replaced "decription": "" 1493 replacements
hash must be replaced with location dependent variables to make sense

adding discriminator to contacts__update did not correct issue with generate


hash
          {
            "style": "simple",
            "in": "path",
            "name": "card-holder-id",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/types__uuid_v4"
            }
          }
          
          
          {
            "style": "simple",
            "in": "path",
            "name": "hash",
            "required": true,
            "description": "The resource token hash to authenticate this request",
            "schema": {
              "type": "string"
            }
          }
