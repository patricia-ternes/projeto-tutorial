# projeto-tutorial
Aprendendo a utilizar o Git e o Github

1 - fazer clone do projeto no computador pessoal
		* no site do github: clicar em clonar --> copiar link
		* no terminal --> acessar a pasta do github --> $ git clone colar_link

2 - Realizar as mudancas desejadas nesse projeto. Adicionar ou modificar os codigos e pastas.

3 - Adicionar as mudancas no git.
		* no terminal --> entrar na pasta do projeto --> $ git add .
														 $ git commit -m "alguma msg sinalizando a alteracao"
4 - Adicionar as mudancas no GitHub
		* no terminal --> entrar na pasta do projeto --> $ git push
		* Digitar usuario/login do GitHub


No processo acima as mudancas foram realizadas no branch "master". O ideal eh realizar as mudancas em outros branchs.

5 - Para criar um branch no Git (pc):
		* git checkout -b nomeBrach

6 - Para subir o branch pro GitHub:
		* repetir passos 2 e 3
		* no terminal --> entrar na pasta do projeto --> $ git push origin nomeBrach

7 - Outros comandos do branch - Git:
		* Para listar branchs existente no Git: $ git branch -a
		* Para trocar de branch (existentes): $ git checkout nomeBrach
		* Para deletar um branch: $ git branch -d nomeBrach