# interactive_form.py
import ipywidgets as widgets
from IPython.display import display, HTML, Image
from datetime import datetime
import base64
import importlib


import id_extractor
import identity_validator
import database_operations

importlib.reload(id_extractor)
importlib.reload(identity_validator)
importlib.reload(database_operations)

from id_extractor import extract_id_data_from_base64
from identity_validator import validate_identity
from database_operations import save_usuario_data, save_endereco_data, save_redes_sociais_data

class SocialMediaManager:
    def __init__(self):
        self.social_rows = []
        self.container = widgets.VBox()
        self.add_button = widgets.Button(
            description="➕ Adicionar Rede Social",
            button_style='info',
            layout={'width': '200px', 'margin': '10px 0'}
        )
        self.add_button.on_click(self.add_social_row)
        self.add_social_row()

    def add_social_row(self, _=None):
        row = widgets.HBox([
            widgets.Dropdown(
                options=['Twitter/X', 'Instagram', 'TikTok', 'Outra'],
                value='Instagram',
                layout={'width': '35%'}
            ),
            widgets.Text(
                placeholder='@usuário',
                layout={'width': '60%'}
            )
        ], layout=widgets.Layout(justify_content='space-between', margin='5px 0'))
        self.social_rows.append(row)
        self.container.children = tuple(list(self.container.children) + [row])

    def get_social_data(self):
        return [
            (row.children[0].value, row.children[1].value)
            for row in self.social_rows
            if row.children[1].value
        ]

