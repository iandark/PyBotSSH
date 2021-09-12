# PyBotSSH - Telegram
(c) IanDark

Este bot é baseado no [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI).
Portanto é altamente recomendável você utilizar as versões do Python para a lib pyTelegramBotAPI.

## Requisitos
 - Armazenamento de chave SSH no server linux a ser conectado.
 - Python 3.6 - 3.9

## Instalação
> python3 -m pip install --user pyTelegramBotAPI

## Configuração de SSH
- Gerar chave SSH:
~~~bash
$ ssh-keygen -t rsa -b 2048
~~~


- Copiar chave local para o servidor:
~~~bash
$ ssh-copy-id user@server
user@server's password:
~~~

- Caso queira verificar no servidor a chave armazenada:
~~~bash
$ cat .ssh/authorized_keys
~~~

- Para garantir que está logando no servidor de forma automática basta logar:
~~~bash
$ ssh user@server

user@server:~$
~~~
