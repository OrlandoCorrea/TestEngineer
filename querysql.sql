CREATE TABLE agrupacion_por_pais AS
SELECT "Pais del tratado" as "Pais", 
count("Pais del tratado") FILTER (WHERE "Vigente" = True) as "Cantidad de tratados vigentes",
count("Pais del tratado") FILTER (WHERE "Vigente" = False) as "Cantidad de tratados no vigentes",
MIN("Fecha de Adopcion") as "Fecha de Adopcion primer tratado",
floor(((current_date - MIN("Fecha de Adopcion"))*0.0328549)+1)::integer AS "Diferencia en meses desde el primer acuerdo a la fecha actual"
FROM public.tratados 
GROUP BY "Pais del tratado";