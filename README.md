# Projeto de Web Scraping com Selenium

Este projeto foi desenvolvido como parte de um teste para a empresa RIVEO. Utiliza o Selenium para buscar
notícias sobre "Deadpool" no site Omelete, extraindo títulos e datas, e salvando essas informações em um arquivo de texto.

## Requisitos

- Python 3.x
- Google Chrome e ChromeDriver compatível
- Biblioteca `selenium`

## Uso

1. Instale as dependências com `pip install selenium`.
2. Execute o comando `py main.py` para buscar e salvar notícias.

## Funcionamento

O script automatiza o Chrome para navegar até o site Omelete, buscar pelo nome "Deadpool",
rolar a página para carregar TODOS os resultados e salvar os títulos e datas das notícias encontradas.

No arquivo title_deadpool.txt, serão inseridas somente as notícias que possuem o nome Deadpool no título.

No arquivo deadpool_news.txt, serão inseridas as notícias relacionadas ao Deadpool, tanto as notícias que tenham o nome Deadpool no título,
quanto as que não tenham o nome no título, mas falam sobre dentro do artigo.