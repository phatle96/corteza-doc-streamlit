import streamlit as st

st.set_page_config(page_title="Common Corteza workflow tasks", layout="wide")

st.markdown("# Common Corteza workflow tasks")
st.sidebar.markdown("# Common Corteza workflow tasks")

st.markdown(" ## 1. How to make a call to an external API whenever a Corteza user takes an action with a record")
st.expander("Workflow template", expanded=False).markdown("""
```json
{
  "workflows": [
    {
      "handle": "record-action-trigger",
      "enabled": true,
      "meta": {
        "name": "[TY] Record action trigger",
        "description": "",
        "visual": null
      },
      "keepSessions": 0,
      "steps": [
        {
          "stepID": "4",
          "kind": "function",
          "ref": "httpRequestSend",
          "arguments": [
            {
              "target": "url",
              "expr": "webhookUrl",
              "type": "String"
            },
            {
              "target": "method",
              "value": "POST",
              "type": "String"
            },
            {
              "target": "params",
              "expr": "event",
              "type": "KVV"
            },
            {
              "target": "headers",
              "value": "  {\"Content-Type\": [\n      \"application/json\"\n    ]\n    }",
              "type": "KVV"
            },
            {
              "target": "body",
              "expr": "stringifyValue",
              "type": "String"
            }
          ],
          "results": [],
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "defaultName": true,
              "id": "4",
              "parent": "55",
              "value": "Send to webhook (for testing)",
              "xywh": [
                432,
                48,
                200,
                80
              ]
            }
          }
        },
        {
          "stepID": "20",
          "kind": "debug",
          "ref": "",
          "arguments": null,
          "results": [],
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "defaultName": true,
              "id": "20",
              "parent": "1",
              "value": "Logs current workflow scope into server logs. If workflow debug is enabled",
              "xywh": [
                3000,
                2304,
                200,
                80
              ]
            }
          }
        },
        {
          "stepID": "30",
          "kind": "function",
          "ref": "jsenvExecute",
          "arguments": [
            {
              "target": "scope",
              "expr": "record",
              "type": "Any"
            },
            {
              "target": "source",
              "value": "var stringifyValue\n\ntry {\n    return JSON.stringify(input)\n} catch (e) {\n    return 'could not stringify: ' + e.message\n}",
              "type": "String"
            }
          ],
          "results": [
            {
              "target": "stringifyValue",
              "expr": "resultString",
              "type": "String"
            }
          ],
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "defaultName": true,
              "id": "30",
              "parent": "1",
              "value": "Process arbitrary data in jsenv",
              "xywh": [
                3296,
                2096,
                200,
                80
              ]
            }
          }
        },
        {
          "stepID": "33",
          "kind": "expressions",
          "ref": "",
          "arguments": [
            {
              "target": "sendtoEmail",
              "expr": "true",
              "type": "Boolean"
            },
            {
              "target": "sendtoWebhook",
              "expr": "true",
              "type": "Boolean"
            },
            {
              "target": "debug",
              "expr": "false",
              "type": "Boolean"
            }
          ],
          "results": [],
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "defaultName": true,
              "id": "33",
              "parent": "1",
              "value": "Define and mutate scope variables",
              "xywh": [
                2696,
                2096,
                200,
                80
              ]
            }
          }
        },
        {
          "stepID": "40",
          "kind": "expressions",
          "ref": "",
          "arguments": [
            {
              "target": "event",
              "expr": "{\"eventType\":[\"afterCreate\"]}",
              "type": "KVV"
            }
          ],
          "results": [],
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "defaultName": true,
              "id": "40",
              "parent": "1",
              "value": "Define and mutate scope variables",
              "xywh": [
                2352,
                1936,
                200,
                80
              ]
            }
          }
        },
        {
          "stepID": "42",
          "kind": "expressions",
          "ref": "",
          "arguments": [
            {
              "target": "event",
              "expr": "{\"eventType\":[\"afterUpdate\"]}",
              "type": "KVV"
            }
          ],
          "results": [],
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "defaultName": true,
              "id": "42",
              "parent": "1",
              "value": "Define and mutate scope variables",
              "xywh": [
                2352,
                2096,
                200,
                80
              ]
            }
          }
        },
        {
          "stepID": "44",
          "kind": "expressions",
          "ref": "",
          "arguments": [
            {
              "target": "event",
              "expr": "{\"eventType\":[\"afterDelete\"]}",
              "type": "KVV"
            },
            {
              "target": "record",
              "expr": "oldRecord",
              "type": "ComposeRecord"
            }
          ],
          "results": [],
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "defaultName": true,
              "id": "44",
              "parent": "1",
              "value": "Define and mutate scope variables",
              "xywh": [
                2352,
                2272,
                200,
                80
              ]
            }
          }
        },
        {
          "stepID": "47",
          "kind": "expressions",
          "ref": "",
          "arguments": [
            {
              "target": "event",
              "expr": "{\"eventType\":[\"afterUndelete\"]}",
              "type": "KVV"
            },
            {
              "target": "record",
              "expr": "oldRecord",
              "type": "ComposeRecord"
            }
          ],
          "results": [],
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "defaultName": true,
              "id": "47",
              "parent": "1",
              "value": "Define and mutate scope variables",
              "xywh": [
                2352,
                2424,
                200,
                80
              ]
            }
          }
        },
        {
          "stepID": "50",
          "kind": "visual",
          "ref": "swimlane",
          "arguments": null,
          "results": [],
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "defaultName": false,
              "id": "50",
              "parent": "1",
              "value": "Create",
              "xywh": [
                1952,
                1896,
                648,
                144
              ]
            }
          }
        },
        {
          "stepID": "51",
          "kind": "visual",
          "ref": "swimlane",
          "arguments": null,
          "results": [],
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "defaultName": false,
              "id": "51",
              "parent": "1",
              "value": "Update",
              "xywh": [
                1952,
                2056,
                648,
                144
              ]
            }
          }
        },
        {
          "stepID": "52",
          "kind": "visual",
          "ref": "swimlane",
          "arguments": null,
          "results": [],
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "defaultName": false,
              "id": "52",
              "parent": "1",
              "value": "Delete",
              "xywh": [
                1952,
                2232,
                648,
                144
              ]
            }
          }
        },
        {
          "stepID": "53",
          "kind": "visual",
          "ref": "swimlane",
          "arguments": null,
          "results": [],
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "defaultName": false,
              "id": "53",
              "parent": "1",
              "value": "Restore",
              "xywh": [
                1952,
                2392,
                648,
                144
              ]
            }
          }
        },
        {
          "stepID": "54",
          "kind": "function",
          "ref": "emailSend",
          "arguments": [
            {
              "target": "subject",
              "expr": "mailSubject",
              "type": "String"
            },
            {
              "target": "from",
              "expr": "mailFrom",
              "type": "String"
            },
            {
              "target": "to",
              "expr": "mailTo",
              "type": "String"
            },
            {
              "target": "plain",
              "expr": "stringifyValue",
              "type": "String"
            }
          ],
          "results": [],
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "defaultName": true,
              "id": "54",
              "parent": "56",
              "value": "Email",
              "xywh": [
                432,
                40,
                200,
                80
              ]
            }
          }
        },
        {
          "stepID": "55",
          "kind": "visual",
          "ref": "swimlane",
          "arguments": null,
          "results": [],
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "defaultName": false,
              "id": "55",
              "parent": "1",
              "value": "Webhook",
              "xywh": [
                3984,
                2048,
                680,
                160
              ]
            }
          }
        },
        {
          "stepID": "56",
          "kind": "visual",
          "ref": "swimlane",
          "arguments": null,
          "results": [],
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "defaultName": false,
              "id": "56",
              "parent": "1",
              "value": "Email",
              "xywh": [
                3984,
                2264,
                680,
                160
              ]
            }
          }
        },
        {
          "stepID": "57",
          "kind": "gateway",
          "ref": "incl",
          "arguments": null,
          "results": [],
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "defaultName": true,
              "id": "57",
              "parent": "1",
              "value": "Inclusive",
              "xywh": [
                3600,
                2096,
                200,
                80
              ]
            }
          }
        },
        {
          "stepID": "60",
          "kind": "expressions",
          "ref": "",
          "arguments": [
            {
              "target": "mailSubject",
              "expr": "\"Record event: \" + toJSON(event)",
              "type": "String"
            },
            {
              "target": "mailFrom",
              "expr": "\"no-reply@phatle.dev\"",
              "type": "String"
            },
            {
              "target": "mailTo",
              "expr": "\"phatlv96@gmail.com\"",
              "type": "String"
            }
          ],
          "results": [],
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "defaultName": true,
              "id": "60",
              "parent": "56",
              "value": "Define and mutate scope variables",
              "xywh": [
                104,
                40,
                200,
                80
              ]
            }
          }
        },
        {
          "stepID": "63",
          "kind": "expressions",
          "ref": "",
          "arguments": [
            {
              "target": "webhookUrl",
              "expr": "\"https://webhook.site/dff12378-5861-4cf0-9972-be36ebfb1d47\"",
              "type": "String"
            }
          ],
          "results": [],
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "defaultName": true,
              "id": "63",
              "parent": "55",
              "value": "Define and mutate scope variables",
              "xywh": [
                104,
                48,
                200,
                80
              ]
            }
          }
        },
        {
          "stepID": "65",
          "kind": "termination",
          "ref": "",
          "arguments": null,
          "results": [],
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "defaultName": true,
              "id": "65",
              "parent": "1",
              "value": "Terminate workflow execution",
              "xywh": [
                4864,
                2096,
                200,
                80
              ]
            }
          }
        },
        {
          "stepID": "76",
          "kind": "gateway",
          "ref": "excl",
          "arguments": null,
          "results": [],
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "defaultName": true,
              "id": "76",
              "parent": "1",
              "value": "Exclusive",
              "xywh": [
                2992,
                2096,
                200,
                80
              ]
            }
          }
        }
      ],
      "paths": [
        {
          "parentID": "33",
          "childID": "76",
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "id": "34",
              "parent": "1",
              "points": [],
              "style": "exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;",
              "value": null
            }
          }
        },
        {
          "parentID": "40",
          "childID": "33",
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "id": "41",
              "parent": "1",
              "points": [],
              "style": "exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.25;entryDx=0;entryDy=0;",
              "value": null
            }
          }
        },
        {
          "parentID": "42",
          "childID": "33",
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "id": "43",
              "parent": "1",
              "points": [],
              "style": "exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;",
              "value": null
            }
          }
        },
        {
          "parentID": "44",
          "childID": "33",
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "id": "45",
              "parent": "1",
              "points": [],
              "style": "exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.75;entryDx=0;entryDy=0;",
              "value": null
            }
          }
        },
        {
          "parentID": "47",
          "childID": "33",
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "id": "49",
              "parent": "1",
              "points": [],
              "style": "exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;",
              "value": null
            }
          }
        },
        {
          "expr": "sendtoWebhook == true",
          "parentID": "57",
          "childID": "63",
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "id": "58",
              "parent": "1",
              "points": [],
              "style": "exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;",
              "value": "sendtoWebhook"
            }
          }
        },
        {
          "parentID": "63",
          "childID": "4",
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "id": "64",
              "parent": "55",
              "points": [],
              "style": "exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;",
              "value": null
            }
          }
        },
        {
          "parentID": "4",
          "childID": "65",
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "id": "66",
              "parent": "1",
              "points": [],
              "style": "exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;",
              "value": null
            }
          }
        },
        {
          "parentID": "30",
          "childID": "57",
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "id": "71",
              "parent": "1",
              "points": [],
              "style": "exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;",
              "value": null
            }
          }
        },
        {
          "expr": "sendtoEmail == true",
          "parentID": "57",
          "childID": "60",
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "id": "72",
              "parent": "1",
              "points": [],
              "style": "exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;",
              "value": "sendtoEmail"
            }
          }
        },
        {
          "parentID": "54",
          "childID": "65",
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "id": "74",
              "parent": "1",
              "points": [],
              "style": "exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;",
              "value": null
            }
          }
        },
        {
          "parentID": "60",
          "childID": "54",
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "id": "75",
              "parent": "56",
              "points": [],
              "style": "exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;",
              "value": null
            }
          }
        },
        {
          "expr": "debug == false",
          "parentID": "76",
          "childID": "30",
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "id": "79",
              "parent": "1",
              "points": [],
              "style": "exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;",
              "value": "#1 - If"
            }
          }
        },
        {
          "expr": "debug == true",
          "parentID": "76",
          "childID": "20",
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "id": "80",
              "parent": "1",
              "points": [],
              "style": "exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;",
              "value": "#2 - Else (if)"
            }
          }
        },
        {
          "parentID": "20",
          "childID": "30",
          "meta": {
            "name": "",
            "description": "",
            "visual": {
              "id": "81",
              "parent": "1",
              "points": [],
              "style": "exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;",
              "value": null
            }
          }
        }
      ],
      "triggers": [
        {
          "resourceType": "compose:record",
          "eventType": "afterCreate",
          "constraints": [],
          "enabled": true,
          "stepID": "40",
          "meta": {
            "description": "",
            "visual": {
              "defaultName": true,
              "edges": [
                {
                  "childID": "40",
                  "meta": {
                    "description": "",
                    "label": "",
                    "visual": {
                      "id": "7",
                      "parent": "1",
                      "points": [],
                      "style": "exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;",
                      "value": null
                    }
                  },
                  "parentID": "3"
                }
              ],
              "id": "3",
              "parent": "1",
              "value": "Compose record - afterCreate",
              "xywh": [
                2064,
                1936,
                200,
                80
              ]
            }
          }
        },
        {
          "resourceType": "compose:record",
          "eventType": "afterUpdate",
          "constraints": [],
          "enabled": true,
          "stepID": "42",
          "meta": {
            "description": "",
            "visual": {
              "defaultName": true,
              "edges": [
                {
                  "childID": "42",
                  "meta": {
                    "description": "",
                    "label": "",
                    "visual": {
                      "id": "36",
                      "parent": "1",
                      "points": [],
                      "style": "exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;",
                      "value": null
                    }
                  },
                  "parentID": "35"
                }
              ],
              "id": "35",
              "parent": "1",
              "value": "Compose record - afterUpdate",
              "xywh": [
                2064,
                2096,
                200,
                80
              ]
            }
          }
        },
        {
          "resourceType": "compose:record",
          "eventType": "afterDelete",
          "constraints": [],
          "enabled": true,
          "stepID": "44",
          "meta": {
            "description": "",
            "visual": {
              "defaultName": true,
              "edges": [
                {
                  "childID": "44",
                  "meta": {
                    "description": "",
                    "label": "",
                    "visual": {
                      "id": "38",
                      "parent": "1",
                      "points": [],
                      "style": "exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;",
                      "value": null
                    }
                  },
                  "parentID": "37"
                }
              ],
              "id": "37",
              "parent": "1",
              "value": "Compose record - afterDelete",
              "xywh": [
                2064,
                2272,
                200,
                80
              ]
            }
          }
        },
        {
          "resourceType": "compose:record",
          "eventType": "afterUndelete",
          "constraints": [],
          "enabled": true,
          "stepID": "47",
          "meta": {
            "description": "",
            "visual": {
              "defaultName": true,
              "edges": [
                {
                  "childID": "47",
                  "meta": {
                    "description": "",
                    "label": "",
                    "visual": {
                      "id": "48",
                      "parent": "1",
                      "points": [],
                      "style": "exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;",
                      "value": null
                    }
                  },
                  "parentID": "46"
                }
              ],
              "id": "46",
              "parent": "1",
              "value": "Compose record - afterUndelete",
              "xywh": [
                2064,
                2424,
                200,
                80
              ]
            }
          }
        }
      ]
    }
  ]
}
```
""")