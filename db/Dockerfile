FROM postgis/postgis:11-2.5-alpine


ADD data /tmp/data
ADD 1ddl.sql /docker-entrypoint-initdb.d/1ddl.sql
ADD 2dml.sql /docker-entrypoint-initdb.d/2dml.sql
