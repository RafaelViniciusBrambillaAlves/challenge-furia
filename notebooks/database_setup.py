from db_utils import create_connection, execute_query

def setup_database(host="postgres", port="5432", user="admin", password="admin"):
    """Cria banco de dados e tabelas necessárias"""
  
    try:
        print("Verificando banco de dados...")
        conn = create_connection(dbname="postgres", user=user, password=password, host=host, port=port)
        
        if not conn:
            print("Falha na conexão com o PostgreSQL")
            return False

        conn.autocommit = True 

        with conn.cursor() as cursor:
            cursor.execute('''
                SELECT 1 FROM pg_catalog.pg_database 
                WHERE datname = 'user-data'
            ''')
            exists = cursor.fetchone()
            
            if not exists:
                print("Criando banco de dados...")
                conn.autocommit = True  # Necessário para criar databases
                cursor.execute('CREATE DATABASE "user-data"')
                print("Banco 'user-data' criado")

        conn.close()

    except Exception as e:
        print(f"Erro na criação do banco: {str(e)}")
        return False
    try:
        print("\nCriando tabelas...")
        conn = create_connection(dbname="user-data", user=user, password=password, host=host, port=port)
        
        if not conn:
            print("Falha na conexão com o user-data")
            return False

        tables = {
            'Usuarios': '''
                CREATE TABLE IF NOT EXISTS Usuarios (
                    id_usuario SERIAL PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    cpf VARCHAR(14) UNIQUE,
                    email VARCHAR(255) NOT NULL,
                    telefone VARCHAR(20),
                    genero VARCHAR(20),
                    profissao VARCHAR(30),
                    data_nascimento DATE, 
                    jogos_favoritos TEXT,
                    times_favoritos TEXT,
                    eventos_participados TEXT,
                    compras_esports TEXT,
                    frequencia_esports TEXT, 
                    produtos_desejados TEXT,
                    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );''',
                
            'Redes_Sociais': '''
                CREATE TABLE IF NOT EXISTS Redes_Sociais (
                    id_rede_social SERIAL PRIMARY KEY,
                    id_usuario INTEGER REFERENCES Usuarios(id_usuario),
                    nome_rede VARCHAR(100) NOT NULL,
                    link_perfil TEXT NOT NULL,
                    paginas_seguidas TEXT[],
                    interacoes_recentes TEXT[],
                    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );''',
                    
            'Enderecos': '''
                CREATE TABLE IF NOT EXISTS Enderecos (
                    id SERIAL PRIMARY KEY,
                    id_usuario INT REFERENCES Usuarios(id_usuario),
                    rua VARCHAR(255) NOT NULL,
                    numero VARCHAR(10) NOT NULL,
                    bairro VARCHAR(100),
                    cidade VARCHAR(100) NOT NULL,
                    estado VARCHAR(50) NOT NULL,
                    cep VARCHAR(10) NOT NULL,
                    pais VARCHAR(100) NOT NULL,
                    complemento VARCHAR(255)
                );'''
        }

        for name, query in tables.items():
            execute_query(conn, query)
            print(f"Tabela {name} criada/verificada")

        conn.close()
        print("\nSetup completo!")
        return True

    except Exception as e:
        print(f"Erro na criação das tabelas: {str(e)}")
        return False