with source as (
    select * from {{ source ('dolar_pipeline', 'base_clientes')}}
),

renamed as (
    select 
        {{ adapter.quote('conta') }},
        {{ adapter.quote('data')}},
        {{ adapter.quote('posicaoUSD')}}
    from source
)

select *
from renamed