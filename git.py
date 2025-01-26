"""
Oq é controle de versão: é um grupo de sistemas e processos para gerenciar alterções feita em documentos, programas e diretorios
O controle de versão é util para qualquer coisa que mude ao longo do tempo ou precise ser compartilhada, como codigos e dados.
O controle de versão nos permite rastrear arquivos em diferentes estados, combinar.
versões diferente, indentificar uma versão especifica de um arquivo, e revertes alterações.
Git armazena tudo, então nada é perdido, ele nos permite comparar o conteudo de arquivos em momentos diferentes
podemos examinar quais mudanças foram feitas, quem as fez e quando
o mais importante é que, se nosso softeware tiver problemas, podemos reverter para uma versão anterios que funciona corretamente 
Usar o git no shell:

pwd : imprime o diretorio de trabalho atual

ls : para ver oq ha em nosso diretorio atual

git --version : checando versão git

Um repositorio é um diretorio que consiste em duas partes: a primeira são os arquivos e subdiretorios que criamos e editamos 

git init nome_do_arquivo : para criar um novo repositorio git

git status : podemos verificar se o repositorio foi inicializado corretamente 

cd caminho(pasta): acessa a pasta

git add nome do arquivo : adiciona o arquivo para a area de preparação

git add . : adiciona todos os arquivos do diretorio atual 

git commit -m(mensagem) "Mensagem de alteração(ex: adiciona a linha de input)" : é usado para criar um instantâneo das alterações preparadas em um cronograma de um histórico de projetos do Git

Estrutura do commit :

1.Commit 
    - O commit contem metadados como autor, mensagem de log e hora do commit

2.Arvore
    - A arvore rastreia os nomes e locais dos arquivos e direorios quando a confirmação ocorreu
    - Pense nisso como um dicionario, com chaves representadas como identificadores exclusivos, mapeadas para arquivos ou diretorios 

3.Bolha 
    - para cada arquivo na arvore, ha um blob, que significa objeto binario grande.
    - Um blob pode conter dados de qualquer tipo.
    - Os blobs contem um instantaneo compactado de conteudo do arquivos quando a confirmação ocorreu
    
git hash

esta é um seguencia de 40 caracteres de numeros e letras como esta

-m Last commit: b22eb75a82a68b9c0f1c45b9f5a9b7abe281683a

é chamado de hash porque o git o produz usando um geradore de numero pseudoaleatorio chamado função hash

Os hashes permitem que o git compatilhe os dados de forma eficiente entre reposiorios 
 - se os dois arquivos forem iguais, seus hashes serao os mesmos

Portanto, o git pode dizer quais informaçoes precisam ser salvas 

git log - podemos vizualizar informações de commit usando exibindo todos os commits, feitas no repositorio em ordem reversa, começando com os commit mais recente

personalizar o git log :

git log -3 : mostra apenas os 3 commits mais recentes
 
git log arquivo.py : verifica apenas o histotico do arquivo 

git log -2 arquivo.py : combinar os dois 

git log --since-- "Apr 2 2024": verificar o log por data

git log --since="Apr 2 2024" --until="Apr 11 2024" - verifica os logs entre o intervalo de duas datas 

Natural data: 

"2 weeks ago"

Data format:

"07-15-2024"

git diff: é como o git nos mostra a diferança entre versões 

git diff arquivo.py: mostra oq foi feito nas versoes do codigo e oq foi alterado

git diff --staged: indica que queremos olha para uma revisão especifica do arquivo

git diff hash hash: comparar commits

git diff HEAD~1 HEAD: compara o commit mais antigo com o mais atual

git revert: restaura todos os arquivos atualizados no commit , precisamos fornecer uma referencia, por meio de um hash de confirmação ou HEAD, as alterações que queremos desfazer,
referenciar o HEAD significa desfazer as alterações feitas no ultimos commit 

git revert --no-edit HEAD: evita que o editor de texto abra quando revertermos

git revert -n HEAD: reverte sem fazer commit, permitindo revisar e modificar o codigo, 

git checkout HEAD~1 -- arquivo.py:

git restore --staged arquivo.py: 

git revert HEAD
Reverte todas as alterações do último commit (indicado por HEAD) criando um novo commit para desfazer as mudanças.

git revert HEAD --no-edit
Reverte o último commit sem abrir o editor de texto para editar a mensagem do commit. Ele usa a mensagem padrão gerada automaticamente.

git revert HEAD -n
Reverte o último commit, mas não cria um novo commit automaticamente. As mudanças são aplicadas à área de preparação (staging area), permitindo revisões antes de confirmar.

git checkout HEAD~1 report.md
Recupera o estado do arquivo report.md do penúltimo commit (o commit antes do HEAD) sem afetar outros arquivos no repositório.

git restore --staged report.md
Remove o arquivo report.md da área de staging (desfaz o comando git add para esse arquivo).

git restore --staged
Remove todos os arquivos da área de staging, desfazendo qualquer git add feito antes do próximo commit.

BRANCHES

Branches sao como suas proprias versões de repositorios, como universos paralelos

Eles nos perimitem ter varias versões de nossos arquivos e rastrea cada versão sistematicamente

em cada remificão, alguns arquivos podem ser iguais, outros podem ser diferentes ou alguns pode não exitir

ramificações são essenciais para o desenvolvimento continuo de software 

por padrao, cada repositorio tem uma ramificação chamada main

geramente este ramo é onde armazenamos nosso aplicativo de trabalho

as ramificações sao beneficas porque permitem que varios desenvolvedores trabalhem em um projeto simultaneamente 

conteúdo entre ramificações, permitindo-nos enviar novos recursos para nosso software ativo.

git branch : verifica as branchs que tem disponivel

git switch nome : mover entre as brachs 

git branch nome: cria uma nova branch

git brach -c nome: criar branch nova e subir commit



"""