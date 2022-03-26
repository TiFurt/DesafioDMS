# DesafioDMS


## Introdução

Olá boa tarde, me chamo Tiago e vou guia-los pelos apps.

Para começar existem 2 apps referente aos exercícios solicitados, sendo assim a pasta exercicio01 se refere ao exercicio 1 
e a pasta exercicio02 se refere ao exercicio 2.

Em seguida abra o navegador da sua preferência e digite: http://127.0.0.1:8000/v1/api/.
Nessa área existe um formulario para preenchimento.

## Buscando IP

Para fazer a busca do IP desejado digite no campo 'Query' o IP respeitando todos os pontos e sem acrescentar espaços em qualquer parte.
Após isso só clicar em post que o seu IP será armazenado no banco de dados

OBS.: Caso queira buscar o seu próprio IP digite: ?fields=61439

Agora para ter acesso às informações do IP inserido entre em: http://127.0.0.1:8000/v1/location/.
Neste aba clique em post, e então as informações de localização vão aparecer listadas e serão armazenadas no banco de dados.

OBS.: A pagina http://127.0.0.1:8000/v1/location/ só funciona caso tenha um IP previamente cadastrado
## Excluindo IP ou localizações

Caso deseje excluir um IP inserido ou as informações de localização é simples, basta digitar ao final das urls o ‘id’ do ‘item’ que deseja excluir.
Após isso só clicar em Delete e confirmar, que o campo será apagado

Exemplo: http://127.0.0.1:8000/v1/api/1/ ou http://127.0.0.1:8000/v1/location/1/

## Analisando dados

Todos os dados além de estarem armazenados no banco de dados ficam disponíveis para visualização nas páginas já citadas a cima, nela é
possivel ver os campos e as suas iformações.





 
