with source as (
    select * from {{ source ('dolar_pipeline', 'cotacao_dolar')}}
),

renamed as (
    select 
        {{ adapter.quote('data') }},
        {{ adapter.quote('cotacaoCompra')}},
        {{ adapter.quote('cotacaoVenda')}},
        {{ adapter.quote('dataHoraCotacao')}},
        {{ adapter.quote('dataExtracao')}}
    from source
)

select *
from renamed