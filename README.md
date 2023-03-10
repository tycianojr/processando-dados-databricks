# Processando Dados com Databricks

## Introdução:

Nos dias de hoje, é comum que empresas e organizações precisem lidar com grandes quantidades de dados, provenientes de diversas fontes, e utilizá-los de forma eficiente para obter insights valiosos para o negócio. Para isso, é essencial contar com um pipeline de dados bem estruturado, que possa coletar, armazenar e processar essas informações de forma automatizada e escalável.

Neste contexto, uma solução bastante popular é a combinação de ferramentas como Docker, Postgres, Airbyte, Databricks e AWS. Juntos, esses componentes podem formar um pipeline de dados completo e robusto, capaz de lidar com uma grande variedade de casos de uso e de se adaptar às necessidades específicas de cada organização. Neste sentido, a utilização dessas ferramentas pode representar um grande diferencial competitivo para empresas que precisam lidar com grandes volumes de dados e tomar decisões baseadas em insights valiosos.

## Objetivo

O objetivo do projeto é mostrar a construção da pipeline em ambiente local para nuvem e quais ferramentas e recursos o Engenheiro de Dados pode utilizar para apresentar soluções.

## Descrição do processamento:

### Local

- Docker
- Postgres
- Airbyte

### Nuvem

- Databricks Platform
- Amazon Web Services

Para preparação do ambiente local, optei utilizar o Docker, que me permite criar, implantar e executar aplicativos em contêineres conforme a imagem a seguir:

![docker](https://github.com/tycianojr/processando-dados-databricks/blob/main/img/docker.png)

A criação desses contêineres foram feitos de acordo com a documentação: https://docs.docker.com/

### Postgres

Após subir a imagem do Postgres, criei duas tabelas e inseri registros para que possam servir de insumo como fonte de dados.

```
CREATE SCHEMA dbadmin AUTHORIZATION dbadmin;

# Cria tabela
CREATE TABLE dbadmin.tb_usuarios
(
    id_usuario integer NOT NULL,
    nome_usuario character varying(50),
    cod_cidade character varying(5),
    PRIMARY KEY (id_usuario)
);

# Cria tabela
CREATE TABLE dbadmin.tb_cidades
(
    codigo_cidade character varying(5),
    nome_cidade character varying(50),
    PRIMARY KEY (codigo_cidade)
);

# Carrega dados
INSERT INTO dbadmin.tb_cidades(codigo_cidade, nome_cidade)
VALUES ('FOR01', 'Fortaleza');

INSERT INTO dbadmin.tb_cidades(codigo_cidade, nome_cidade)
VALUES ('BLU01', 'Blumenau');

INSERT INTO dbadmin.tb_cidades(codigo_cidade, nome_cidade)
VALUES ('UBA01', 'Ubatuba');

INSERT INTO dbadmin.tb_usuarios(id_usuario, nome_usuario, cod_cidade)
VALUES (1001, 'Bob Silva', 'BLU01');

INSERT INTO dbadmin.tb_usuarios(id_usuario, nome_usuario, cod_cidade)
VALUES (1002, 'Monica Teixeira', 'BLU01');

INSERT INTO dbadmin.tb_usuarios(id_usuario, nome_usuario, cod_cidade)
VALUES (1003, 'Josenildo Farias', 'FOR01');

INSERT INTO dbadmin.tb_usuarios(id_usuario, nome_usuario, cod_cidade)
VALUES (1004, 'Maria Joy', 'UBA01');

INSERT INTO dbadmin.tb_usuarios(id_usuario, nome_usuario, cod_cidade)
VALUES (1005, 'Alex Tavares', 'FOR01');

# Cria chave estrangeira
ALTER TABLE dbadmin.tb_usuarios
    ADD CONSTRAINT "FK_CIDADE" FOREIGN KEY (cod_cidade)
    REFERENCES dbadmin.tb_cidades (codigo_cidade)
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


```

### Airbyte

Para conexão do ambiente local com a nuvem, escolhi o Airbyte, que é uma plataforma de código aberto que permite criar pipelines de dados de forma fácil e escalável. Para isso, precisei configurar o conector do banco de dados (postegres) com o Databricks, conforme a seguir:

![airbyte](https://github.com/tycianojr/processando-dados-databricks/blob/main/img/airbyte1.png)

Para conseguir fazer a conexão da fonte de dados e do destino é preciso passar configurações de credenciais:

### Airbyte - Postgres

![airbyte](https://github.com/tycianojr/processando-dados-databricks/blob/main/img/airbyte-conexão1.png)

### Airbyte - Databricks

![airbyte](https://github.com/tycianojr/processando-dados-databricks/blob/main/img/airbyte-conexão2.png)

###  Airbyte - AWS

![airbyte](https://github.com/tycianojr/processando-dados-databricks/blob/main/img/airbyte-conexão3.png)

Mais informações: https://docs.airbyte.com/

### AWS e Databricks

A configuração do ambiente AWS com o Databricks foi feito de acordo com a documentação: https://docs.databricks.com/

### AWS

Após a configuração de toda a infraestrutura com o arquivo .yaml que a Databricks fornece para subida do pseudo-cluster utilizando o CloudFormation, são criadas instâncias EC2, buckets S3, IAM roles.

Buckets S3:

![airbyte](https://github.com/tycianojr/processando-dados-databricks/blob/main/img/bucket.png)


A camada de armazenamento utilizada é o Delta Lake, possibilitando a manipulação de arquivos no ambiente Databricks

### Databricks

Após o Airbyte fazer a ingestão de dados do Postgres para o Data Lake, é possível construir uma pipeline analytics conforme a necessidade do projeto:

![databricks1](https://github.com/tycianojr/processando-dados-databricks/blob/main/img/databricks1.png)

O databricks possui ferramentas de gráfico e dashboard, que dependendo da complexidade do projeto, podem ser utilizadas para uma visualização rápida do comportamento dos dados:

![databricks1](https://github.com/tycianojr/processando-dados-databricks/blob/main/img/databricks2.png)


