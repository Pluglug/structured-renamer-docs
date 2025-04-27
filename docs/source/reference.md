# Reference

(FilePaths)=

## File Paths

These are the locations where presets are stored.

::::{tab-set}

:::{tab-item} Windows
Factory Preset

```{code-block}
C:\Users\<your_name>\AppData\Roaming\Blender Foundation\Blender\<Version>\scripts\addons\structured_renamer\resources\presets\patterns.json
```

User Preset

```{code-block}
C:\Users\<your_name>\AppData\Roaming\Blender Foundation\Blender\<Version>\config\addons\structured_renamer\presets\patterns.json
```

Backup

```{code-block}
C:\Users\<your_name>\AppData\Roaming\Blender Foundation\Blender\<Version>\config\addons\structured_renamer\backups\stdr_backup_<datetime>.json
```

:::

:::{tab-item} macOS

Factory Preset

```{code-block}
/Users/<your_name>/Library/Application Support/Blender/<Version>/scripts/addons/structured_renamer/resources/presets/patterns.json
```

User Preset

```{code-block}
/Users/<your_name>/Library/Application Support/Blender/<Version>/config/addons/structured_renamer/presets/patterns.json
```

Backup

```{code-block}
/Users/<your_name>/Library/Application Support/Blender/<Version>/config/addons/structured_renamer/backups/stdr_backup_<datetime>.json
```

:::

:::{tab-item} Linux

Factory Preset

```{code-block}
$HOME/.config/blender/<Version>/scripts/addons/structured_renamer/resources/presets/patterns.json
```

User Preset

```{code-block}
$HOME/.config/blender/<Version>/config/addons/structured_renamer/presets/patterns.json
```

Backup

```{code-block}
$HOME/.config/blender/<Version>/config/addons/structured_renamer/backups/stdr_backup_<datetime>.json
```

:::

::::

:::{admonition} Note
:class: important

When the addon file is updated, the preset file inside the addon file will be overwritten.
Therefore, it is necessary to save the user preset and backup in a different directory from the addon file.
:::

(JsonSchema)=

## Json Schema

A JSON schema that defines the structure of the naming pattern.
If you want to edit the JSON file in an external editor, please refer to this JSON Schema.

```{versionadded} 0.8.0
```

:::{code-block} json
{
    "type": "object",
    "properties": {
        // Specify the current version 1.0.0.
        "version": {
            "type": "array",
            "description": "Addon version when the file was exported.",
            "minItems": 3,
            "maxItems": 3,
            "items": {"type": "integer", "minimum": 0},
        },
        "patterns": {
            "type": "array",
            "description": "List of naming patterns.",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string",
                        "description": "Unique identifier for the pattern.",
                        "pattern": "^[a-zA-Z0-9_]+$",
                    },
                    "name": {
                        "type": "string",
                        "description": "Display name of the pattern.",
                        "minLength": 1,
                    },
                    "elements": {
                        "type": "array",
                        "description": "List of elements within the pattern.",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "string",
                                    "description": "Unique identifier for the element.",
                                    "pattern": "^[a-zA-Z0-9_]+$",
                                },
                                "display_name": {
                                    "type": "string",
                                    "description": "Display name of the element.",
                                    "minLength": 1,
                                },
                                "type": {
                                    "type": "string",
                                    "description": "Type of the element.",
                                    "enum": ["text", "position", "numeric_counter"],
                                },
                                "enabled": {
                                    "type": "boolean",
                                    "description": "Whether the element is enabled.",
                                },
                                "order": {
                                    "type": "integer",
                                    "description": "Display order of the element.",
                                    "minimum": 0,
                                },
                                "separator": {
                                    "type": "string",
                                    "description": "Separator character used after this element.",
                                    "enum": ["UNDERSCORE", "DOT", "DASH", "SPACE", "NONE"],
                                },
                                // Type-specific properties
                                "items": {
                                    "type": "array",
                                    "items": {"type": "string"},
                                    "description": "List of text items (for 'text' type).",
                                },
                                "padding": {
                                    "type": "integer",
                                    "description": "Padding for the counter (for 'numeric_counter' type).",
                                    "minimum": 0,
                                },
                                "count_up": {
                                    "type": "boolean",
                                    "description": "Whether the counter counts up (for 'numeric_counter' type).",
                                },
                                "xaxis_type": {
                                    "type": "string",
                                    "description": "Representation for X-axis (for 'position' type).",
                                    "enum": [
                                        "L|R",
                                        "l|r",
                                        "LEFT|RIGHT",
                                        "Left|Right",
                                        "left|right"
                                    ]
                                },
                                "xaxis_enabled": {
                                    "type": "boolean",
                                    "description": "Whether X-axis is enabled (for 'position' type).",
                                },
                                "yaxis_enabled": {
                                    "type": "boolean",
                                    "description": "Whether Y-axis is enabled (for 'position' type).",
                                },
                                "zaxis_enabled": {
                                    "type": "boolean",
                                    "description": "Whether Z-axis is enabled (for 'position' type).",
                                },
                            },
                            "required": [
                                "id",
                                "display_name",
                                "type",
                                "enabled",
                                "order",
                                "separator",
                            ],
                            "allOf": [
                                {
                                    "if": {"properties": {"type": {"const": "text"}}},
                                    "then": {"required": ["items"]},
                                },
                                {
                                    "if": {
                                        "properties": {
                                            "type": {"const": "numeric_counter"}
                                        }
                                    },
                                    "then": {"required": ["padding", "count_up"]},
                                },
                                {
                                    "if": {
                                        "properties": {"type": {"const": "position"}}
                                    },
                                    "then": {
                                        "required": [
                                            "xaxis_type",
                                            "xaxis_enabled",
                                            "yaxis_enabled",
                                            "zaxis_enabled",
                                        ]
                                    },
                                },
                            ],
                        },
                    },
                },
                "required": ["id", "name", "elements"],
            },
        },
    },
    "required": ["version", "patterns"],
}
:::

(concepts)=

# Concepts

## Pattern & Element

Core class structure for managing naming elements and patterns.

:::{mermaid}

classDiagram
   direction LR
   class NamingPattern {
      +elements: List[INameElement]
      +parse_name(name: str)
      +update_elements(updates: Dict)
      +render_name() str
   }
   class NameElement {
      +id: str
      +order: int
      +enabled: bool
      +separator: str
      +value: str
      # _pattern: regex.Pattern
      +parse(name: str) bool
      +set_value(value: Any)
      +render() tuple[sep: str, value: str]
      }
   class CounterElement{
      +padding: int
      +increment()
      #_build_pattern() str
   }
   class PositionElement{
      +position_values: List[str]
      #_build_pattern() str
   }
   class TextElement{
      +items: List[str]
      #_build_pattern() str
   }

   NamingPattern "1" -- "n" NameElement
   NameElement <|.. TextElement
   NameElement <|.. PositionElement
   NameElement <|.. CounterElement

:::

## Decomposition & Reconstruction

Basic flow of name decomposition, update, and reconstruction.

:::{mermaid}
graph LR
    A[DEF-Arm-01.L] --> B{parse_name}
    B --> |Prefix| C[DEF] 
    B --> |Middle| D[Arm] 
    B --> |Counter| E[01] 
    B --> |Position| F[L]
    G["{'Prefix': 'CTRL', 'Middle': 'Spine'}"] --> |User Input| H{update_elements}
    C & D --> H
    H --> I[CTRL] & J[Spine]
    I & J & E & F --> K{render_name}
    K --> L[CTRL-Spine-01.L]
:::
