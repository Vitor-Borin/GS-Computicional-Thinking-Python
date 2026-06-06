import os
import math
import random
from datetime import datetime

# listas globais que guardam os dados enquanto o programa roda
camaras = []
leituras = []
alertas = []

# catalogos fixos da base AgroLunar - dados de referencia
# (4 listas com 20 itens cada, usadas no relatorio da base - opcao 7)
PLANTAS_HIDROPONICAS = [
    "alface", "rucula", "manjericao", "espinafre", "couve",
    "agriao", "cebolinha", "salsa", "coentro", "hortela",
    "morango", "tomate-cereja", "pimentao", "pepino", "acelga",
    "mostarda", "alecrim", "tomilho", "endivia", "almeirao"
]

TEMPERATURAS_HISTORICAS = [
    21.4, 22.0, 19.8, 23.1, 20.5, 24.3, 18.9, 22.7, 21.0, 23.8,
    20.1, 19.5, 22.2, 24.0, 21.7, 18.4, 23.5, 20.9, 22.9, 21.3
]

MODULOS_DISPONIVEIS = [
    "Modulo A - Setor 1", "Modulo A - Setor 2", "Modulo A - Setor 3", "Modulo A - Setor 4",
    "Modulo B - Setor 1", "Modulo B - Setor 2", "Modulo B - Setor 3", "Modulo B - Setor 4",
    "Modulo C - Setor 1", "Modulo C - Setor 2", "Modulo C - Setor 3", "Modulo C - Setor 4",
    "Modulo D - Setor 1", "Modulo D - Setor 2", "Modulo D - Setor 3", "Modulo D - Setor 4",
    "Estufa Externa 1", "Estufa Externa 2", "Laboratorio 1", "Laboratorio 2"
]

DIAGNOSTICOS_BASE = [
    "Bomba de agua operando normal", "Filtro de ar limpo", "Reservatorio cheio",
    "Painel solar a 98%", "Bateria carregada", "Sensor de luz calibrado",
    "Valvula de nutrientes ok", "Ventilacao ativa", "Umidade dentro da faixa",
    "Temperatura estavel", "pH da solucao em 6.2", "Condutividade ok",
    "Camera de inspecao online", "Link de telemetria ativo", "Backup de energia ok",
    "Dreno desobstruido", "Lampada LED 1 ok", "Lampada LED 2 ok",
    "Termostato responsivo", "Sistema geral nominal"
]


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def cabecalho(titulo):
    print("=" * 52)
    print(f"  {titulo}")
    print("=" * 52)


def ler_inteiro(mensagem, minimo, maximo):
    # le um numero inteiro do usuario com validacao usando try/except
    while True:
        entrada = input(mensagem).strip()
        try:
            numero = int(entrada)
        except ValueError:
            print(f"  Valor invalido. Digite um numero inteiro entre {minimo} e {maximo}.")
            continue

        if numero < minimo or numero > maximo:
            print(f"  Fora do intervalo. Digite entre {minimo} e {maximo}.")
            continue

        return numero


def media_lista(valores):
    # media simples dos valores de uma lista de numeros
    if len(valores) == 0:
        return 0

    soma = 0
    for v in valores:
        soma = soma + v
    return soma / len(valores)


def cadastrar_camara():
    # id sequencial baseado no tamanho atual da lista
    id_novo = len(camaras) + 1

    limpar_tela()
    cabecalho("Cadastrar Nova Camara de Cultivo")

    # escolha do tipo com validacao
    print()
    print("  Tipo de camara:")
    print("  1 - Lunar  (base Artemis / NASA)")
    print("  2 - Urbana (fazenda vertical terrestre)")
    print()

    tipo = ""
    while tipo == "":
        escolha = input("  Digite 1 ou 2: ").strip()
        if escolha == "1":
            tipo = "lunar"
        elif escolha == "2":
            tipo = "urbana"
        else:
            print("  Opcao invalida. Digite apenas 1 ou 2.")

    # nome da planta - vazio aceita o padrao alface
    print()
    planta = input("  Nome da planta (ENTER para 'alface'): ").strip()
    if planta == "":
        planta = "alface"

    # localizacao obrigatoria
    print()
    localizacao = ""
    while localizacao == "":
        localizacao = input("  Localizacao (ex: Modulo B - Setor 3): ").strip()
        if localizacao == "":
            print("  Localizacao nao pode ser vazia.")

    data_cadastro = datetime.now().strftime("%d/%m/%Y %H:%M")

    nova_camara = {
        "id": id_novo,
        "tipo": tipo,
        "planta": planta,
        "localizacao": localizacao,
        "data_cadastro": data_cadastro
    }

    camaras.append(nova_camara)

    # mostra resumo do que foi salvo
    print()
    print("=" * 52)
    print("  CAMARA CADASTRADA COM SUCESSO!")
    print("=" * 52)
    print(f"  ID         : {id_novo}")
    print(f"  Tipo       : {tipo.capitalize()}")
    print(f"  Planta     : {planta.capitalize()}")
    print(f"  Localizacao: {localizacao}")
    print(f"  Cadastro   : {data_cadastro}")
    print("=" * 52)


