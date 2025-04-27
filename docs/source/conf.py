# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Structured Renamer"
copyright = "2025, Pluglug"
author = "Pluglug"
release = "1.0"

# sphinx-build -b gettext docs/source docs/build/gettext
language = "en"  # デフォルト言語
locale_dirs = ["locale/"]  # 翻訳ディレクトリのパス
gettext_compact = False    # ファイルごとにpotファイルを生成
gettext_uuid = True        # 翻訳者向けのコメント追加

# # 言語切り替えの設定
# html_theme_options = {
#     "announcement": """
#     <div style="text-align: center;">
#         <a href="javascript:void(0)" onclick="switchLanguage('ja')">日本語</a> | 
#         <a href="javascript:void(0)" onclick="switchLanguage('en')">English</a>
#     </div>
#     """
# }

# カスタムJavaScriptを追加
html_js_files = [
    'mermaid_reinit.js',
    'language_switcher.js',
]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

html_static_path = ['_static']

extensions = [
    # Sphinx built-in extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",  # Google/Numpy形式のDocstring対応
    "sphinx.ext.viewcode",  # ソースコード表示
    "sphinx.ext.intersphinx",  # 外部ドキュメントへのリンク
    "sphinx.ext.inheritance_diagram",  # 継承関係の図
    "sphinx.ext.graphviz",  # クラス図
    # Third-party extensions
    "sphinx_automodapi.automodapi",  # モジュールのAPIドキュメント
    "sphinxcontrib.mermaid",  # マーメイド図
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    # "sphinx_rtd_theme",  # Furo theme is used, so this is not needed
    "atsphinx.color_text",
    "sphinx_togglebutton",
]

templates_path = ["_templates"]
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
exclude_patterns = []

# -- MyST Parser configuration -----------------------------------------------
myst_enable_extensions = [
    "colon_fence",    # Enables ```{directive} syntax
    "deflist",        # Enables definition lists
    "fieldlist",      # Enables field lists (like :key: value)
    "html_image",     # Enables standard image syntax for HTML builds
    # Add other extensions as needed, e.g.:
    # "dollarmath",
    # "amsmath",
    # "html_admonition",
    # "smartquotes",
    # "tasklist",
]
# myst_url_schemes = ["http", "https", "mailto"] # Optional: Define allowed URL schemes

# -- Autodoc configuration ---------------------------------------------------
autodoc_mock_imports = ["bpy", "mathutils"]

# -- Inheritance Diagram configuration ---------------------------------------
inheritance_graph_attrs = dict(rankdir="TB", size='"6.0, 8.0"')
inheritance_node_attrs = dict(
    shape="rect", fontsize=12, height=0.4, margin='"0.08, 0.03"'
)

# -- Mermaid configuration ---------------------------------------------------
mermaid_params = [
    "--theme", "mc",
    "--width", "100%",
    "--backgroundColor", "transparent",
]
mermaid_version = "11.2.0"  # 使用するMermaidのバージョン
mermaid_output_format = "raw"  # HTML出力時はJavaScriptで描画
mermaid_include_elk = "0.1.4"  # ELKレイアウトを有効化
mermaid_init_js = """
mermaid.initialize({
  startOnLoad: true,
  theme: 'mc',
  themeVariables: { klassStyle: 'classic' },
  layoutEngine: 'elk'
})
"""

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_title = "Structured Renamer"
html_static_path = ["_static"]
# html_theme_options = {
#     # Add Furo theme options here if needed
#     # "announcement": "...",
#     # "light_css_variables": { ... },
# }
# html_logo = "_static/logo.png" # Optional: Add a logo
# html_favicon = "_static/favicon.ico" # Optional: Add a favicon
