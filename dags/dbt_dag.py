from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping
from datetime import datetime
import os

profile_config = ProfileConfig(
    profile_name = "default",
    target_name = "dev",
    profile_mapping = SnowflakeUserPasswordProfileMapping(
        conn_id = "snowflake_conn",
        profile_args = {"database": "dbt_db", "schema": "dbt_schema"}
    )
)

dbt_snowflake_dag = DbtDag(
    ProjectConfig = ProjectConfig("/users/local/airflow/dags/dbt/data_pipeline",),
    operator_args={"install_deps": True},
    profile_config = profile_config,
    execution_config = ExecutionConfig(dbt_executable_path=f"{os.environ.get("C:\Users\NathanDzreke-Poku\Downloads", "/users/local/bin/dbt")}"),
    schedule_interval = "@daily",
    start_date = datetime(2023, 9, 10),
    catchup = False,
    dag_id = "dbt_dag",
)