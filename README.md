# projeto-tutorial
Aprendendo a utilizar o Git e o Github

1 - fazer clone do projeto no computador pessoal

		* no site do github: clicar em clonar --> copiar link
		* no terminal --> acessar a pasta do github --> $ git clone colar_link

2 - Realizar as mudancas desejadas nesse projeto. Adicionar ou modificar os codigos e pastas.

3 - Adicionar as mudancas no git.

		* no terminal --> $ git add .
		* no terminal --> $ git commit -m "alguma msg sinalizando a alteracao"
4 - Adicionar as mudancas no GitHub

		* no terminal --> $ git push
		* Digitar usuario/senha do GitHub


No processo acima as mudancas foram realizadas no branch "master". 
O ideal eh realizar as mudancas em outros branchs.

5 - Para criar um branch no Git (pc):

		* git checkout -b nomeBrach

6 - Para subir o branch pro GitHub:

		* repetir passos 2 e 3
		* no terminal --> $ git push origin nomeBrach

7 - Para fazer com que o branch fique igual ao master:

		* git checkout dev_branch
		* git reset --hard master
		* git push --force
		
		
8 - Outros comandos do branch - Git:

		* Para listar branchs existente no Git: $ git branch -a
		* Para trocar de branch (existentes) no Git: $ git checkout nomeBrach
		* Para deletar um branch no Git: $ git branch -d nomeBrach
		* Para deletar um branch no GitHub: $ git push origin :nomeBrach
		* Para sincronizar o projeto local a partir do GitHub: $ git pull

9 - Remover pastas e arquivos - Git:

		* Para remover um arquivo: $ git rm file
		* Para remover uma pasta: $ git rm -r folder
		* repetir passo 3 e 4 (ou 6)