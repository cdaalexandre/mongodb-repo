## 🔄 Como iniciar o projeto todo dia

```powershell
# 1. Abrir o projeto no VS Code
cd C:\repo\mongodb-repo

# 2. Ativar ambiente virtual
# Windows PowerShell
.\.venv\Scripts\activate
# Linux/Mac
# source .venv/bin/activate

# 3. Verificar interpretador no VS Code
# (Ctrl+Shift+P → Python: Select Interpreter → .venv\Scripts\python.exe)

# 4. Iniciar o MongoDB (se não estiver rodando)
# Windows
net start MongoDB
# Linux/Mac
# sudo systemctl start mongod

# 5. Conferir conexão com o banco
mongosh
show dbs
exit

# 6. Instalar dependências (se necessário)
pip install -r requirements.txt

# 7. Rodar o projeto
python main.py

# 8. Versionar com Git
git pull origin main   # antes de começar
git add .
git commit -m "mensagem clara"
git push origin main
