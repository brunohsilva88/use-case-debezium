FROM jupyter/pyspark-notebook:latest

USER ${NB_UID}

EXPOSE 8888

RUN mamba install --yes \
    'grpcio-status' \
    'grpcio' \
    'pandas=2.2.2' \
    'kafka-python' \
    'psycopg2' \
    'pyarrow' && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"