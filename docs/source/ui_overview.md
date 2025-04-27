(ui_overview)=

# User Guide

The operation panel is located at 3DView > Tool > Structured Renamer. It has two display modes: Renaming Mode and Edit Mode.

## Renaming Mode

```{image} _static/renaming_ui.png
:align: right
:width: 36%
:alt: Renaming Mode UI
```

This is the screen for pattern selection and actual renaming operations.

### Naming Patterns

- This is a list of naming patterns. The selected pattern will be used for the actual renaming operation.
- If there is a `*` next to the pattern name, it means changes are not reflected in the cache. Press the reload button ({material-regular}`sync`) to reflect the changes before performing renaming operations.

::::{warning}

- Settings are saved in user preferences. If you exit Blender without saving, your settings will be lost!
- When AutoSave ({material-regular}`save`) is enabled, settings will be automatically saved each time you exit Edit Mode.

::::

(Import/Export)=

#### Import / Export

- Naming Patterns can be imported/exported as JSON files.

Related: {ref}`FilePaths`, {ref}`JsonSchema`

### Enter Edit Mode

- Switch to Edit Mode to edit patterns (add, delete, or reorder elements).
For details, see {ref}`Edit Mode`.

<!-- ### Target Area -->
<!-- - Specify the selection area for renaming (e.g., 3D View, Outliner). -->
<!-- Coming soon... -->

### Name Elements

- Displays a list of naming elements for the selected pattern.
- Each element has item buttons (e.g., {bdg-secondary}`Spine`, {bdg-secondary}`Arm`, {bdg-secondary}`Leg`, etc.).
- Pressing an item button adds or replaces the element in the selected object's name.
- Use the delete button to remove the element from the name.
- For counter elements, press "..." at the end to specify manually.

---

(Edit Mode)=

## Edit Mode

```{image} _static/editor_ui.png
:align: right
:width: 36%
:alt: Edit Mode UI
```

This is the screen for editing patterns (adding, deleting, or reordering elements).

### Exit Edit Mode

- Closes the editing screen and returns to Renaming Mode.
- Updates the regular expression cache for modified patterns.

### Name Elements

- This is a list of name elements. The order represents the word order (e.g., the first item is Prefix, the last item is Suffix).
- You can toggle enable/disable, change order, add, and delete elements.
- Press the Preview button to see random combinations based on current settings.

:::{admonition} Pattern Constraints
:class: caution

A pattern requires at least one text element and one counter element.
<!-- For details, see {ref}`deprecated_settings`. -->
:::

### Element Settings

Settings for each element.

#### Common Settings

Enabled
: When disabled, the element is excluded from the pattern.

Element Type
: You can select Text, Position, or Counter.

Display Name
: A freely configurable display name.

Separator
: A string inserted between the previous element and the current word. Not required for the first element. (e.g., "Prefix" + "_Middle" + "-Suffix")
  You can select Underscore(`_`), Dash(`-`), Dot(`.`), Space(` `), or None.

Boundary Detection
: This option is only available when Separator is set to None.

  When enabled, boundary detection is performed for UpperCamelCase and lowerCamelCase.\
  When disabled (recommended), no boundary detection is performed for any element in the pattern.

#### Text Element

<!-- :::{image} _static/edit_textitem.png -->

Text Items
: Specifies the actual strings to be used.

:::{admonition} Text Element Constraints
:class: caution

Empty elements cannot be used.\
If there are two or more TextElements with the same separator and text items, false detection may occur.
:::

#### Position Element

:::{image} _static/edit_pos.png
:align: right
:width: 36%
:alt: Position Element UI
:::

Specifies identifiers for the X, Y, and Z axes.

X Axis
: Uses left/right identifiers.

X Axis Type
: Select left/right identifiers.
  Choose from "L / R", "l / r", "Left / Right", "left / right".

Y Axis
: Uses depth identifiers.
  Only "Fr / Bk" is available.

Z Axis
: Uses height identifiers.
  Only "Top / Bot" is available.

:::{admonition} Difference between TextElement and PositionElement
:class: note

This is for detecting short words like "L / R". Detection is performed with the separator.
However, since TextElement can now detect 1-2 character words, the only difference is in the words handled.

Note that Y Axis and Z Axis identifiers are fixed to correspond with Blender's mirroring.
([Blender-Manual: Naming](https://docs.blender.org/manual/en/latest/animation/armatures/bones/editing/naming.html))

:::

:::{admonition} Position Element Constraints
:class: caution

If multiple PositionElements use the same axis in the same pattern, false detection may occur.
:::

#### Numeric Counter

:::{image} _static/edit_ncounter.png
:align: right
:width: 36%
:alt: Numeric Counter UI
:::

Padding
: Specifies the number of digits for the counter. (001, 01, 1)

Count up
: When renaming multiple objects, the counter will be sequential.

:::{admonition} Numeric Counter Constraints
:class: caution

Numbers exceeding the counter's digit count are not expected.\
Two or more counters must have different separators and padding.
:::
