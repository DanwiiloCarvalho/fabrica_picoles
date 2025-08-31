from typing import List

from faker import Faker
from sqlalchemy import select

from conf.db_session import create_session, create_tables
from models.aditivo_nutritivo import AditivoNutritivo
from models.conservante import Conservante
from models.ingrediente import Ingrediente
from models.picole import Picole
from models.revendedor import Revendedor
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.lote import Lote
from models.nota_fiscal import NotaFiscal

# Configuração do Faker
fake = Faker('pt_BR')

# Criar tabelas
create_tables()

# Criar sessão
session = create_session()


def populate_aditivos_nutritivos():
    aditivos = [
        "Vitamina C",
        "Vitamina D",
        "Vitamina B12",
        "Ferro",
        "Cálcio",
        "Proteína",
        "Fibras"
    ]

    for nome in aditivos:
        aditivo = AditivoNutritivo(
            nome=nome, formula_quimica=fake.lexify(text="???-???-???"))
        session.add(aditivo)

    session.commit()


def populate_conservantes():
    conservantes = [
        "Sorbato de Potássio",
        "Benzoato de Sódio",
        "Ácido Cítrico",
        "Metabissulfito de Sódio",
        "Nitrito de Sódio"
    ]

    for nome in conservantes:
        conservante = Conservante(
            nome=nome, descricao=fake.text(max_nb_chars=45))
        session.add(conservante)

    session.commit()


def populate_sabores():
    sabores = [
        "Morango",
        "Chocolate",
        "Baunilha",
        "Creme",
        "Napolitano",
        "Flocos",
        "Pistache"
    ]

    for nome in sabores:
        sabor = Sabor(nome=nome)
        session.add(sabor)

    session.commit()


def populate_ingredientes():
    ingredientes = [
        "Leite",
        "Açúcar",
        "Cacau",
        "Morango",
        "Água",
        "Creme de Leite",
        "Leite Condensado"
    ]

    for nome in ingredientes:
        ingrediente = Ingrediente(nome=nome)
        session.add(ingrediente)

    session.commit()


def populate_tipos_embalagem():
    tipos = [
        "Papel",
        "Plástico",
        "Papelão",
        "Plástico Reciclável"
    ]

    for nome in tipos:
        tipo = TipoEmbalagem(nome=nome)
        session.add(tipo)

    session.commit()


def populate_tipos_picole():
    tipos = [
        "Água",
        "Cremoso",
        "Frutas",
        "Premium"
    ]

    for nome in tipos:
        tipo = TipoPicole(nome=nome)
        session.add(tipo)

    session.commit()


def populate_revendedores():
    for _ in range(5):
        revendedor = Revendedor(
            cnpj=fake.cnpj(),
            razao_social=fake.company(),
            contato=fake.name()
        )
        session.add(revendedor)

    session.commit()


def populate_picoles():
    # Recuperar dados necessários
    stmt_sabores = select(Sabor)
    sabores: List[Sabor] = session.scalars(stmt_sabores).unique().all()

    stmt_tipos = select(TipoPicole)
    tipos: List[TipoPicole] = session.scalars(stmt_tipos).unique().all()

    stmt_embalagens = select(TipoEmbalagem)
    embalagens: List[TipoEmbalagem] = session.scalars(
        stmt_embalagens).unique().all()

    stmt_ingredientes = select(Ingrediente)
    ingredientes: List[Ingrediente] = session.scalars(
        stmt_ingredientes).unique().all()

    stmt_conservantes = select(Conservante)
    conservantes: List[Conservante] = session.scalars(
        stmt_conservantes).unique().all()

    stmt_aditivos = select(AditivoNutritivo)
    aditivos: List[AditivoNutritivo] = session.scalars(
        stmt_aditivos).unique().all()

    # Criar picolés
    for _ in range(10):
        picole = Picole(
            preco=fake.pyfloat(min_value=2, max_value=10, right_digits=2),
            id_sabor=fake.random_element(elements=sabores).id,
            id_tipo_picole=fake.random_element(elements=tipos).id,
            id_tipo_embalagem=fake.random_element(elements=embalagens).id,
        )

        # Adicionar ingredientes aleatórios
        for _ in range(fake.random_int(min=2, max=4)):
            picole.ingredientes.append(
                fake.random_element(elements=ingredientes))

        # Adicionar conservantes aleatórios
        for _ in range(fake.random_int(min=1, max=2)):
            picole.conservantes.append(
                fake.random_element(elements=conservantes))

        # Adicionar aditivos nutricionais aleatórios
        for _ in range(fake.random_int(min=1, max=3)):
            picole.aditivos_nutritivos.append(
                fake.random_element(elements=aditivos))

        session.add(picole)

    session.commit()


def populate_notas_fiscais_e_lotes():
    # Recuperar revendedores e tipos de picolés
    stmt_revendedores = select(Revendedor)
    revendedores: List[Revendedor] = session.scalars(
        stmt_revendedores).unique().all()

    stmt_tipos_picole = select(TipoPicole)
    tipos_picole: List[TipoPicole] = session.scalars(
        stmt_tipos_picole).unique().all()

    # Criar notas fiscais e lotes
    for _ in range(5):
        revendedor = fake.random_element(elements=revendedores)
        nota = NotaFiscal(
            valor=fake.pyfloat(min_value=100, max_value=1000, right_digits=2),
            numero_serie=str(fake.unique.random_number(digits=8)),
            descricao=fake.text(max_nb_chars=100),
            id_revendedor=revendedor.id,
            data=fake.date_time_between(start_date='-2y', end_date='now')
        )
        session.add(nota)
        session.flush()  # Para obter o ID da nota fiscal

        # Criar lotes para esta nota fiscal
        for _ in range(fake.random_int(min=1, max=3)):
            tipo_picole = fake.random_element(elements=tipos_picole)
            lote = Lote(
                id_tipo_picole=tipo_picole.id,
                quantidade=fake.random_int(min=100, max=500)
            )
            session.add(lote)
            session.flush()  # Para obter o ID do lote

            # Relacionar lote com nota fiscal
            nota.lotes.append(lote)

    session.commit()


if __name__ == '__main__':
    # Populando as tabelas em ordem
    populate_aditivos_nutritivos()
    populate_conservantes()
    populate_sabores()
    populate_ingredientes()
    populate_tipos_embalagem()
    populate_tipos_picole()
    populate_revendedores()
    populate_picoles()
    populate_notas_fiscais_e_lotes()

    print("Banco de dados populado com sucesso!")