def consultar_status_interativo():
    limpar_tela()
    cabecalho("Consultar Status de Camara")

    # sem camaras nao tem o que consultar
    if len(camaras) == 0:
        print()
        print("  Nenhuma camara cadastrada ainda.")
        print("  Use a opcao 1 para cadastrar uma camara.")
        return

    # lista todas as camaras com indice visivel
    print()
    print("  Camaras cadastradas:")
    print()
    for i in range(len(camaras)):
        c = camaras[i]
        print(f"  [{i + 1}]  ID {c['id']}  |  {c['tipo'].capitalize():<7}  |  {c['planta'].capitalize():<12}  |  {c['localizacao']}")

    print()

    # validacao da escolha - so aceita numero dentro do range
    num = ler_inteiro(f"  Escolha uma camara (1 a {len(camaras)}): ", 1, len(camaras))
    camara = camaras[num - 1]

    # ranges calibrados pra cultivo de alface em hidroponico
    temperatura  = round(random.uniform(16.0, 28.0), 1)
    umidade_ar   = round(random.uniform(55.0, 85.0), 1)
    umidade_solo = round(random.uniform(60.0, 95.0), 1)
    luz          = int(random.uniform(150.0, 900.0))

    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    nova_leitura = {
        "id_camara": camara["id"],
        "timestamp": timestamp,
        "temperatura": temperatura,
        "umidade_ar": umidade_ar,
        "umidade_solo": umidade_solo,
        "luz": luz
    }

    leituras.append(nova_leitura)

    # exibe resultado
    limpar_tela()
    cabecalho(f"Status  |  Camara {camara['id']}  |  {camara['tipo'].capitalize()}")
    print()
    print(f"  Planta       : {camara['planta'].capitalize()}")
    print(f"  Localizacao  : {camara['localizacao']}")
    print(f"  Leitura em   : {timestamp}")
    print()
    print("  " + "-" * 36)
    print(f"  {'Sensor':<18} {'Valor':>8}  {'Unidade'}")
    print("  " + "-" * 36)
    print(f"  {'Temperatura':<18} {temperatura:>8.1f}  C")
    print(f"  {'Umidade do ar':<18} {umidade_ar:>8.1f}  %")
    print(f"  {'Umidade solo':<18} {umidade_solo:>8.1f}  %")
    print(f"  {'Luminosidade':<18} {luz:>8}  lux")
    print("  " + "-" * 36)
    print()
    print("  Leitura registrada no historico.")


def status_iluminacao(lux, limiar):
    # decide se a hora precisa ou nao de luz artificial
    if lux < limiar:
        return "[ LUZ ARTIFICIAL ]"
    else:
        return "  luz natural"


