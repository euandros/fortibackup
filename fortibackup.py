import requests
import re
import json
from datetime import datetime

def realizar_backup(fortigate, api_token, porta):
    url = f"https://{fortigate}:{porta}/api/v2/monitor/system/config/backup?scope=global"
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Accept': 'application/json'
    }

    requests.packages.urllib3.disable_warnings()
    response = requests.get(url, headers=headers, verify=False)

    if response.status_code == 200:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"{fortigate}_backup_{timestamp}.conf"
        
        with open(backup_filename, 'wb') as backup_file:
            backup_file.write(response.content)
        print(f"Backup salvo com sucesso como '{backup_filename}'")
    else:
        print(f"Falha na requisição de backup para {fortigate}: {response.status_code} - {response.text}")

def ler_arquivo_configuracoes(arquivo_configuracoes):
    with open(arquivo_configuracoes, 'r') as file:
        for linha in file:
            match = re.match(r"fortigate = '(.*?)' ; api_token = '(.*?)' ; porta = '(.*?)'", linha.strip())
            if match:
                fortigate = match.group(1)
                api_token = match.group(2)
                porta = match.group(3)
                realizar_backup(fortigate, api_token, porta)
            else:
                print(f"Linha inválida: {linha}")

arquivo_configuracoes = 'fortigate_configs.txt'

ler_arquivo_configuracoes(arquivo_configuracoes)
