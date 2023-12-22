from dagster_duckdb import DuckDBResource
from dagster import EnvVar

"""
  - EnvVar fetches the environmental variable’s value every time a run starts
  - os.getenv fetches the environment variable when the code location is loaded
  
  By using EnvVar instead of os.getenv, you can dynamically customize a resource’s configuration.
  For example, you can change which DuckDB database is being used without having to restart Dagster’s web server.
"""

database_resource = DuckDBResource(
    database=EnvVar("DUCKDB_DATABASE")
)
