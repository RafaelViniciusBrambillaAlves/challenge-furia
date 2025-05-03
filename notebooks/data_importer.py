import csv
from psycopg2 import sql
from db_utils import create_connection, execute_query

def import_data():
    """Importa dados de CSVs para as tabelas do PostgreSQL"""
    csv_mapping = [
        ('dados/usuarios.csv', 'usuarios'),
        ('dados/enderecos.csv', 'enderecos'),
        ('dados/redes_sociais.csv', 'redes_sociais')
    ]

    conn = create_connection(dbname="user-data", user="admin", password="admin", host="postgres", port="5432")
    
    try:
        for csv_file, table_name in csv_mapping:
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                count = 0  # Contador manual
                
                with conn.cursor() as cursor:
                    for row in reader:
                        cleaned_data = [
                            str(value).strip() if value is not None and str(value).strip() != '' else None 
                            for value in row.values()
                        ]
                        
                        # Montar query dinamicamente
                        query = sql.SQL("""
                            INSERT INTO {} ({})
                            VALUES ({})
                        """).format(
                            sql.Identifier(table_name),
                            sql.SQL(', ').join(map(sql.Identifier, row.keys())),
                            sql.SQL(', ').join([sql.Placeholder()] * len(cleaned_data))
                        ) 
                        
                        cursor.execute(query, cleaned_data)
                        count += 1  # Incrementa contador
                    
                    print(f"{count} registros inseridos em {table_name}")
                    
        conn.commit()
        
    except Exception as e:
        conn.rollback()
        print(f"Erro na importação: {str(e)}")
    finally:
        if conn and not conn.closed:
            conn.close()