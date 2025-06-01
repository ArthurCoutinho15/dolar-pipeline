with source as (
    select *
    from {{ref("int_base_clientes_cotacao")}}
),

posicao_BRL as (
    select 
        a.conta, 
        a.data, 
        a.posicao_USD,
        a.cotacaoVenda as cotacao_dolar, 
        round((a.posicao_USD * a.cotacaoVenda),2) as posicao_BRL
    from source as a
),

receita_ao_dia as (
    select 
        *,
        round(((posicao_BRL * 0.00137) / 100),2) as receita_ao_dia
    from posicao_BRL
)

select *
from receita_ao_dia

