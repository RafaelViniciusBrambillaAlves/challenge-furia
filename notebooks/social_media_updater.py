import psycopg2
import random
from IPython.display import display, HTML
import time
from db_utils import create_connection, execute_query

# Função para simular API do Twitter
def mock_twitter_api(username):
    pages = ['@FURIA', '@CSGO', '@LoL_Esports', '@Gaules', '@BrasilGameShow']
    interactions = [
        f'RT: {random.choice(pages)} - {random.randint(1,24)}h atrás',
        f'Like: {random.choice(pages)} - {random.randint(1,24)}h atrás',
        f'Reply: {random.choice(pages)} - {random.randint(1,24)}h atrás'
    ]
    return pages[:3], interactions[:3]

# Função para simular API do Instagram
def mock_instagram_api(username):
    pages = ['@furia', '@csgo', '@lolesports', '@gaules', '@bgs']
    interactions = [
        f'Curtida em foto - {random.randint(1,24)}h atrás',
        f'Comentário: "{random.choice(["🔥","😍","👏"])}" - {random.randint(1,24)}h atrás',
        'Story visualizado'
    ]
    return pages[:3], interactions[:3]

# Função para simular API do TikTok
def mock_tiktok_api(username):
    pages = ['furiagg', 'csgobrasil', 'lolesportsbr', 'gaules', 'bgs']
    interactions = [
        f'Curtida em vídeo - {random.randint(1,24)}h atrás',
        f'Compartilhamento - {random.randint(1,24)}h atrás',
        'Seguiu conta sugerida'
    ]
    return pages[:3], interactions[:3]

def fetch_social_accounts():
    conn = create_connection("user-data", "admin", "admin")
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM redes_sociais")
            return cursor.fetchall()
    except Exception as e:
        print(f"Erro ao buscar contas: {e}")
        return []
    finally:
        if conn:
            conn.close()

def update_social_data(account_id, pages, interactions):
    conn = create_connection("user-data", "admin", "admin")
    try:
        with conn.cursor() as cursor:
            update_query = """
                UPDATE redes_sociais
                SET paginas_seguidas = %s,
                    interacoes_recentes = %s
                WHERE id_rede_social = %s
            """
            cursor.execute(update_query, (pages, interactions, account_id))
            conn.commit()
    except Exception as e:
        print(f"Erro ao atualizar conta {account_id}: {e}")
    finally:
        if conn:
            conn.close()

def main_social_update():
    accounts = fetch_social_accounts()
    
    if not accounts:
        display(HTML("<h3 style='color:red'>Nenhuma conta social encontrada!</h3>"))
        return
    
    display(HTML("<h3>🚀 Iniciando coleta de dados sociais:</h3>"))
    
    for account in accounts:
        acc_id, user_id, rede, perfil, paginas, interacoes, data_reg = account
        display(HTML(f"<p>📡 Processando: {rede} - {perfil}</p>"))

        has_data = (paginas not in (None, [])) or (interacoes not in (None, []))
        
        if has_data:
            display(HTML(
                f"<p style='color:#666'>⏩ Pulando {rede} - {perfil} "
                "(já possui dados)</p>"
            ))
            continue
        
        # Coleta dados mockados
        if 'Twitter' in rede:
            pages, interactions = mock_twitter_api(perfil)
        elif 'Instagram' in rede:
            pages, interactions = mock_instagram_api(perfil)
        elif 'TikTok' in rede:
            pages, interactions = mock_tiktok_api(perfil)
        else:
            display(HTML("<p style='color:orange'>⚠️ Rede social não suportada</p>"))
            continue
            
        # Atualiza banco
        update_social_data(acc_id, pages, interactions)
        
        # Mostra resultados
        display(HTML(f"""
            <div style='margin-left:20px; border-left:2px solid #ccc; padding-left:10px'>
                <p>📊 Páginas seguidas: {', '.join(pages)}</p>
                <p>💡 Interações recentes:</p>
                <ul>
                    {''.join([f'<li>{interaction}</li>' for interaction in interactions])}
                </ul>
                <p style='color:green'>✅ Atualizado com sucesso!</p>
            </div>
        """))