def calcular_cronograma_iluminacao():
    # L(h) = amplitude * cos(2pi * (h - pico) / periodo) + base
    LIMIAR_LUX = 200  # lux minimo para alface crescer

    limpar_tela()
    cabecalho("Cronograma de Iluminacao Artificial")

    print()
    print("  Tipo de ambiente:")
    print("  1 - Terra  (ciclo de 24 horas)")
    print("  2 - Lunar  (ciclo de 708 horas / 14,7 dias)")
    print()

    tipo = ""
    while tipo == "":
        escolha = input("  Digite 1 ou 2: ").strip()
        if escolha == "1":
            tipo = "terra"
        elif escolha == "2":
            tipo = "lunar"
        else:
            print("  Opcao invalida. Digite 1 ou 2.")

    limpar_tela()

    if tipo == "terra":
        # pico ao meio-dia (h=12), zero a meia-noite (h=0 e h=24)
        amplitude  = 600
        nivel_base = 600
        periodo    = 24
        pico       = 12

        cabecalho("Cronograma  |  Terra  |  Ciclo 24h")
        print()
        print(f"  L(h) = {amplitude} * cos(2pi * (h - {pico}) / {periodo}) + {nivel_base}")
        print(f"  Limiar para alface: {LIMIAR_LUX} lux")
        print()
        print("  " + "-" * 44)
        print(f"  {'Hora':<8} {'Lux natural':>11}  Iluminacao")
        print("  " + "-" * 44)

        horas_artificiais = []

        for h in range(24):
            lux = amplitude * math.cos(2 * math.pi * (h - pico) / periodo) + nivel_base
            lux = max(0, int(round(lux)))
            status = status_iluminacao(lux, LIMIAR_LUX)

            if lux < LIMIAR_LUX:
                horas_artificiais.append(h)

            print(f"  {h:02d}:00   {lux:>9} lux  {status}")

        print("  " + "-" * 44)
        print()

        if len(horas_artificiais) == 0:
            print("  Luz natural suficiente o dia todo.")
        else:
            lista = ", ".join([f"{h:02d}:00" for h in horas_artificiais])
            print(f"  Luz artificial em {len(horas_artificiais)} horas/dia")
            print(f"  Horarios: {lista}")

    else:
        # dia lunar = 352h de luz continua, noite lunar = 352h de escuridao total
        print("  Em qual fase do ciclo lunar a base esta?")
        print()
        print("  1 - Dia lunar  (14,7 dias de luz solar direta)")
        print("  2 - Noite lunar (14,7 dias de escuridao total)")
        print()

        fase = ""
        while fase == "":
            escolha_fase = input("  Digite 1 ou 2: ").strip()
            if escolha_fase == "1":
                fase = "dia"
            elif escolha_fase == "2":
                fase = "noite"
            else:
                print("  Opcao invalida. Digite 1 ou 2.")

        limpar_tela()

        if fase == "noite":
            cabecalho("Cronograma  |  Lunar  |  Noite Lunar")
            print()
            print("  Escuridao total por 14,7 dias terrestres.")
            print(f"  Limiar para alface: {LIMIAR_LUX} lux")
            print()
            print("  " + "-" * 44)
            print(f"  {'Hora':<8} {'Lux natural':>11}  Iluminacao")
            print("  " + "-" * 44)

            for h in range(24):
                print(f"  {h:02d}:00   {'0':>9} lux  [ LUZ ARTIFICIAL ]")

            print("  " + "-" * 44)
            print()
            print("  Luz artificial necessaria: 24 horas por dia.")
            print("  Custo energetico critico. Priorizar baterias e paineis.")

        else:
            # dia lunar: periodo de 708h, pico no centro do ciclo (t=354)
            # em apenas 24h o angulo avanca ~12 graus -> variacao minima de lux
            amplitude  = 800
            nivel_base = 800
            periodo    = 708
            pico       = 354

            cabecalho("Cronograma  |  Lunar  |  Dia Lunar")
            print()
            print(f"  L(t) = {amplitude} * cos(2pi * (t - {pico}) / {periodo}) + {nivel_base}")
            print(f"  Limiar para alface: {LIMIAR_LUX} lux")
            print(f"  Janela de 24h a partir do meio do dia lunar (t=354)")
            print()
            print("  " + "-" * 44)
            print(f"  {'Hora':<8} {'Lux natural':>11}  Iluminacao")
            print("  " + "-" * 44)

            horas_artificiais = []

            for h in range(24):
                # t comeca no pico do dia lunar e avanca hora a hora
                t = pico + h
                lux = amplitude * math.cos(2 * math.pi * (t - pico) / periodo) + nivel_base
                lux = max(0, int(round(lux)))
                status = status_iluminacao(lux, LIMIAR_LUX)

                if lux < LIMIAR_LUX:
                    horas_artificiais.append(h)

                print(f"  {h:02d}:00   {lux:>9} lux  {status}")

            print("  " + "-" * 44)
            print()

            if len(horas_artificiais) == 0:
                print("  Luz solar suficiente em todas as horas.")
                print("  Ciclo lunar e lento: 24h representa ~12 graus do ciclo.")
            else:
                lista = ", ".join([f"{h:02d}:00" for h in horas_artificiais])
                print(f"  Luz artificial em {len(horas_artificiais)} horas/dia")
                print(f"  Horarios: {lista}")


def criar_alerta(leitura, sensor, problema):
    # monta o dicionario do alerta com base na leitura original
    return {
        "id_camara": leitura["id_camara"],
        "timestamp": leitura["timestamp"],
        "sensor": sensor,
        "valor": leitura[sensor],
        "problema": problema
    }


