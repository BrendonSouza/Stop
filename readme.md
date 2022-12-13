# STOP!

 **STOP** é um jogo multiplayer que consiste em escrever o mais rápido possível palavras  de determinadas categorias iniciadas por uma letra previamente sorteada. Quando o primeiro jogador clica em **STOP** ninguém pode escrever mais nada e o jogo passa para a fase de validação.
 Nessa Fase, o jogador vota nas palavras que ele acredita não existir / não iniciar com a letra sorteada. Após isso a rodada encerra, e somente as palavras válidas são apontadas.


# Como executar

Recomenda-se utilizar em um ambiente virtualizado a fim de evitar problemas de versionamento das dependências
```console
	python3 -m venv venv
	pip install -r requirement.txt
```

Após a instalação, é necessário abrir o arquivo src/server.py e editar o  "host" para o ip local da máquina servidor:
	"img_here"

No arquivo, src/client.py também é necessário editar o "host para o ip local da máquina servidor:
	"img_here"

Em seguida, a máquina servidor deve executar o arquivo src/server.py:
`	python3 src/server.py`

Por fim, os clientes devem executar o arquivo main.py:
`	python3 main.py`
 
# O Protocolo
As interações clientes servidores são regidas pelo protocolo implemento, na camada de aplicação, desenvolvido com base no TCP.

As mensagens enviadas é estruturada em um JSON e é composta por pelo menos 2 campos obrigatórios:
- data - Onde será enviado todo os dados 
- type - um atributo dentro do objeto **data** que indica o tipo da mensagem enviada
```json
{
	"data":{
		"type":"some_type"
	}
}
```
O corpo do objeto data, além do campo obrigatório type, pode conter outros campos que enviam informações necessárias tanto para controle do fluxo do game, quanto para processamento. Segue exemplos abaixo:

- `"type": "name_already_exists"` -> Verifica se o nome informado pelo usuário já foi cadastrado previamente e retorna True ou False
```json
{
	"data":  {
		"type":  "name_already_exists",
		"value":  True,
	}
}
```
- `"type": "send_name"` -> Envia o nome do jogador, recebe como resposta o `"type": "name_already_exists"` descrito acima.
```json

{
        
	"data":{
		"type": "send_name",
		"name": "Vrevyn"
    }
}
```
-`"type":"verify_number_of_players` -> Envia o número de jogadores conectados
```json
{

	"data": {
		"type": "verify_number_of_players",
		"number_of_players": 2,
	}
}
```
-`"type":"stop` -> Envia pro servidor um pedido para encerrar a fase de escrita das palavras, o servidor retorna o `"type": "response"` para todos os clientes conectados

```json
{
	"data":{
		"type": "stop"
	}
}
```

`"type": "response"` -> Partindo do servidor, informa ao cliente que o "stop" foi requisitado. Partindo do cliente, envia as palavras digitadas em cada categoria. Quando o servidor recebe o `"type": "response"`, retorna `"type": "validate_response"` para todos os clientes conectados

```json
{
	"data": {
		"type": "response",
		"stop": True,
		"name_request_stop": "Vrevyn",
	}
}
```

```json
{
	"data":{
		"type": "response",
		"name": "Vrevyn",
		"inputs":[
			{
				"name": "Profissão",
				"value": "Arquiteto"
			},
			{
				"name": "Cep",
				"value": "Alagoas"
			},
			{
				"name": "Animal",
				"value":"Anta"
			},
			{
				"name": "Comida",
				"value": "Almôndegas"
			},
			{
				"name": "Filmes e Séries",
				"value": "A volta dos que não foram"
			},
			{
				"name": "Minha Sogra é",
				"value": "Atentada"
			},
			{
				"name": "Cores",
				"value": "Azul"
			},
			{
				"name": "Nome",
				"value": "Alberto"
			},
			{
				"name": "Famosos",
				"value": "Alisson"
			}
		]

	}
}
```

- `"type": "validate_response"` -> Envia todas as respostar recebidas para os jogadores validarem.
```json
{

	"data": {
		"type": "validate_response",
		"responses": {
			"Famosos": ["Albert Einstein", "Alisson"],
			...
		},
	}
}
```
- `"type": "invalid_responses"` -> retorna as palavras invalidadas pelo jogador

```json
{
	"data":{
		"type":"invalid_responses",
		"responses": "Famosos": ["Alisson"],
	}
}
```

- `"type": "score"` -> retorna o ranking

```json
{
	"data":{
		"type":"score",
		"ranking": rank
	}
}
```
  

# Desafios encontrados

O maior desafio encontrado foi entender como lidar com inputs de texto no pygame, já que o mesmo não fornece nativamente suporte para isso. A estruturação do projeto e das classes também foi um desafio e se encontra desenvolvido no método "Go Horse", em que as telas/ classes não foram divididas em subclasses o que não afeta o desempenho, mas afeta a legibilidade e manutenção do código.

As interações cliente-servidor foram tranquilas de desenvolver, porém, não conseguimos desenvolver com sucesso o método que busca na rede local o servidor, necessitando que o código seja alterado a cada mudança de host.








