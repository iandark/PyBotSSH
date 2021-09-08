import os
import subprocess
import telebot
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.environ.get('API_TOKEN'))


def exec_process(args):
    if args.count('sudo') > 0:
        return 'Comando não autorizado!'
    else:
        ssh = 'ssh {user}@{server}'.format(user=os.environ.get('USER_SERVER'), server=os.environ.get('SERVER_ADDRESS'))
        ssh = ssh.split(' ')
        ssh.extend(args)
        return subprocess.check_output(ssh)


@bot.message_handler(commands=['ssh'])
def execute_ssh(message):
    args = os.environ.get('COMMAND').split(' ')
    output = exec_process(args)
    bot.reply_to(message, output)


@bot.message_handler(commands=['list'])
def return_list(message):
    f = open("tmp/loreipsum.txt", "r")
    bot.reply_to(message, f.read())


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Olá {name}!".format(name=message.from_user.first_name.split(' ')[0]) + """
Eu aceito estes comandos:

/start
/list
    """)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=['document'])
def handle_docs(message):
    bot.send_message(message.chat.id, "{name},".format(name=message.from_user.first_name).split(' ')[
        0] + " eu ainda não aceito documentos =\ ")


@bot.message_handler(content_types=['audio', 'voice'])
def handle_audio(message):
    bot.send_message(message.chat.id, "{name},".format(name=message.from_user.first_name).split(' ')[
        0] + " eu ainda não aceito áudios =\ ")


@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    sti = open('tmp/telegram.webp', 'rb')
    bot.send_sticker(chat_id=message.chat.id, data=sti)


bot.polling()
