import snowflake.connector

class SnowflakeOperations:
    def __init__(self, user, password, account, database, warehouse):
        self.conn = snowflake.connector.connect(
            user=user,
            password=password,
            account=account
        )
        self.conn.cursor().execute(f"USE DATABASE {database}")
        self.conn.cursor().execute(f"USE WAREHOUSE {warehouse}")

    def execute_sql_file(self, sql_file):
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        self.conn.cursor().execute(sql_script)
        print(f"Executed SQL from {sql_file}")

    def close_connection(self):
        self.conn.close()
