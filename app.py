from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
bot = ChatBot(
	'ChatBot',
	storage_adapter='chatterbot.storage.SQLStorageAdapter',
	logic_adapters=[
		'chatterbot.logic.BestMatch',
		'chatterbot.logic.MathematicalEvaluation',
	],
	database_uri='sqlite:///database.sqlite3'
)

def initialize():
	trainer = ChatterBotCorpusTrainer(bot)
	trainer.train('chatterbot.corpus.english')
	trainer.train('chatterbot.corpus.kazakh')

@app.route('/train')
def train():
	pass

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/bot')
def get_bot_response():
	user_input = request.args.get('msg')
	return str(bot.get_response(user_input))


if __name__ == '__main__':
	# initialize()
	# casual_conv()
	app.run()


def casual_conv():
	print ("Start the conversation...")
	while True:
		try:
			print(">", end=' ')
			bot_input = bot.get_response(input())
			print(">", end=' ')
			print(bot_input)
		except(KeyboardInterrupt, EOFError, SystemExit):
			break