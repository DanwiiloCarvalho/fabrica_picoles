import sqlalchemy as sa
from sqlalchemy import Engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from models.model_base import ModelBase

__engine: Engine | None = None


def create_engine() -> Engine:
    """
    Função para configurar a conexão ao banco de dados
    """
    global __engine

    if __engine:
        return

    __engine = sa.create_engine(
        'postgresql://postgres:postgres@localhost:5432/picoles')  # echo=True
    return __engine


def create_session() -> Session:
    """
    Função para criar a sessão de conexão ao banco de dados
    """
    global __engine

    if not __engine:
        create_engine()
    __session = sessionmaker(bind=__engine, expire_on_commit=False)

    session: Session = __session()
    return session


def create_tables() -> None:
    global __engine

    if not __engine:
        create_engine()

    import models.__all__models
    ModelBase.metadata.drop_all(bind=__engine)
    ModelBase.metadata.create_all(bind=__engine)
