create table cotacao_dolar (
	data DATE primary key,
    cotacaoCompra DECIMAL(8,4),
    cotacaoVenda DECIMAL(8,4),
    dataHoraCotacao DATETIME,
    dataExtracao DATETIME

);

create table base_clientes (
	conta varchar(20),
    data date,
    posicaoUSD DECIMAL(15,4)
);
