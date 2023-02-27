# Analytics


# Lista o conteúdo
dbutils.fs.ls("s3://learning-databricks-thsaj/dados/dbadmin/")

# Carrega os dados em um dataframe do Spark
df = spark.read.load("s3://learning-databricks-thsaj/dados/dbadmin/thsaj_tb_usuarios/")

# Visualiza os dados
display(df) 

# Executa query SQL
%sql
SELECT nome_usuario, nome_cidade
FROM dbadmin.thsaj_tb_usuarios, dbadmin.thsaj_tb_cidades
WHERE dbadmin.thsaj_tb_cidades.codigo_cidade = dbadmin.thsaj_tb_usuarios.cod_cidade;

# Executa query SQL
%sql
SELECT nome_cidade, COUNT(*)
FROM dbadmin.thsaj_tb_usuarios, dbadmin.thsaj_tb_cidades
WHERE dbadmin.thsaj_tb_cidades.codigo_cidade = dbadmin.thsaj_tb_usuarios.cod_cidade
GROUP BY nome_cidade;