
from crypto_utils import encrypt_message, decrypt_message
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)

# Configuração de segurança da chave secreta
app.secret_key = os.urandom(24)

# Inicializa a proteção CSRF
csrf = CSRFProtect(app)

# Funções de criptografia e descriptografia
def encrypt_message(message):
    return message[::-1]  # Exemplo de criptografia simples

def decrypt_message(encrypted_message):
    return encrypted_message[::-1]  # Exemplo de descriptografia simples

# Classe do formulário de mensagens
class MessageForm(FlaskForm):
    message = StringField("Mensagem", validators=[DataRequired()])

# Lista para armazenar as mensagens
messages = []

@app.route("/", methods=["GET", "POST"])
def index():
    form = MessageForm()
    global messages
    if form.validate_on_submit():
        raw_message = form.message.data
        encrypted = encrypt_message(raw_message)
        decrypted = decrypt_message(encrypted)
        messages.append({"encrypted": encrypted, "decrypted": decrypted})
        return redirect("/")
    return render_template("index.html", form=form, messages=messages)

if __name__ == "__main__":
    app.run(debug=True)
