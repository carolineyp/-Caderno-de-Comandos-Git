🔽 Como clonar o projeto do GitHub para sua máquina

No GitHub, entre no repositório que você quer copiar.

Clique no botão verde Code e copie o link HTTPS (vai ser algo como https://github.com/usuario/repositorio.git).

Abra o VS Code e depois o Terminal (Ctrl + ' ou Ctrl + J).

No terminal, vá até a pasta onde quer salvar o projeto e rode:

git clone https://github.com/usuario/repositorio.git


Isso vai baixar o projeto para a sua máquina.

Entre na pasta do projeto:

cd repositorio


Abra no VS Code:

code .

📝 Como salvar suas alterações no GitHub

Sempre que você modificar algo no código:

Veja o status dos arquivos alterados:

git status


Adicione as mudanças:

git add .


Faça o commit (salvar as mudanças localmente):

git commit -m "Descrição do que mudou"


Envie para o GitHub:

git push origin main


⚠️ Obs: em alguns casos o branch pode se chamar master ao invés de main. Se der erro, tente:

git push origin master

🔄 Antes de atualizar o GitHub (muito importante!)

Sempre que for começar a mexer no código, rode:

git pull origin main


Isso garante que você está com a versão mais recente e evita conflito.