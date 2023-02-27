# Pipeline de dados com Apache Airflow

## Introdução:

Nos dias de hoje, é comum que empresas e organizações precisem lidar com grandes quantidades de dados, provenientes de diversas fontes, e utilizá-los de forma eficiente para obter insights valiosos para o negócio. Para isso, é essencial contar com um pipeline de dados bem estruturado, que possa coletar, armazenar e processar essas informações de forma automatizada e escalável.

Neste contexto, uma solução bastante popular é a combinação de ferramentas como PostegreSQL, Airbyte, Databricks e AWS. O PostegreSQL é um sistema de gerenciamento de bancos de dados relacional bastante poderoso e flexível, capaz de lidar com grandes volumes de dados. O Airbyte é uma plataforma de integração de dados open source, que permite coletar informações de diversas fontes e integrá-las em um único lugar. O Databricks é uma plataforma de processamento de dados escalável em nuvem, que permite executar análises complexas em larga escala. E a AWS é uma plataforma de computação em nuvem amplamente utilizada, que oferece diversas ferramentas e serviços para gerenciar dados e processamento.

Juntos, esses componentes podem formar um pipeline de dados completo e robusto, capaz de lidar com uma grande variedade de casos de uso e de se adaptar às necessidades específicas de cada organização. Neste sentido, a utilização dessas ferramentas pode representar um grande diferencial competitivo para empresas que precisam lidar com grandes volumes de dados e tomar decisões baseadas em insights valiosos.

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

Para preparação do ambiente local, optei para utilização do Docker, que me permite criar, implantar e executar aplicativos em contêineres conforme a imagem a seguir:

imagem

A criação desses contêineres foram feitos de acordo com a documentação Docker: https://docs.docker.com/

### Postegres

Após subir a imagem do Postgres, criei duas tabelas e inseri registros para que possam servir de insumo para a ingestão de dados.

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

Para conexão do ambiente local com a nuvem escolhi o Airbyte, que é uma plataforma de código aberto que permite criar pipelines de dados de forma fácil e escalável. Para isso, precisei configurar o conector do banco de dados (postegres) com o Databricks, conforme a seguir:

imagem



### Interface Airflow:

**Graph:**

![Graph](https://github.com/tycianojr/projeto-airflow/blob/main/img/graph.png)

**Grid:**

![Grid](https://github.com/tycianojr/projeto-airflow/blob/main/img/grid.png)

**Gantt:**

![Grid](https://github.com/tycianojr/projeto-airflow/blob/main/img/gantt.png)










