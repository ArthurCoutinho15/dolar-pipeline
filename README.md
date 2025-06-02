<h1>Teste técnico -Pipeline extração dados do dólar na API Banco Central</h1>
<h2>Estrutura do projeto</h2>
<img src="https://github.com/ArthurCoutinho15/dolar-pipeline/blob/main/img/Diagrama.png" alt="Diagrama pipeline">
<p> 
    O Pipeline se iniciou organizando o Código em um paradigma orientado a objetos permitindo modularização e organização. 
    A primeira etapa foi a extração da API utilizando requests. Logo após, a transformação dos dados ocorreram fazendo o tratamento de dados nulos, pois a api não retorna dados dos finais de semana e feriados
    então a alternativa foi utilizar a cotação do dia anterior. 
    Após isso, ocorreu a persitência dos dados em arquivos parquet com um bucket no Amazon S3.
    Em seguida ocorre carga incremental no MySQL.
    Após a carga de dados, para o cálculo da posição do cliente em Reais, utilizei o dbt para criar uma camada analítica e realizar os cálculos com sql. 
    Todo esse processo foi orquestrado pelo apache airflow com docker-compose e disponibilização dos dados finais em um notebook.
</p>
<h3>Tabela MySql dados Extração API</h3>
<img src="https://github.com/ArthurCoutinho15/dolar-pipeline/blob/main/img/Captura%20de%20tela%202025-06-01%20225955.png" alt="Diagrama pipeline">
<h3>Tabela Posição em Reais</h3>
<img src="https://github.com/ArthurCoutinho15/dolar-pipeline/blob/main/img/imagem_2025-06-01_231923017.png" alt="Diagrama pipeline">
<h3>Tabela Receita ao Mês</h3>
<img src="https://github.com/ArthurCoutinho15/dolar-pipeline/blob/main/img/Captura%20de%20tela%202025-06-01%20230021.png" alt="Diagrama pipeline">
<h3>Bucket S3</h3>
<img src="https://github.com/ArthurCoutinho15/dolar-pipeline/blob/main/img/imagem_2025-06-01_232039976.png" alt="Diagrama pipeline">
