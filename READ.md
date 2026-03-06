## 🛠️ Configuração do Ambiente Virtual (venv)

Para manter as bibliotecas do projeto (como TensorFlow e NLTK) isoladas e evitar conflitos com outras instalações do Python no computador,utilizamos um ambiente virtual.

### Como foi criado:
O ambiente foi gerado na raiz do projeto com o seguinte comando:
```bash
python -m venv chatbot

### 📦 Instalação das Dependências

Após ativar o ambiente virtual `(chatbot)`, você deve instalar as bibliotecas necessárias para que o cérebro do bot funcione.

**Como foi instalado originalmente:**
```bash
"pip install tensorflow nltk numpy".
para instalar as bibliotecas use "pip install numpy tensorflow nltk"

#lembrando que esse projeto não teve inicio comigo e sim do canal SimpleLearn, mas esta sendo melhorado e atualizado por mim.

pip install -r requirements.txt


teste de enviar mensagem para o zap "phone_number = "+5585999592853"
message = "teste bot do zap"
hours = 17
minutes = 30
pwk.sendwhatmsg_instantly(phone_number, message, hours, minutes)
print("Mensagem enviada com sucesso!")"

iniciar chatbot = python -u "c:/python projects/chatbot-novo/chatbot.py"