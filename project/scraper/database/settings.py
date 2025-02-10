from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    "postgres",
    user="postgres",
    password="postgres",
    host="postgres",
    port=5432,
)
