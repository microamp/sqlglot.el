# Table of Contents

- [sqlglot.el](#sqlglot.el)
  - [Demo](#demo)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [TODOs](#todos)
  - [License](#license)

# sqlglot.el

[SQLGlot](https://sqlglot.com/sqlglot.html) is

> a no-dependency SQL parser, transpiler, optimizer, and engine. It can be used to format SQL or translate between 30 different dialects like DuckDB, Presto / Trino, Spark / Databricks, Snowflake, and BigQuery. It aims to read a wide variety of SQL inputs and output syntactically and semantically correct SQL in the targeted dialects.

The sqlglot.el package provides an Emacs interface to SQLGlot for converting SQL between dialects and formatting code directly in the editor.

## Demo

[![asciicast](https://asciinema.org/a/fNsJYQ4yMDekpiPBrPvrEURHC.svg)](https://asciinema.org/a/fNsJYQ4yMDekpiPBrPvrEURHC)

## Prerequisites

- Python 3.9+

- SQLGlot

  ``` bash
  python -m pip install sqlglot
  ```

  e.g.

  ``` example
  ...
  Successfully installed sqlglot-27.6.0
  ```

## Installation

- Emacs 30.1+:

  ``` elisp
  (use-package sqlglot
    :ensure t
    :after sql
    :vc (:url "https://github.com/microamp/sqlglot.el" :rev :newest)
    :bind (:map
           sql-mode-map
           ("C-c C-f" . sqlglot-format-region)
           ("C-c C-c" . sqlglot-transpile-region))
    :custom
    (sqlglot-default-read-dialect "Postgres")
    (sqlglot-default-write-dialect "DuckDB")
    (sqlglot-default-identify t))
  ```

**Note**: Run `M-x sqlglot-list-dialects RET` to list all dialects supported by SQLGlot:

``` example
Supported SQL Dialects:

  Athena
  BigQuery
  ClickHouse
  Databricks
  Doris
  Dremio
  Drill
  Druid
  DuckDB
  Dune
  Exasol
  Fabric
  Hive
  Materialize
  MySQL
  Oracle
  PRQL
  Postgres
  Presto
  Redshift
  RisingWave
  SQLite
  SingleStore
  Snowflake
  Spark
  Spark2
  StarRocks
  TSQL
  Tableau
  Teradata
  Trino
```

## Usage

``` elisp
;; M-x sqlglot-transpile-region - Transpile selected SQL
;; M-x sqlglot-transpile-buffer - Transpile SQL in current buffer
;; M-x sqlglot-format-region    - Format/pretty-print selected SQL
;; M-x sqlglot-format-buffer    - Format/pretty-print SQL in current buffer
```

**Note**: When called with a prefix argument (`C-u`), all interactive functions will prompt you to specify read dialect, write dialect, and whether to delimit identifiers.

## TODOs

- [x] Rename the package from `sqlglot-transpile.el` to `sqlglot.el`

- [x] SQLGlot dialects \[2/2\]

  - [x] Remove the hardcoded list of dialects by fetching them dynamically

  - [x] Support caching via the variable `sqlglot--cached-dialects`

- [ ] Add `sqlglot-transpile-buffer`

- [ ] Add `sqlglot-format-buffer`

- [ ] Add an interface to the `sqlglot.optimize` function

- [ ] Use Transient for configuring read and write dialects

## License

MIT
