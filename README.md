# 💬 Secure Messenger - Aplicação Web Segura

Aplicação Flask com criptografia simétrica (AES) e proteção contra ataques CSRF.

---

## 🚀 Como Rodar o Projeto

1. 📁 Clone o repositório ou copie os arquivos para uma pasta local.
2. 🐍 Crie um ambiente virtual (recomendado):

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. 📦 Instale as dependências:

```bash
pip install flask flask-wtf cryptography
```

4. ▶️ Execute a aplicação:

```bash
python app.py
```

5. 🌐 Acesse no navegador:

http://127.0.0.1:5000

---

## 🔐 Funcionalidades de Segurança

✅ Criptografia AES (simétrica) com chave e IV para proteger mensagens.  
✅ Mitigação contra CSRF via Flask-WTF e tokens automáticos nos formulários.  
✅ Mensagens criptografadas armazenadas apenas em memória e descriptografadas para exibição.

---

## 🧪 Como Testar

- ✍️ Envie mensagens pela interface.
- 🔒 Veja a mensagem criptografada sendo exibida como texto embaralhado.
- 🔁 Envie a mesma mensagem mais de uma vez — a criptografia será diferente (uso de IV aleatório).
- 🛡️ Remova o token CSRF do formulário (via ferramentas como Postman) e veja que a aplicação retorna:

```http
400 Bad Request  
The CSRF token is missing.
```

---

## 🛠️ Escolhas de Design

- AES em modo CBC com padding manual e IV aleatório garante confidencialidade.
- Tokens CSRF embutidos automaticamente nos formulários impedem falsificação de requisições.
- Interface minimalista em HTML e CSS (sem bibliotecas externas) foca em funcionalidade.
- Mensagens armazenadas em memória por simplicidade.

---

## 🧪 Teste de Proteção contra CSRF

A aplicação usa tokens CSRF integrados com Flask-WTF. Para comprovar sua eficácia:

1. O usuário acessa normalmente a interface (token é incluído automaticamente).
2. Um ataque CSRF foi simulado com Postman ou inspeção manual do HTML.
3. Resultado: requisição sem token foi bloqueada com o erro 400.

✅ Isso confirma que a proteção CSRF está funcionando corretamente.

---

## 📸 Capturas de Tela

https://github.com/KalledAbdala/AVALIA-O-CIBERSEGURAN-A/blob/main/secure_messenger/prints/Captura%20de%20tela%202025-05-09%20205031.png

https://github.com/KalledAbdala/AVALIA-O-CIBERSEGURAN-A/blob/main/secure_messenger/prints/Captura%20de%20tela%202025-05-09%20205229.png

https://github.com/KalledAbdala/AVALIA-O-CIBERSEGURAN-A/blob/main/secure_messenger/prints/Captura%20de%20tela%202025-05-09%20205301.png


---

✍️ Desenvolvido por Kalled — Projeto de Segurança em Aplicações Web.
