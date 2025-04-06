SELECT
  id,
  UPPER(nome) AS nome,
  cidade,
  estado,
  ativo
FROM public.clientes