# Automação de Cadastro de Produtos (RPA) 🤖🐍

Este repositório contém um projeto de Automação Robótica de Processos (RPA) desenvolvido em **Python**. O objetivo é ler uma base de dados de produtos em um arquivo CSV e cadastrá-los automaticamente em um sistema web, simulando interações humanas de mouse e teclado.

## 🚀 Tecnologias Utilizadas

* **Python**
* **PyAutoGUI** (Automação de interface gráfica - mouse e teclado)
* **Pandas** (Leitura e manipulação de dados em CSV)

## 📁 Estrutura do Projeto

* `codigo.py`: Script principal que realiza a automação (abre o navegador, faz login e cadastra os itens um a um).
* `auxiliar.py`: Script de apoio para capturar as coordenadas `(x, y)` do mouse na tela.
* `produtos.csv`: Base de dados contendo os produtos que serão cadastrados pelo robô.

## ⚙️ Como Funciona o Robô

1. Abre o navegador (Google Chrome) e acessa a página de login do sistema.
2. Preenche os dados de acesso (e-mail e senha) e faz o login automaticamente.
3. Importa a base de dados do arquivo `produtos.csv`.
4. Através de um loop de repetição, percorre cada linha da tabela e preenche o formulário web com as informações de cada produto (código, marca, tipo, categoria, preço, custo e observações).
5. O processo se repete ininterruptamente até que toda a tabela seja cadastrada.

## 🛠️ Como Executar na Sua Máquina
### 1. Instalação das dependências
Certifique-se de ter o Python instalado. Em seguida, instale as bibliotecas necessárias rodando o comando abaixo no terminal:

```bash
pip install pyautogui pandas
```
2. Ajuste de Coordenadas (Aviso Importante ⚠️)
O PyAutoGUI baseia seus cliques na resolução da tela do computador onde o código foi escrito. Portanto, as coordenadas do arquivo codigo.py (pyautogui.click(x, y)) muito provavelmente precisarão ser ajustadas para o seu monitor.

Para ajustar e rodar:

Abra a tela onde o clique deve acontecer.

Execute o arquivo auxiliar.py, posicione o mouse no local desejado e aguarde 5 segundos para que a coordenada seja impressa no terminal.

Atualize os valores de click() dentro do codigo.py com as suas novas coordenadas.

Execute o codigo.py e deixe o robô trabalhar.

