# Como Rodar o Projeto

## Clone o repositório ou copie os arquivos para uma pasta local.
## Crie um ambiente virtual (recomendado):

python -m venv venv
source venv/bin/activate  # No Linux/Mac
venv\Scripts\activate     # No Windows

## Instale as dependências:

pip install flask flask-wtf cryptography

## Execute a aplicação:

python app.py

## Acesse no navegador:

http://127.0.0.1:5000

# Funcionalidades de Segurança

✅ Criptografia AES (simétrica) usando chave e IV para proteger mensagens.

✅ Mitigação contra CSRF via Flask-WTF e tokens automáticos nos formulários.

✅ Mensagens criptografadas armazenadas em memória e descriptografadas apenas para exibição.

# Como Testar

Envie mensagens pela interface da aplicação.

Veja que a mensagem criptografada aparece como texto embaralhado.

Teste uma mesma mensagem duas vezes e veja que os resultados criptografados são diferentes (isso comprova o uso de IV).

Faça um teste manual de CSRF (ou com plugin do navegador) para ver que a aplicação recusa envios sem token.

# Escolhas de Design

AES em modo CBC com padding manual e IV aleatório garante confidencialidade.

Tokens CSRF embutidos no formulário impedem ataques de falsificação de requisições.

Interface simples com HTML e CSS focada na funcionalidade.

Armazenamento das mensagens em memória (não persistente) por simplicidade.

# Teste de Proteção contra CSRF

A aplicação utiliza o mecanismo de tokens CSRF integrado ao Flask-WTF. Para verificar se a proteção funciona corretamente, foi realizado o seguinte teste:

O usuário acessou o formulário normalmente pela interface web, onde o token CSRF é automaticamente incluído.

Em seguida, foi simulado um ataque CSRF utilizando uma ferramenta como o Postman ou inspecionando o HTML e removendo o token do formulário.

Resultado: ao enviar uma requisição POST sem o token CSRF, o servidor retorna a resposta:

400 Bad Request
The CSRF token is missing.

Isso comprova que a proteção contra CSRF está ativa e funcionando corretamente.

# Prints adicionais