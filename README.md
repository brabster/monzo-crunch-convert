Convert Monzo statement CSV files to Crunch accounting

`python convert.py statement_file_path [--final_balance balance]`

## DuckDB

- Get latest `duckdb` from https://duckdb.org/docs/installation/?version=stable&environment=cli&platform=linux&download_method=direct&architecture=x86_64
- Drop transactions files into `uncommitted`
- Run `duckdb_setup.sql`
