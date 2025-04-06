SELECT
  id,
  nome,
  estado
FROM {{ ref('stg_clientes') }}
WHERE ativo = TRUE
