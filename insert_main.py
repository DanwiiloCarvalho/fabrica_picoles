from datetime import datetime
from decimal import Decimal
from conf.db_session import create_session
# Insert parte 1
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor
# Insert parte 2
from models.lote import Lote
from models.nota_fiscal import NotaFiscal
from models.picole import Picole


def insert_aditivo_nutritivo() -> AditivoNutritivo:
    print('Cadastrando Aditivo Nutritivo')

    nome: str = input('Informe o nome do aditivo nutritivo: ')
    formula_quimica: str = input('Informe a fórmula química: ')

    an: AditivoNutritivo = AditivoNutritivo(
        nome=nome, formula_quimica=formula_quimica)

    with create_session() as session:
        session.add(an)
        session.commit()

        # print(
        #     f'ID: {an.id}\nNome aditivo nutritivo: {an.nome}\nFórmula: {an.formula_quimica}')
        # print(f'Data criação: {an.data_criacao}')

    return an


def insert_sabor() -> Sabor:
    print('Cadastrando Sabor')

    nome_sabor: str = input('Informe o nome do sabor: ')
    sabor: Sabor = Sabor(nome=nome_sabor)

    with create_session() as session:
        session.add(sabor)
        session.commit()

        # print(f'ID do sabor: {sabor.id}\nSabor: {sabor.nome}')
        # print(f'Data de criação: {sabor.data_criacao}')

    return sabor


def insert_tipo_embalagem() -> TipoEmbalagem:
    print('Cadastrando Tipo de embalagem')

    nome_tipo_embalagem: str = input('Informe o tipo de embalagem: ')
    tipo_embalagem: TipoEmbalagem = TipoEmbalagem(nome=nome_tipo_embalagem)

    with create_session() as session:
        session.add(tipo_embalagem)
        session.commit()

        # print(
        #     f'ID do tipo de embalagem: {tipo_embalagem.id}\nNome do tipo de embalagem: {tipo_embalagem.nome}')
        # print(f'Data de criação: {tipo_embalagem.data_criacao}')

    return tipo_embalagem


def insert_tipo_picole() -> TipoPicole:
    print('Cadastrando tipo de picolé')

    nome_tipo_picole: str = input('Informe o tipo de picolé: ')
    tipo_picole: TipoPicole = TipoPicole(nome=nome_tipo_picole)

    with create_session() as session:
        session.add(tipo_picole)
        session.commit()

    return tipo_picole


def insert_conservante() -> Conservante:
    print('Cadastrando conservante')

    nome_conservante: str = input('Informe o nome do conservante: ')
    descricao_conservante: str = input('Informe a descrição do conservante: ')
    conservante: Conservante = Conservante(
        nome=nome_conservante, descricao=descricao_conservante)

    with create_session() as session:
        session.add(conservante)
        session.commit()

        # print(
        #     f'ID do conservante: {conservante.id}\nConservante: {conservante.nome}')
        # print(f'Data de criação: {conservante.data_criacao}')

    return conservante


def insert_ingrediente() -> Ingrediente:
    print('Cadastrando ingrediente')

    nome_ingrediente: str = input('Informe o nome do ingrediente: ')
    ingrediente: Ingrediente = Ingrediente(nome=nome_ingrediente)

    with create_session() as session:
        session.add(ingrediente)
        session.commit()

        # print(
        #     f'ID do ingrediente: {ingrediente.id}\nIngrediente: {ingrediente.nome}')
        # print(f'Data de criação: {ingrediente.data_criacao}')

    return ingrediente


def insert_revendedor() -> Revendedor:
    print('Cadastrando revendedor')

    cnpj: str = input('Informe o CNPJ: ')
    razao_social: str = input('Informe a razão social: ')
    contato: str = input('Informe o contato do revendedor: ')

    revendedor: Revendedor = Revendedor(
        cnpj=cnpj, razao_social=razao_social, contato=contato)

    with create_session() as session:
        session.add(revendedor)
        session.commit()

    return revendedor


def insert_lote() -> Lote:
    print('Cadastrando lote')

    quantidade: int = int(input('Informe a quantidade: '))
    id_tipo_picole: int = int(input('Informe o ID do tipo de picolé: '))

    lote: Lote = Lote(quantidade=quantidade, id_tipo_picole=id_tipo_picole)

    with create_session() as session:
        session.add(lote)
        session.commit()

    return lote