def gerar_alerta():
    # ranges aceitos para cada sensor (alface hidroponico)
    TEMP_MIN = 18
    TEMP_MAX = 28
    UMID_MIN = 50
    UMID_MAX = 90
    LUZ_MIN  = 200
    LUZ_MAX  = 1000

    limpar_tela()
    cabecalho("Gerar Alertas de Falha")

    if len(leituras) == 0:
        print()
        print("  Nenhuma leitura registrada ainda.")
        print("  Use a opcao 2 para gerar leituras antes.")
        return

    # zera a lista pra re-processar todas as leituras do zero
    alertas.clear()

    for leitura in leituras:
        temp      = leitura["temperatura"]
        umid_ar   = leitura["umidade_ar"]
        umid_solo = leitura["umidade_solo"]
        luz       = leitura["luz"]

        # temperatura
        if temp < TEMP_MIN:
            desc = f"Temperatura baixa ({temp} C) - minimo {TEMP_MIN} C"
            alertas.append(criar_alerta(leitura, "temperatura", desc))
        elif temp > TEMP_MAX:
            desc = f"Temperatura alta ({temp} C) - maximo {TEMP_MAX} C"
            alertas.append(criar_alerta(leitura, "temperatura", desc))

        # umidade do ar
        if umid_ar < UMID_MIN:
            desc = f"Umidade do ar baixa ({umid_ar}%) - minimo {UMID_MIN}%"
            alertas.append(criar_alerta(leitura, "umidade_ar", desc))
        elif umid_ar > UMID_MAX:
            desc = f"Umidade do ar alta ({umid_ar}%) - maximo {UMID_MAX}%"
            alertas.append(criar_alerta(leitura, "umidade_ar", desc))

        # umidade do solo
        if umid_solo < UMID_MIN:
            desc = f"Umidade do solo baixa ({umid_solo}%) - minimo {UMID_MIN}%"
            alertas.append(criar_alerta(leitura, "umidade_solo", desc))
        elif umid_solo > UMID_MAX:
            desc = f"Umidade do solo alta ({umid_solo}%) - maximo {UMID_MAX}%"
            alertas.append(criar_alerta(leitura, "umidade_solo", desc))

        # luminosidade
        if luz < LUZ_MIN:
            desc = f"Luz baixa ({luz} lux) - minimo {LUZ_MIN} lux"
            alertas.append(criar_alerta(leitura, "luz", desc))
        elif luz > LUZ_MAX:
            desc = f"Luz alta ({luz} lux) - maximo {LUZ_MAX} lux"
            alertas.append(criar_alerta(leitura, "luz", desc))

    # resumo geral
    print()
    print(f"  Leituras analisadas : {len(leituras)}")
    print(f"  Alertas gerados     : {len(alertas)}")
    print()

    if len(alertas) == 0:
        print("  Nenhum sensor fora do range esperado.")
        print("  Todas as camaras operando dentro dos parametros.")
        return

    # tabela com os alertas encontrados
    print("  " + "-" * 60)
    print(f"  {'Camara':<7} {'Sensor':<14} {'Valor':>7}  Descricao")
    print("  " + "-" * 60)

    for a in alertas:
        valor_str = f"{a['valor']}"
        print(f"  {a['id_camara']:<7} {a['sensor']:<14} {valor_str:>7}  {a['problema']}")

    print("  " + "-" * 60)


def listar_historico():
    limpar_tela()
    cabecalho("Historico de Leituras")

    if len(leituras) == 0:
        print()
        print("  Nenhuma leitura registrada ainda.")
        print("  Use a opcao 2 para gerar leituras.")
        return

    # conta quantas camaras diferentes ja foram lidas
    ids_unicos = []
    for l in leituras:
        if l["id_camara"] not in ids_unicos:
            ids_unicos.append(l["id_camara"])

    print()
    print(f"  Total de leituras    : {len(leituras)}")
    print(f"  Camaras com leitura  : {len(ids_unicos)}")
    print(f"  Alertas pendentes    : {len(alertas)}")
    print()

    # tabela ascii com cabecalho e linhas de dados
    linha_sep = "  +-----+---------------------+--------+--------+--------+--------+"

    print(linha_sep)
    print(f"  | {'ID':^3} | {'Timestamp':^19} | {'Temp':^6} | {'UmAr':^6} | {'UmSo':^6} | {'Luz':^6} |")
    print(linha_sep)

    for l in leituras:
        id_str   = str(l["id_camara"])
        temp_str = f"{l['temperatura']:.1f}C"
        ar_str   = f"{l['umidade_ar']:.1f}%"
        solo_str = f"{l['umidade_solo']:.1f}%"
        luz_str  = f"{l['luz']}"

        print(f"  | {id_str:^3} | {l['timestamp']:^19} | {temp_str:^6} | {ar_str:^6} | {solo_str:^6} | {luz_str:^6} |")

    print(linha_sep)


