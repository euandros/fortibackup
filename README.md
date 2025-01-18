
# FortiBackup - Script de Automação para Backup de Firewalls Fortigate

![Segmento](https://img.shields.io/badge/Segmento_:-Segurança_da_Informação-blue?style=flat-square) 
![Fase](https://img.shields.io/badge/Fase_:-Estável-green?style=flat-square) 
![Tecnologias](https://img.shields.io/badge/Tecnologias_:-Fortigate,_Python,_FortiOS_API-yellow?style=flat-square) 
![Versão](https://img.shields.io/badge/versão_:-1.0-darkyellow?style=flat-square)

Este script em Python realiza o backup automatizado das configurações de um ou mais dispositivos FortiGate, utilizando a API do FortiOS para obter o arquivo de configuração e salvá-lo localmente em servidor. O script lê as configurações de múltiplos dispositivos a partir de um arquivo de texto, realiza a autenticação via bearer token e efetua o download do backup no formato .conf.

## Funcionalidades

* Conexão com dispositivos FortiGate via API REST.
* Download automatizado do backup das configurações dos dispositivos FortiGate.
* Suporte para múltiplos dispositivos, cujas configurações são lidas de um arquivo de texto.
* Armazenamento dos backups com nomeação única baseada no dispositivo e no timestamp atual.

## Requisitos

* Python 3.x
* Biblioteca requests (pode ser instalada com pip install requests)
* Acesso à API do FortiGate e um token de autenticação (API Token)

## Estrutura do Código

### Função realizar_backup

Esta função realiza a solicitação HTTP à API do FortiGate para obter o backup do dispositivo especificado.

#### Parâmetros:
* fortigate: Endereço ou hostname do dispositivo FortiGate.
* api_token: Token da API para autenticação.
* porta: Porta de conexão da API (geralmente 443).

#### Fluxo:
1. Monta a URL da API para o backup.
2. Define os cabeçalhos da requisição, incluindo o token de autenticação.
3. Envia uma requisição GET para baixar o arquivo de configuração.
4. Se o download for bem-sucedido, salva o backup localmente com um nome que inclui o timestamp.
5. Em caso de erro, exibe o código e a mensagem da resposta.

### Função ler_arquivo_configuracoes
Lê o arquivo de texto que contém as configurações dos dispositivos FortiGate, e para cada linha válida, chama a função realizar_backup.

#### Parâmetros:
* arquivo_configuracoes: Nome do arquivo de texto contendo as informações dos dispositivos.

#### Estrutura do Arquivo de Configurações (fortigate_configs.txt):
Cada linha deve seguir o seguinte formato: ```fortigate = '<endereco_fortigate>' ; api_token = '<token_api>' ; porta = '<porta>'```

Exemplo: fortigate = '192.168.1.1' ; api_token = '1234567890abcdef' ; porta = '443'

Se o formato da linha não estiver correto, o script ignora e exibe uma mensagem de erro.
