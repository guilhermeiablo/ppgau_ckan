#!/bin/sh
psql -U postgres -c "CREATE USER ${CKAN_POSTGRES_USER} \
    WITH PASSWORD '${CKAN_POSTGRES_PWD}' \
    NOSUPERUSER NOCREATEDB NOCREATEROLE;"

createdb -U postgres -e -O ${CKAN_POSTGRES_USER} ${CKAN_POSTGRES_DB} -E utf-8