def mostrar_sobre():
    limpar_tela()
    cabecalho("Sobre o AgroLunar")

    # descricao em 5 linhas (exigencia do briefing)
    print()
    print("  AgroLunar e um sistema autonomo de cultivo hidroponico para a base")
    print("  lunar do programa Artemis (alimento custa US$ 1 mi/kg, latencia")
    print("  Lua-Terra de 2,5s). Sensores ESP32 controlam temperatura, umidade")
    print("  e luz localmente; este programa Python simula o lado de monitoramento.")
    print("  A mesma engenharia atende fazendas verticais urbanas (95% menos agua).")
    print()
    print("  " + "-" * 48)
    print("  Equipe FIAP - Global Solution 2026.1")
    print("    Robert Josino  - RM571622")
    print("    Ryan Maick     - RM573051")
    print("    Vitor Borin    - RM573194")


def relatorio_base():
    limpar_tela()
    cabecalho("Catalogo e Relatorio da Base")

    # resumo das 4 listas de referencia da base
    print()
    print(f"  Plantas catalogadas    : {len(PLANTAS_HIDROPONICAS)}")
    print(f"  Modulos disponiveis    : {len(MODULOS_DISPONIVEIS)}")
    print(f"  Leituras historicas    : {len(TEMPERATURAS_HISTORICAS)}")
    print(f"  Itens de diagnostico   : {len(DIAGNOSTICOS_BASE)}")
    print()

    # estatisticas das temperaturas historicas (manipulacao de lista por funcao)
    media = media_lista(TEMPERATURAS_HISTORICAS)
    maior = max(TEMPERATURAS_HISTORICAS)
    menor = min(TEMPERATURAS_HISTORICAS)

    print("  Temperaturas historicas da base (C):")
    print(f"    Media: {media:.1f}    Maxima: {maior:.1f}    Minima: {menor:.1f}")
    print()

    # quantidade a exibir - entrada validada com try/except (via ler_inteiro)
    total = len(PLANTAS_HIDROPONICAS)
    print(f"  Quantas plantas do catalogo deseja ver? (1 a {total})")
    quantidade = ler_inteiro("  Quantidade: ", 1, total)

    print()
    print("  Catalogo de plantas hidroponicas:")
    for i in range(quantidade):
        print(f"    {i + 1:>2}. {PLANTAS_HIDROPONICAS[i].capitalize()}")

    print()
    # sorteia um item de diagnostico da base pra simular uma checagem
    diagnostico = random.choice(DIAGNOSTICOS_BASE)
    print(f"  Checagem aleatoria da base: {diagnostico}")


def menu_principal():
    limpar_tela()
    cabecalho("AgroLunar - Sistema de Cultivo Hidroponico")
    print()
    print("  1 - Cadastrar nova camara de cultivo")
    print("  2 - Consultar status de uma camara")
    print("  3 - Calcular cronograma de iluminacao")
    print("  4 - Gerar alerta de falha")
    print("  5 - Listar historico de leituras")
    print("  6 - Sobre o AgroLunar")
    print("  7 - Catalogo e relatorio da base")
    print("  0 - Sair")
    print()
    print("=" * 52)
    opcao = input("  Escolha uma opcao: ").strip()
    return opcao


def main():
    while True:
        opcao = menu_principal()

        match opcao:
            case "1":
                cadastrar_camara()
            case "2":
                consultar_status_interativo()
            case "3":
                calcular_cronograma_iluminacao()
            case "4":
                gerar_alerta()
            case "5":
                listar_historico()
            case "6":
                mostrar_sobre()
            case "7":
                relatorio_base()
            case "0":
                print("\n  Encerrando AgroLunar. Boa sorte na missao.")
                break
            case _:
                print("\n  Opcao invalida. Digite um numero do menu.")

        input("\n  Pressione ENTER para voltar ao menu...")


if __name__ == "__main__":
    main()