def insert_nota_fiscal() -> NotaFiscal:
    print('Cadastrando nota fiscal')

    data: datetime = input('Informe a data da nota fiscal: ')
    valor: Decimal = Decimal(input('Informe o valor da nota fiscal: '))
    numero_serie: str = input('Informe o número de série: ')
    descricao: str = input('Informe a descrição da nota fiscal: ')
    id_revendedor: int = int(input('Informe o ID do revendedor: '))

    novo_lote: Lote = insert_lote()

    nota_fiscal: NotaFiscal = NotaFiscal(
        valor=valor, numero_serie=numero_serie, descricao=descricao, data=data, id_revendedor=id_revendedor)

    nota_fiscal.lotes.append(novo_lote)

    with create_session() as session:
        session.add(nota_fiscal)
        session.commit()

    return nota_fiscal


def insert_picole() -> Picole:
    print('Cadastrando picolé')

    preco: Decimal = Decimal(input('Informe o preço do picolé: '))
    id_sabor: int = int(input('Informe o ID do sabor: '))
    id_tipo_embalagem: int = int(input('Informe o ID do tipo de embalagem: '))
    id_tipo_picole: int = int(input('Informe o ID do tipo de picolé: '))

    novo_picole: Picole = Picole(
        preco=preco, id_sabor=id_sabor, id_tipo_embalagem=id_tipo_embalagem, id_tipo_picole=id_tipo_picole)

    novo_ingrediente1: Ingrediente = insert_ingrediente()
    novo_ingrediente2: Ingrediente = insert_ingrediente()

    novo_aditivo_nutritivo: AditivoNutritivo = insert_aditivo_nutritivo()

    novo_conservante: Conservante = insert_conservante()

    novo_picole.ingredientes.append(novo_ingrediente1)
    novo_picole.ingredientes.append(novo_ingrediente2)

    novo_picole.aditivos_nutritivos.append(novo_aditivo_nutritivo)

    novo_picole.conservantes.append(novo_conservante)

    with create_session() as session:
        session.add(novo_picole)
        session.commit()

        print(f'Preço do picolé: {novo_picole.preco}')
        print(f'Sabor do picolé: {novo_picole.sabor.nome}')
        print(f'Tipo do picolé: {novo_picole.tipo_picole.nome}')
        print(f'Embalagem do picolé: {novo_picole.tipo_embalagem.nome}')
        print(f'Ingredientes do picolé: {novo_picole.ingredientes}')
        print(f'Conservantes do picolé: {novo_picole.conservantes}')
        print(
            f'Aditivos Nutritivos do picolé: {novo_picole.aditivos_nutritivos}')

    return novo_picole


if __name__ == '__main__':
    # 1 Aditivo Nutritivo
    # insert_aditivo_nutritivo()

    # 2 Sabor
    # insert_sabor()

    # 3 Tipo Embalagem
    # insert_tipo_embalagem()

    # 4 Tipo Picolé
    # tipo_picole: TipoPicole = insert_tipo_picole()
    # print(f'ID do tipo de picolé: {tipo_picole.id}')
    # print(f'Nome do tipo de picolé: {tipo_picole.nome}')
    # print(f'Data de criação do tipo de picolé: {tipo_picole.data_criacao}')

    # 5 Ingrediente
    # ingrediente: Ingrediente = insert_ingrediente()
    # print(f'ID do ingrediente: {ingrediente.id}')
    # print(f'Nome do ingrediente: {ingrediente.nome}')
    # print(f'Data de criação do ingrediente: {ingrediente.data_criacao}')

    # 6 Conservante
    # insert_conservante()

    # 7 Revendedor
    # revendedor: Revendedor = insert_revendedor()
    # print(f'ID do revendedor: {revendedor.id}')
    # print(f'CNPJ do revendedor: {revendedor.cnpj}')
    # print(f'Razão social do revendedor: {revendedor.razao_social}')
    # print(f'Contato do revendedor: {revendedor.contato}')
    # print(f'Data criação do revendedor: {revendedor.data_criacao}')

    # 7 Lote
    # lote: Lote = insert_lote()
    # print(f'ID do lote: {lote.id}')
    # print(f'Quantidade do lote: {lote.quantidade}')
    # print(f'Id do tipo de picolé do lote: {lote.id_tipo_picole}')
    # print(f'Data de criação do lote: {lote.data_criacao}')

    # 8 NotaFiscal
    # nota_fiscal: NotaFiscal = insert_nota_fiscal()
    # print(f'ID nota fiscal: {nota_fiscal.id}')
    # print(f'Data da nota fiscal: {nota_fiscal.data}')
    # print(f'Valor da nota fiscal: {nota_fiscal.valor}')
    # print(f'Número de série da nota fiscal: {nota_fiscal.numero_serie}')
    # print(f'Descrição da nota fiscal: {nota_fiscal.descricao}')
    # print(f'ID do revendedor: {nota_fiscal.id_revendedor}')

    # 9 Picole
    insert_picole()
