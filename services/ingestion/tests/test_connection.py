from energy_ingestion.database.connection import get_connection

def test_database_connection():
    with get_connection() as connection:
         with connection.cursor() as cursor:
            cursor.execute("SELECT current_database();")
            result = cursor.fetchone()

            assert result[0] == "energy_db"