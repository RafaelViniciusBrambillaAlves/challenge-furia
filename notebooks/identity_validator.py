from datetime import datetime
from validate_docbr import CPF

def validate_identity(extracted_data, form_data):
    """Valida os dados extraídos contra os dados do formulário"""
    
    errors = []
    cpf = CPF()

    # Validação do CPF
    extracted_cpf = ''.join(filter(str.isdigit, extracted_data.get('cpf', '')))
    if not extracted_cpf or len(extracted_cpf) != 11:
        errors.append("Documento inválido - CPF não encontrado")
    elif not cpf.validate(extracted_cpf):  # Validação usando a biblioteca
        errors.append("CPF inválido - Número não é válido")

    # Resto das validações
    if not extracted_data.get('nome'):
        errors.append("Documento inválido - Nome não encontrado")
            
    if not extracted_data.get('nascimento'):
        errors.append("Documento inválido - Data de Nascimento não encontrado")
    
    if extracted_data.get('nome', '').lower() != form_data['nome'].lower():
        errors.append("Nome não corresponde ao documento")

    form_cpf = ''.join(filter(str.isdigit, form_data['cpf']))
    if extracted_cpf != form_cpf:
        errors.append("CPF não corresponde ao documento")
        
    try:
        doc_date_str = extracted_data.get('nascimento', '')
        form_date_str = form_data['nascimento'].strftime('%d/%m/%Y')
        
        if doc_date_str != form_date_str:
            errors.append(f"Data de nascimento não corresponde: Documento({doc_date_str}) ≠ Formulário({form_date_str})")
            
    except AttributeError:
        errors.append("Formato de data inválido no formulário")
    except ValueError:
        errors.append("Formato de data inválido no documento")
    
    return errors