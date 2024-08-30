# Script de Transferência de Arquivos com Sockets

Este script em Python permite a transferência de arquivos entre um cliente e um servidor usando sockets. O script pode ser executado tanto como um servidor quanto como um cliente, dependendo dos argumentos passados.

## Requisitos

- Python 3.x

## Instalação

Nenhuma instalação especial é necessária. Apenas certifique-se de ter o Python 3 instalado em sua máquina.

## Como Usar

### Executando o Servidor

Para iniciar o script como um servidor, utilize o argumento `--server`. Você também pode especificar o host, a porta e o diretório que deseja compartilhar:

```bash

python teste2.py --server --host <endereço_host> --port <número_porta> --dir <diretório_para_servir>
--host: O endereço IP do servidor (padrão é localhost).
--port: O número da porta em que o servidor escutará (padrão é 50000).
--dir: O diretório com os arquivos a serem servidos (padrão é o diretório atual .).

Executando o Cliente
Para rodar o script como um cliente, você deve especificar o host, a porta e o nome do arquivo que deseja obter:

bash

Copiar código
python teste2.py --host <endereço_host> --port <número_porta> --file <nome_arquivo>
--host: O endereço IP do servidor do qual o cliente obterá o arquivo (padrão é localhost).
--port: O número da porta usada pelo servidor (padrão é 50000).
--file: O nome do arquivo a ser obtido do servidor.

Exemplo
Executando o servidor:

bash

Copiar código
python teste2.py --server --dir ./arquivos
Executando o cliente para obter um arquivo:

bash
Copiar código
python teste2.py --file exemplo.txt
Contribuição
Se quiser contribuir para este projeto, sinta-se à vontade para abrir um pull request.
