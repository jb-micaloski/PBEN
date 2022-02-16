import pandas as pd
from aspirante import Aspirante
import re

aspirante_nulo = Aspirante()

aspirante_nulo.numero_atual = 'XXXX'
aspirante_nulo.nome_guerra = 'Nome não encontrado'
def cria_aspirantes(pben):
    aspirantes = []

    for i in range(len(pben)):
        aspirante = Aspirante()

        aspirante.numero_interno_atual = pben['Número Interno Atual'][i]
        #Alterar datas
        aspirante.numero_interno_2021 = pben['Número Interno 2021'][i]
        aspirante.numero_interno_2020 = pben['Número Interno 2020'][i]
        aspirante.numero_interno_2019 = pben['Número Interno 2019'][i]
        aspirante.numero_interno_2018 = pben['Número Interno 2018'][i]
        aspirante.nome_guerra = pben['Nome de Guerra'][i]
        aspirante.nome_completo = pben['Nome Completo'][i]
        aspirante.companhia = pben['Companhia'][i]
        aspirante.pelotao = pben['Pelotão'][i]
        aspirante.alojamento = pben['Alojamento/Camarote'][i]
        aspirante.nip = pben['N.I.P.'][i]
        aspirante.id_militar = pben['Número da ID. Militar'][i]
        aspirante.quarto_habilitacao = pben['Quarto/Habilitação'][i]
        aspirante.telefone = pben['Telefone de Contato'][i]
        aspirante.celular = pben['Celular de Contato'][i]
        aspirante.data_nascimento = pben['Data de Nascimento'][i]
        aspirante.sangue = pben['Tipo Sanguíneo +Fator RH'][i]
        aspirante.equipe = pben['Equipe'][i]
        aspirante.email = pben['E-mail'][i]
        aspirante.religiao = pben['Religião'][i]
        aspirante.cidade = pben['Cidade'][i]
        aspirante.estado = pben['Estado'][i]
        aspirante.bairro = pben['Bairro'][i]
        aspirante.endereco = pben['Endereço'][i]
        aspirante.cep = pben['CEP'][i]
        aspirante.nome_pai = pben['Nome do Pai'][i]
        aspirante.profissao_pai = pben['Profissão do Pai'][i]
        aspirante.forca_militar_pai = pben['Caso o Pai Seja Militar- Força Armada/Força Auxiliar'][i]
        aspirante.cargo_militar_pai = pben['Caso o Pai Seja Militar- Posto ou Graduação'][i]
        aspirante.nome_mae = pben['Nome da Mãe'][i]
        aspirante.profissao_mae = pben['Profissão da Mãe'][i]
        aspirante.forca_militar_mae = pben['Caso a Mãe Seja Militar- Força Armada/Força Auxiliar'][i]
        aspirante.cargo_militar_mae = pben['Caso a Mãe Seja Militar- Posto ou Graduação'][i]
        aspirante.adicional = pben['Descrição'][i]

        aspirantes.append(aspirante)
    
    return aspirantes

def busca_aspirante(aspirantes, valor_buscado):
    padrao_numero = '([0-9]{4})'
    padrao_im = '(IM-[0-9]{3})'
    padrao_fn = '(FN-[0-9]{3})'
    valor_buscado = valor_buscado.upper()

    if re.search(padrao_numero,valor_buscado) or re.search(padrao_im,valor_buscado) or re.search(padrao_fn,valor_buscado):
        for aspirante in aspirantes:
            if str(aspirante.numero_interno_atual) == str(valor_buscado):
                return aspirante
        return aspirante_nulo
    else:
        for aspirante in aspirantes:
            if aspirante.nome_guerra.upper() == str(valor_buscado).upper():
                return aspirante
        return aspirante_nulo
