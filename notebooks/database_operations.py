from datetime import datetime
from db_utils import create_connection
import psycopg2

def save_usuario_data(usuario_data):
    """Salva os dados principais do usuário na tabela Usuarios"""
    conn = None
    try:
        conn = create_connection(dbname="user-data", user="admin", password="admin", host="postgres", port="5432")
        with conn.cursor() as cursor:
            usuario_query = """
                INSERT INTO Usuarios (
                    nome, cpf, email, telefone, genero, profissao, data_nascimento,
                    jogos_favoritos, times_favoritos, eventos_participados,
                    compras_esports, frequencia_esports, produtos_desejados
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s,
                    %s, %s,
                    %s
                ) RETURNING id_usuario;
            """
            jogos = ', '.join(usuario_data.get('jogos_favoritos', []))
            times = usuario_data.get('times_favoritos', '')
            eventos = usuario_data.get('eventos_participados', '')
            produtos = usuario_data.get('produtos_desejados', '')

            compras = usuario_data.get('compras_esports')
            frequencia = usuario_data.get('frequencia_esports')
            
            cursor.execute(usuario_query, (
                usuario_data['nome'],
                usuario_data['cpf'],
                usuario_data['email'],
                usuario_data['telefone'],
                usuario_data['genero'],
                usuario_data['profissao'],
                usuario_data['data_nascimento'],
                jogos,          
                times,          
                eventos,        
                usuario_data.get('compras_esports', ''),
                usuario_data.get('frequencia_esports', ''),
                produtos       
            ))

            print()
            
            user_id = cursor.fetchone()[0]
            conn.commit()
            return user_id
            
    except psycopg2.Error as e:
        print(f"Erro ao salvar usuário: {e}")
        if conn:
            conn.rollback()
        return None
    finally:
        if conn:
            conn.close()

def save_endereco_data(user_id, endereco_data):
    """Salva os dados de endereço do usuário"""
    conn = None
    try:
        conn = create_connection(dbname="user-data", user="admin", password="admin", host="postgres", port="5432")
        with conn.cursor() as cursor:
            endereco_query = """
                INSERT INTO Enderecos (
                    id_usuario, rua, numero, bairro, cidade, estado, cep, pais, complemento
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            
            cursor.execute(endereco_query, (
                user_id,
                endereco_data['rua'],
                endereco_data['numero'],
                endereco_data['bairro'],
                endereco_data['cidade'],
                endereco_data['estado'],
                endereco_data['cep'],
                endereco_data['pais'],
                endereco_data['complemento']
            ))
            
            conn.commit()
            return True
            
    except psycopg2.Error as e:
        print(f"Erro ao salvar endereço: {e}")
        if conn:
            conn.rollback()
        return False
    finally:
        if conn:
            conn.close()

def save_redes_sociais_data(user_id, redes_data):
    """Salva os dados de redes sociais do usuário"""
    conn = None
    try:
        conn = create_connection(dbname="user-data", user="admin", password="admin", host="postgres", port="5432")
        with conn.cursor() as cursor:
            rede_query = """
                INSERT INTO Redes_Sociais (
                    id_usuario, nome_rede, link_perfil
                ) VALUES (%s, %s, %s);
            """
            
            for rede in redes_data:
                cursor.execute(rede_query, (
                    user_id,
                    rede[0],
                    rede[1]
                ))
            
            conn.commit()
            return True
            
    except psycopg2.Error as e:
        print(f"Erro ao salvar redes sociais: {e}")
        if conn:
            conn.rollback()
        return False
    finally:
        if conn:
            conn.close()