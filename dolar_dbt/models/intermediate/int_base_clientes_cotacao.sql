with base_clientes as (
    select *
    from {{ref("stg_base_clientes")}}
),

cotacao_dolar as (
    select *
    from {{ref("stg_cotacao_dolar")}}
)

select 
    bc.conta,
    bc.data,
    bc.posicaoUSD as posicao_USD,
    cd.cotacaoCompra, 
    cd.cotacaoVenda,
    cd.dataHoraCotacao,
    cd.dataExtracao
from 
    base_clientes as bc 
left join 
    cotacao_dolar as cd on bc.data = cd.data