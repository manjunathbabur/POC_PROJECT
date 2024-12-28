import argparse
from snowflake_operations import SnowflakeOperations
from config import SNOWFLAKE_CONFIG

def execute_sql(sql_file):
    snowflake_ops = SnowflakeOperations(
        SNOWFLAKE_CONFIG['user'],
        SNOWFLAKE_CONFIG['password'],
        SNOWFLAKE_CONFIG['account'],
        SNOWFLAKE_CONFIG['database'],
        SNOWFLAKE_CONFIG['warehouse']
    )
    try:
        snowflake_ops.execute_sql_file(sql_file)
    finally:
        snowflake_ops.close_connection()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Execute modules")
    parser.add_argument('--sql_file', help="Path to SQL file to execute")
    args = parser.parse_args()

    if args.sql_file:
        execute_sql(args.sql_file)
    else:
        print("No SQL file provided. Running default logic.")
