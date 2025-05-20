(getting_started)=

# Getting Started

## Installation

::::{tab-set}

:::{tab-item} Blender 4.2 and later

1.  Download the add-on's `.zip` file from your purchase platform (Gumroad, Blender Market, etc.).
2.  Open Blender and select **Edit > Preferences**.

```{image} _static/install.png
:alt: install from disk
:width: 50%
:align: right
```

3.  Go to the **Add-ons** tab, click the {material-regular}`keyboard_arrow_down` in the top right, then click **Install from Disk...**.
4.  Select the downloaded `.zip` file and click **Install Add-on**.

:::

:::{tab-item} Blender 4.1 and earlier

1.  Download the add-on's `.zip` file from your purchase platform (Gumroad, Blender Market, etc.).
2.  Open Blender and select **Edit > Preferences**.
3.  Go to the **Add-ons** tab and click the **Install...** button.
4.  Select the downloaded `.zip` file and click **Install Add-on**.

:::

::::

## Quickstart

Once the add-on is enabled, the "Structured Renamer" panel will appear in the **Tools** tab of the 3D Viewport's sidebar.

::::{admonition} Note   

Currently, Structured Renamer primarily supports renaming **Objects** and **Bones** (including EditBones and PoseBones) in the 3D Viewport. I am actively working on extending support to other editors and data types, such as the Outliner, Node Editor, Sequence Editor, and File Browser. Your feedback on which features or data types you'd like to see prioritized is highly valuable! Please share your thoughts and suggestions on the [Blender Artists](https://blenderartists.org/t/add-on-structured-renamer/1590670).

::::

### Basic Renaming Procedure

1.  **Select a Pattern:** Choose the naming pattern you want to use from the **Naming Patterns** dropdown at the top of the panel.
2.  **Select Objects:** Select one or more objects in the 3D viewport that you want to rename.
3.  **Apply Elements:** The **Name Elements** section of the panel displays the elements of the selected pattern.
    *   **Click text element buttons (e.g., {bdg-secondary}`CTRL`, {bdg-secondary}`Arm`):** Adds or replaces the element in the selected object's name.
    *   **Click position element buttons (e.g., {bdg-secondary}`.L`, {bdg-secondary}`.R`):** Applies identifiers for left/right, etc.
    *   **Click counter element buttons (e.g., {bdg-secondary}`01`):** Adds sequential numbers. Click the last "..." to specify a number manually.
    *   **Click delete button (e.g., {material-regular}`delete`):** Removes the element from the name.

#### Example: Renaming "Bone" to "CTRL_Arm-01.L"

1.  Select the `Bone` object.
2.  Select an appropriate pattern.
3.  Click `CTRL` and `Arm` from the Text Element item buttons. (Becomes `CTRL_Arm`)
4.  Click `.L` from the Position Element item buttons. (Becomes `CTRL_Arm.L`)
5.  Click `01` from the Counter Element item buttons. (Becomes `CTRL_Arm-01.L`)
    *   *(Separators and order depend on the selected pattern settings)*

#### Trying Other Presets

Once you're familiar with the default patterns, try other presets.
The add-on includes various presets for different purposes (rigging, characters, motion graphics, etc.).

1.  Click the import button ({material-regular}`download`) in the **Naming Patterns** section at the top of the panel.
2.  When the file browser opens, navigate to the `resources/presets` folder in the add-on directory. (Usually opens automatically)
3.  Select and import preset files you want to try, such as `vrm.json`, `hardsurface.json`, `archviz.json`, etc.
4.  The imported patterns will be added to the **Naming Patterns** dropdown.

For details: {ref}`Import/Export`

### Editing Patterns

*   For more detailed settings or to create new patterns, click the **Enter Edit Mode** button at the top of the panel to switch to **Edit Mode**.
*   When editing is complete, use **Exit Edit Mode** to return to **Renaming Mode**.

### More Information

*   For details about each UI element, see {ref}`ui_overview`.
*   For concepts about naming patterns and elements, see {ref}`concepts`.
