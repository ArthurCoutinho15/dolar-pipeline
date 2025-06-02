with source as (
    select *
    from {{ref("mts_posicao_brl")}}
)

select 
    conta, 
    month(data) as mes, 
    year(data) as ano, 
    sum(receita_ao_dia) as receita_mes
from source
group by 1, 2, 3 

