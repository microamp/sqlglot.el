# Table of Contents

- [sqlglot.el](#sqlglot.el)
  - [Demo](#demo)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [TODOs](#todos)
  - [License](#license)

# sqlglot.el

[SQLGlot](https://sqlglot.com/sqlglot.html) is a Python library for parsing and converting SQL queries across multiple database dialects, supporting over 30 platforms like BigQuery, Snowflake, Spark, PostgreSQL, and MySQL. It serves as the foundation for [SQLMesh](https://www.tobikodata.com/sqlmesh).

This Emacs Lisp package offers an interface to SQLGlot, enabling SQL dialect conversion and code formatting directly within Emacs.

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
;; M-x sqlglot-format-region    - Format/pretty-print selected SQL
```

**Note**: When called with a prefix argument (`C-u`), all interactive functions will prompt you to specify read dialect, write dialect, and whether to delimit identifiers.

## TODOs

- [x] Rename the package from `sqlglot-transpile.el` to `sqlglot.el`

- [x] SQLGlot dialects \[2/2\]

  - [x] Remove the hardcoded list of dialects by fetching them dynamically

  - [x] Support caching via the variable `sqlglot--cached-dialects`

- [ ] Add an interface to the `optimize` function

- [ ] Use Transient for configuring read and write dialects

## License

MIT
