import psycopg2
from psycopg2 import sql
from psycopg2 import OperationalError

def create_connection(dbname, user, password, host="postgres", port="5432"):
    """Estabelece a conexão com o banco de dados PostgreSQL."""
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        return conn
    except OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def execute_query(conn, query, data=None):
    """Executa uma query SQL no banco de dados."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, data)
            conn.commit()
            print("Query executada com sucesso!")
    except Exception as e:
        print(f"Erro ao executar a query: {e}")
        conn.rollback()
