# Sistema de Gerenciamento de Pedidos

Este é um sistema de gerenciamento de pedidos desenvolvido em Python usando a biblioteca tkinter para a interface gráfica e SQLite como banco de dados. O programa permite aos usuários criar, visualizar, editar e excluir pedidos de clientes, além de filtrar e pesquisar pedidos com base em diferentes critérios.

## Funcionalidades

### Criação de Pedido
- Os usuários podem criar novos pedidos fornecendo informações como nome do cliente, contato, endereço, produto, data do pedido e previsão de entrega.

### Visualização e Filtros
- Os pedidos são exibidos em uma tabela onde os usuários podem ver detalhes como número do pedido, nome do cliente, contato, endereço, data do pedido, previsão de entrega e status.
- Há a opção de filtrar os pedidos com base em diferentes status, como "Para produção", "Em produção", "Falta Pagamento", "Falta Material" e "Concluído".

### Edição de Pedido
- Os usuários podem editar pedidos existentes, incluindo informações como nome do cliente, contato, endereço, produto, datas e status.
- As edições feitas são salvas no banco de dados, mantendo as informações atualizadas.

### Exclusão de Pedido
- Os usuários podem excluir pedidos existentes com uma confirmação de exclusão.
- Os pedidos excluídos são removidos do banco de dados e da visualização.

### Pesquisa de Cliente
- Há uma opção de pesquisa que permite aos usuários encontrar pedidos por número do pedido ou contato do cliente.

## Como Executar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Clone este repositório em sua máquina local.
3. Abra um terminal na pasta do projeto e execute o seguinte comando para instalar as dependências: <br>
```pip install customtkinter tkinter tkcalendar sqlite3```
5. Execute o programa com o seguinte comando: <br>
```python main.py```

## Capturas de Tela

![image](https://github.com/Carlos-Guilherme/Gerenciamento_de_pedidos/assets/72580077/ff97ef61-3655-4921-b56c-549692cfdbe6)
![image](https://github.com/Carlos-Guilherme/Gerenciamento_de_pedidos/assets/72580077/0562fcf8-7266-42e1-93b2-13a257f7b01d)


## Contribuições

Contribuições são bem-vindas! Se você encontrar algum problema, tiver ideias para melhorias ou quiser adicionar novas funcionalidades, fique à vontade para fazer um fork deste repositório e enviar pull requests.

## Autor

Carlos Guilherme

## Licença

Este projeto está licenciado sob a Licença GNU - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.
