🔽 Clonar um repositório do GitHub
git clone https://github.com/usuario/repositorio.git
cd repositorio
code .

🔄 Atualizar seu projeto antes de editar
git pull origin main   # ou master

📝 Ciclo básico de salvar alterações
git status                # Ver quais arquivos foram modificados
git add .                 # Adicionar todas as alterações
git commit -m "mensagem"  # Salvar mudanças localmente
git push origin main      # Enviar para o GitHub

📌 Comandos úteis
git log              # Ver histórico de commits
git branch           # Ver branches existentes
git checkout -b nome # Criar e mudar para uma nova branch
git checkout main    # Voltar para a branch principal

⚠️ Dicas importantes

Sempre rode git pull antes de começar a trabalhar.

Use mensagens de commit claras (ex: "Corrige bug no login").

Se der erro de branch (main vs master), verifique qual é o nome com:

git branch -a
