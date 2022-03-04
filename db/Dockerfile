FROM postgis/postgis:11-2.5-alpine

ENV POSTGRES_USER carto_test
ENV POSTGRES_PASSWORD carto_test

ADD data /tmp/data
ADD 1ddl.sql /docker-entrypoint-initdb.d/1ddl.sql
ADD 2dml.sql /docker-entrypoint-initdb.d/2dml.sql
