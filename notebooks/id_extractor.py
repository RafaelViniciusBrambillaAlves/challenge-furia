import pytesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

import cv2
import re
import numpy as np
import base64

def extract_id_data_from_base64(base64_image: str):
    try:
        if not base64_image:
            return {"erro": "Imagem não fornecida."}

        image_bytes = base64.b64decode(base64_image)
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img is None:
            return {"erro": "Imagem inválida."}

        # Pré-processamento
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (9, 9), 10.0)
        sharp = cv2.addWeighted(gray, 1.5, blurred, -0.5, 0)
        _, thresh = cv2.threshold(sharp, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        kernel = np.ones((1, 1), np.uint8)
        dilated = cv2.dilate(thresh, kernel, iterations=1)

        # OCR
        config = r'--oem 3 --psm 4 -l por+eng'
        text = pytesseract.image_to_string(dilated, config=config)
        lines = [line.strip() for line in text.split('\n') if line.strip()]

        dados = {
            'nome': None,
            'cpf': None,
            'nascimento': None
        }

        name_pattern = r'^([A-ZÀ-Ü][a-zà-ü]{2,}(?:\s+[A-ZÀ-Ü][a-zà-ü]{2,}){1,4})$'

        for i, line in enumerate(lines):
            if any(k in line.lower() for k in ['nome', 'name']) and i + 1 < len(lines):
                candidate = lines[i + 1].strip()
                if re.match(name_pattern, candidate):
                    dados['nome'] = candidate
                    break

        if not dados['nome']:
            for line in lines:
                if re.match(name_pattern, line):
                    dados['nome'] = line
                    break

        cpf_regex = r'\b(\d{3}[\.\-]?\d{3}[\.\-]?\d{3}[\-]?\d{2})\b'
        cpf_matches = re.findall(cpf_regex, text)
        if cpf_matches:
            cpf = re.sub(r'\D', '', cpf_matches[0])
            if len(cpf) == 11:
                dados['cpf'] = cpf

        date_regex = r'\b(\d{2}[\/\-\.]\d{2}[\/\-\.](\d{4}))\b'
        for match in re.finditer(date_regex, text):
            day, month, year = re.split(r'\D', match.group(1))
            if 1900 <= int(year) <= 2023:
                dados['nascimento'] = f"{day.zfill(2)}/{month.zfill(2)}/{year}"
                break
        
        return dados

    except Exception as e:
        return {"erro": f"Erro na extração: {str(e)}"}