def create_furia_form():
    
    
    # Configuração de estilo otimizada
    style = {'description_width': '220px'}
    layout = widgets.Layout(width='100%', overflow='visible')
    
    # Elementos do cabeçalho
    form_title = widgets.HTML(
        value="<h1 style='color: #000000; border-bottom: 2px solid #2e6c80; padding-bottom: 10px; text-align: center;'>PESQUISA FURIOSA</h1>"
    )
    
    # Introdução
    intro_html = widgets.HTML(
        value="""<div style='text-align: center; color: #666; margin: 15px 0; font-size: 0.95em;'>
            <i>\"Sua paixão move a FURIA!\"</i><br>
            Este formulário nos ajuda a entender melhor nossa comunidade de fãs<br>
            e criar experiências mais personalizadas no mundo de esports.
        </div>"""
    )

    # Widgets com ajuste de largura
    nome = widgets.Text(description="Nome Completo:", style=style, layout=layout)
    
    # Linha de contato ajustada
    linha_contato = widgets.HBox([
        widgets.Text(description="CPF:", style=style, layout={'width': '32%'}),
        widgets.Text(description="E-mail:", style=style, layout={'width': '34%'}),
        widgets.Text(description="Telefone:", style=style, layout={'width': '34%'})
    ], layout=widgets.Layout(justify_content='space-between', width='100%'))
    
    # Linha de dados pessoais
    linha_dados = widgets.HBox([
        widgets.Dropdown(
            options=['Masculino', 'Feminino', 'Outro', 'Prefiro não informar'],
            description="Gênero:",
            style=style,
            layout={'width': '30%'}
        ),
        widgets.DatePicker(
            description="Data Nasc.:",
            style=style,
            layout={'width': '30%'}
        ),
        widgets.Text(
            description="Profissão:", 
            style=style,
            layout={'width': '40%'}
        )
    ], layout=widgets.Layout(justify_content='space-between'))

    # Seção de Endereço
    endereco_label = widgets.HTML(value="<h3 style='margin: 20px 0 10px 0; color: #000000;'>Endereço Completo</h3>")
    
    endereco_fields = [
        widgets.HBox([
            widgets.Text(description="Rua:", style=style, layout={'width': '70%'}),
            widgets.Text(description="Número:", style=style, layout={'width': '25%'})
        ], layout=widgets.Layout(justify_content='space-between')),
        
        widgets.HBox([
            widgets.Text(description="Bairro:", style=style, layout={'width': '48%'}),
            widgets.Text(description="Cidade:", style=style, layout={'width': '48%'})
        ], layout=widgets.Layout(justify_content='space-between')),
        
        widgets.HBox([
            widgets.Dropdown(
                options=['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS',
                         'MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO'],
                description="Estado:",
                style=style,
                layout={'width': '30%'}
            ),
            widgets.Text(description="CEP:", style=style, layout={'width': '30%'}),
            widgets.Text(description="País:", value="Brasil", style=style, layout={'width': '35%'})
        ], layout=widgets.Layout(justify_content='space-between')),
        
        widgets.Text(description="Complemento:", style=style, layout=layout)
    ]

    # Seção de Esports ajustada
    jogos_label = widgets.HTML(
        value="<h3 style='margin: 20px 0 10px 0; color: #000000;'>Preferências de Esports</h3>"
    )
    
    jogos_opcoes = widgets.HBox([
        widgets.Checkbox(description=game, indent=False, layout={'width': '18%'}) 
        for game in ['LOL', 'CS', 'VALORANT', 'ROCKET LEAGUE', 'FF']
    ] + [widgets.Text(placeholder='Outro', layout={'width': '20%'})],
    layout=widgets.Layout(justify_content='space-between', flex_wrap='wrap'))

    times_favoritos = widgets.Text(
        description="Outros times que torce:",  # Label mais curto
        style=style, 
        layout=layout
    )

    # Demais seções ajustadas
    compras_esports = widgets.RadioButtons(
        options=['Sim', 'Não'],
        description='Comprou produtos de esports?',
        style=style,
        layout=layout
    )
    
    frequencia_label = widgets.HTML(
        value="<h4 style='margin: 10px 0; color: #000000;'>Frequência que assiste competições:</h4>"
    )
    
    frequencia_opcoes = widgets.ToggleButtons(
        options=['Diariamente', 'Nos fim de semana', 'Eventos Importantes', 'Não assisto'],
        layout={'width': '100%', 'flex_wrap': 'wrap'}
    )

    termos = widgets.Checkbox(
        description='Aceito compartilhar estas informações com a FURIA',
        style=style, 
        indent=False
    )
    
    eventos_participados = widgets.Text(description="Eventos participados:", style=style, layout=layout)
    produtos_desejados = widgets.Text(description="Produtos desejados:", style=style, layout=layout)
    output_history = widgets.Output(layout={'height': '400px', 'margin': '15px 0'})

    social_label = widgets.HTML(
        value="<h3 style='margin: 20px 0 10px 0; color: #000000;'>Redes Sociais</h3>"
    )
    social_manager = SocialMediaManager()
    
    #imagem
    upload_label = widgets.HTML(value="<h3 style='margin: 20px 0 10px 0; color: #000000;'>Upload de Imagem</h3>")
    
    image_upload = widgets.FileUpload(
        description='Enviar Foto',
        multiple=False,
        accept='image/*',
        style=style,
        layout={'width': '50%'}
    )
    
    btn_submit = widgets.Button(
        description="🎮 Enviar Formulário", 
        button_style='success', 
        layout={'width': '200px', 'margin': '20px 0'}
    )

    # 2. Container principal com referências corretas
    form_container = widgets.VBox([
        form_title,
        intro_html,
        nome,
        linha_contato,
        linha_dados,
        endereco_label,
        *endereco_fields,
        jogos_label,
        jogos_opcoes,
        times_favoritos,
        eventos_participados,
        compras_esports,
        frequencia_label,
        frequencia_opcoes,
        produtos_desejados,
        social_label,           
        social_manager.container,
        social_manager.add_button,
        upload_label,  
        image_upload, 
        termos,
        btn_submit,
        output_history
    ], layout=widgets.Layout(
        padding='25px',
        width='98%',
        margin='0 auto',
        border='2px solid #2e6c80',
        border_radius='5px'
    ))

    # 3. Função de submissão corrigida
    def on_submit(b):
        with output_history:
            output_history.clear_output()
            
            if not termos.value:
                print("❌ Você precisa aceitar os termos para continuar!")
                return

            validation_message = widgets.HTML()
            if image_upload.value:
                try:
                    uploaded_file = image_upload.value[0]
                    image_data = base64.b64encode(uploaded_file['content']).decode()
                    
                    # Extrai dados do documento
                    dados_extraidos = extract_id_data_from_base64(image_data)
                    
                    # Prepara dados para validação
                    form_data = {
                        'nome': nome.value,
                        'cpf': linha_contato.children[0].value,
                        'nascimento': linha_dados.children[1].value
                    }

                    print(dados_extraidos, form_data)
                    # Executa validação
                    errors = validate_identity(dados_extraidos, form_data)
                    
                    if errors:
                        error_html = "<div style='color: #dc3545; margin: 10px 0; padding: 10px; border: 1px solid #dc3545; border-radius: 5px;'>"
                        error_html += "<strong>❌ Validação de Identidade Falhou:</strong><ul>"
                        for error in errors:
                            error_html += f"<li>{error}</li>"
                        error_html += "</ul></div>"
                        validation_message.value = error_html
                        display(validation_message)
                        return
                    
                except Exception as e:
                    print(f"❌ Erro na validação do documento: {str(e)}")
                    return
            else:
                print("❌ Por favor, envie uma imagem do documento para validação")
                return
            
            imagem = None
            if image_upload.value:
                uploaded_file = image_upload.value[0]
                imagem = base64.b64encode(uploaded_file['content']).decode()

            usuario_data = {
                'nome': nome.value,
                'cpf': linha_contato.children[0].value,
                'email': linha_contato.children[1].value,
                'telefone': linha_contato.children[2].value,
                'genero': linha_dados.children[0].value,
                'profissao': linha_dados.children[2].value,
                'data_nascimento': linha_dados.children[1].value,
                'jogos_favoritos': [game.description for game in jogos_opcoes.children[:-1] if game.value],
                'times_favoritos': times_favoritos.value,
                'eventos_participados': eventos_participados.value, # ", ".join(eventos_participados.value)
                'compras_esports': compras_esports.value,
                'frequencia_esports': frequencia_opcoes.value,
                'produtos_desejados': produtos_desejados.value,
            }
    
            endereco_data = {
                'rua': endereco_fields[0].children[0].value,
                'numero': endereco_fields[0].children[1].value,
                'bairro': endereco_fields[1].children[0].value,
                'cidade': endereco_fields[1].children[1].value,
                'estado': endereco_fields[2].children[0].value,
                'cep': endereco_fields[2].children[1].value,
                'pais': endereco_fields[2].children[2].value,
                'complemento': endereco_fields[3].value
            }
    
            redes_data = social_manager.get_social_data()

            try:
                # Salvar dados transacionalmente
                user_id = save_usuario_data(usuario_data)
                if user_id:
                    save_endereco_data(user_id, endereco_data)
                    save_redes_sociais_data(user_id, redes_data)
                    print("✅ Dados salvos no banco com sucesso!")
                else:
                    print("❌ Falha ao salvar dados do usuário")
    
            except Exception as e:
                print(f"❌ Erro crítico ao salvar dados: {str(e)}")
            
            # Coletar dados de forma estruturada com tratamento de valores vazios
            dados = {
                "Nome": nome.value or "Não informado",
                "CPF": linha_contato.children[0].value or "Não informado",
                "E-mail": linha_contato.children[1].value or "Não informado",
                "Telefone": linha_contato.children[2].value or "Não informado",
                "Gênero": linha_dados.children[0].value or "Não informado",
                "Data Nascimento": str(linha_dados.children[1].value) if linha_dados.children[1].value else "Não informada",
                "Profissão": linha_dados.children[2].value or "Não informada",
                "Endereço": f"{endereco_fields[0].children[0].value or 'Sem rua'}, {endereco_fields[0].children[1].value or 'S/N'}",
                "Bairro": endereco_fields[1].children[0].value or "Não informado",
                "Cidade": endereco_fields[1].children[1].value or "Não informada",
                "Estado": endereco_fields[2].children[0].value or "Não informado",
                "CEP": endereco_fields[2].children[1].value or "Não informado",
                "País": endereco_fields[2].children[2].value or "Não informado",
                "Complemento": endereco_fields[3].value or "Nenhum",
                "Jogos Favoritos": ', '.join(filter(None, [
                    game.description for game in jogos_opcoes.children[:-1] if game.value] +
                    ([f"Outro: {jogos_opcoes.children[-1].value}"] if jogos_opcoes.children[-1].value else [])
                )) or "Nenhum jogo selecionado",
                "Times que Torce": times_favoritos.value or "Nenhum outro time",
                "Eventos Participados": eventos_participados.value or "Nenhum evento",
                "Comprou Produtos": compras_esports.value or "Não informado",
                "Frequência": frequencia_opcoes.value or "Não informada",
                "Produtos Desejados": produtos_desejados.value or "Nenhum",
                "Redes Sociais": ', '.join([f"{rs[0]}: {rs[1]}" for rs in redes_data]) if redes_data else "Nenhuma rede social informada",
                "Imagem": "Enviada com sucesso..." if imagem else "Nenhuma imagem enviada"
            }
    
            # Imprimir lista completa
            print("✅ Dados coletados com sucesso!\n")
            print("="*40 + "\n📋 RELATÓRIO COMPLETO\n" + "="*40)
            for key, value in dados.items():
                print(f"• {key}: {value}")
            print("\n" + "="*40)
    
            if imagem:
                display(HTML(f'<img src="data:image/png;base64,{imagem}" style="max-width: 300px; margin-top: 15px;">'))
            
            print("\n" + "="*40)

            # Resetar campos
            fields_to_reset = [
                nome, linha_contato.children[0], linha_contato.children[1], linha_contato.children[2],
                linha_dados.children[2], endereco_fields[0].children[0], endereco_fields[0].children[1],
                endereco_fields[1].children[0], endereco_fields[1].children[1], endereco_fields[2].children[1],
                endereco_fields[3], times_favoritos, eventos_participados, produtos_desejados
            ]
            
            for field in fields_to_reset:
                field.value = ''
            
            linha_dados.children[0].value = linha_dados.children[0].options[0]
            endereco_fields[2].children[0].value = None
            endereco_fields[2].children[2].value = "Brasil"
            for checkbox in jogos_opcoes.children[:-1]:
                checkbox.value = False
            jogos_opcoes.children[-1].value = ''
            compras_esports.value = None
            frequencia_opcoes.value = None
            termos.value = False

            image_upload.value = []
            image_upload._counter = 0

    # 4. Conectar o botão corretamente
    btn_submit.on_click(on_submit)
    
    return form_container