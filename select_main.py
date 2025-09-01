from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.picole import Picole


def select_todos_aditivos_nutritivos() -> None:

    aditivos_nutritivos: list[AditivoNutritivo] | None = None

    with create_session() as session:
        # Forma 1
        aditivos_nutritivos = session.query(AditivoNutritivo).all()
        # Forma 2
        # aditivos_nutritivos = session.query(AditivoNutritivo)

    # return aditivos_nutritivos
    for aditivo in aditivos_nutritivos:
        print(aditivo)


def select_sabor_by_id(id: int) -> None:
    sabor: Sabor | None = None

    with create_session() as session:
        sabor = session.query(Sabor).filter_by(id=id).one_or_none()

    print(sabor)


def select_picole_by_id(id: int) -> None:
    picole: Picole | None = None

    with create_session() as session:
        picole = session.query(Picole).filter_by(id=id).one_or_none()

    if picole:
        print(f'ID: {picole.id}')
        print(f'Data_Criação: {picole.data_criacao}')
        print(f'Preço: {picole.preco}')
        print(f'Sabor: {picole.sabor.nome}')
        print(f'Embalagem: {picole.tipo_embalagem.nome}')
        print(f'Tipo: {picole.tipo_picole.nome}')
        print(f'Conservantes: {picole.conservantes}')
        print(f'Aditivos nutritivos: {picole.aditivos_nutritivos}')
        print(f'Ingredientes: {picole.ingredientes}')


if __name__ == '__main__':
    # select_todos_aditivos_nutritivos()
    # select_sabor_by_id(2)
    select_picole_by_id(id=2)
    # picole: Picole = select_picole_by_id(id=2)

    # if picole:
    #     print(f'ID: {picole.id}')
    #     print(f'Data_Criação: {picole.data_criacao}')
    #     print(f'Preço: {picole.preco}')
    #     print(f'Sabor: {picole.sabor.nome}')
    #     print(f'Embalagem: {picole.tipo_embalagem.nome}')
    #     print(f'Tipo: {picole.tipo_picole.nome}')
    #     print(f'Conservantes: {picole.conservantes}')
    #     print(f'Aditivos nutritivos: {picole.aditivos_nutritivos}')
    #     print(
    #         f'Aditivos nutritivos: {[aditivo.nome for aditivo in picole.aditivos_nutritivos]}')
    #     print(f'Ingredientes: {picole.ingredientes}')
