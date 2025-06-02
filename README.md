<h1>Teste técnico -Pipeline extração dados do dólar na API Banco Central</h1>
<h2>Estrutura do projeto</h2>
<img src="" alt="">
<p> 
    O Pipeline se iniciou organizando o Código em um paradigma orientado a objetos permitindo modularização e organização. 
    A primeira etapa foi a extração da API utilizando requests, logo após a transformação dos dados ocorreram fazendo o tratamento de dados nulos, pois a api não retorna dados dos finais de semana e feriados
    então a alternativa foi utilizar a cotação do dia anterior. 
    Após isso, ocorreu a persitência dos dados em arquivos parquet com um bucket no Amazon S3.
    Em seguida ocorre carga incremental no MySQL.
    Após a carga de dados, para o cálculo da posição do cliente em Reais, utilizei o dbt para criar uma camada analítica e realizar os cálculos com sql. 
    Todo esse processo foi orquestrado pelo apache airflow com docker-compose e disponibilização dos dados finais em um notebook.
</p>
