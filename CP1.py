def tokenizar(frase):
    frase = frase.lower()
    for pontuacao in [',', '.', '!', '?', ';', ':', '"', "'", '(', ')', '[', ']']:
        frase = frase.replace(pontuacao, '')
    palavras = frase.split()
    return palavras

def extrair_radical(palavra):
    sufixos_comuns = ["ar", "er", "ir", "ando", "endo", "indo", "ei", "ou", "ava", "ado", "ida", "ido", "ais", "eis", "éis", "ia", "am", "em", "arem", "erem", "irem", "ando", "endo", "indo", "ou", "ar", "er", "ir", "ei"]
    for sufixo in sufixos_comuns:
        if palavra.endswith(sufixo):
            return palavra[:-len(sufixo)]
    return palavra

def preparar_lista_sentimentos(lista):
    return [extrair_radical(palavra) for palavra in lista]

def analise_sentimento(frase, palavras_positivas, palavras_negativas):
    palavras = tokenizar(frase)
    radicais_frase = [extrair_radical(palavra) for palavra in palavras]

    # Adiciona lógica para inverter sentimento após "não" até pontuação
    pontuacoes = [',', '.', '!', '?', ';', ':']
    invertido = False
    score = 0

    for palavra in radicais_frase:
        if palavra == 'não':
            invertido = True
        elif any(pontuacao in palavra for pontuacao in pontuacoes):  # Verifica se a palavra contém pontuação
            invertido = False
        
        if palavra in palavras_positivas:
            score += -1 if invertido else 1
        elif palavra in palavras_negativas:
            score += 1 if invertido else -1
    
    if score > 0:
        return "Sentimento positivo"
    elif score < 0:
        return "Sentimento negativo"
    else:
        return "Sentimento neutro"
    
def inserir_frase():
    frase_invalida = True
    frase_usuario = ''
    while (frase_invalida):
        frase_usuario = input("Digite uma frase: ")
        frase_invalida = validar_frase_padrao(frase_usuario)
    return frase_usuario

def validar_frase_padrao(frase):
    palavras_compostas = [
        "água de coco", "pé de moleque", "banho de mar", "cão de guarda", "fim de semana",
        "pão de queijo", "queijo fresco", "copo d'água", "banho de sol", "cachorro quente",
        "guarda-chuva", "beija-flor", "cor-de-rosa", "cabeça-dura", "pão-duro",
        "deus-nos-acuda", "mão de obra", "bem-vindo", "passatempo", "ponta-pé",
        "coração partido", "cavalo-marinho", "corpo-a-corpo", "luz do sol", "pé-de-meia",
        "papel-manteiga", "passa-tempo", "meio-dia", "falta de ar", "fim de jogo",
        "mesa de jantar", "livro de leitura", "sol de verão", "chuva de verão",
        "caminho de ferro", "barco a vapor", "salto de esqui", "caminho de volta",
        "meio-fio", "sala de estar", "amor-próprio", "louva-a-deus", "louva-a-Deus",
        "livro de capa dura", "sala de aula", "pote de vidro", "laranja-limão",
        "quarto de dormir", "amor de mãe", "laranja madura", "água salgada",
        "pescoço de cisne", "sombra de árvore", "casa de campo", "peixe espada",
        "frente de batalha", "bola de futebol", "caixa de correio", "mundo de fantasia",
        "céu estrelado", "saco de dormir", "gota d'água", "guarda florestal",
        "cabo de guerra", "sol de inverno", "pássaro azul", "pato-real", "boca de fumo",
        "caminho de pedra", "papel de parede", "sol de primavera", "corrente de ar",
        "cachorro-quente", "banho-maria", "janela de vidro", "cor de laranja", "meia-noite",
        "casa de banho", "dor de cabeça", "boca de sino", "pescoço de galinha",
        "terra de ninguém", "saco de pancadas", "dente de leão", "fogo de artifício",
        "bola de neve", "boca de lobo", "caixa de ferramentas", "caminho-de-ferro",
        "folha de papel", "fio de cabelo", "gota d'água", "mão-de-obra", "ponto de vista",
        "pé de meia", "terra de ninguém", "gota d'água", "lua de mel", "linha de frente",
        "cavalo de batalha", "peixe-boi", "gato-pingado", "mão de obra", "ponto de vista"
    ]
    lista_stopwords = [
        "de", "a", "o", "que", "e", "é", "do", "da", "em", "um", "para", "com", "não", 
        "uma", "os", "no", "se", "na", "por", "mais", "as", "dos", "como", "mas", 
        "foi", "ao", "ele", "das", "tem", "à", "seu", "sua", "ou", "ser", "quando", 
        "muito", "há", "nos", "já", "está", "eu", "também", "só", "pelo", "pela", 
        "até", "isso", "ela", "entre", "era", "depois", "sem", "mesmo", "aos", 
        "ter", "seus", "quem", "nas", "me", "esse", "eles", "estão", "você", "tinha", 
        "foram", "essa", "num", "nem", "suas", "meu", "às", "minha", "têm", "numa", 
        "pelos", "elas", "havia", "seja", "qual", "será", "nós", "tenho", "lhe", 
        "deles", "essas", "esses", "pelas", "este", "fosse", "dele", "tu", "te", 
        "vocês", "vos", "lhes", "meus", "minhas", "teu", "tua", "teus", "tuas", 
        "nosso", "nossa", "nossos", "nossas", "dela", "delas", "esta", "estes", 
        "estas", "aquele", "aquela", "aqueles", "aquelas", "isto", "aquilo", "estou", 
        "está", "estamos", "estão", "estive", "esteve", "estivemos", "estiveram", 
        "estava", "estávamos", "estavam", "estivera", "estivéramos", "esteja", 
        "estejamos", "estejam", "estivesse", "estivéssemos", "estivessem", "estiver", 
        "estivermos", "estiverem", "hei", "há", "havemos", "hão", "houve", "houvemos", 
        "houveram", "houvera", "houvéramos", "haja", "hajamos", "hajam", "houvesse", 
        "houvéssemos", "houvessem", "houver", "houvermos", "houverem", "houverei", 
        "houverá", "houveremos", "houverão", "houveria", "houveríamos", "houveriam", 
        "sou", "somos", "são", "era", "éramos", "eram", "fui", "foi", "fomos", 
        "foram", "fora", "fôramos", "seja", "sejamos", "sejam", "fosse", "fôssemos", 
        "fossem", "for", "formos", "forem", "serei", "será", "seremos", "serão", 
        "seria", "seríamos", "seriam", "tenho", "tem", "temos", "tém", "tinha", 
        "tínhamos", "tinham", "tive", "teve", "tivemos", "tiveram", "tivera", 
        "tivéramos", "tenha", "tenhamos", "tenham", "tivesse", "tivéssemos", 
        "tivessem", "tiver", "tivermos", "tiverem", "terei", "terá", "teremos", 
        "terão", "teria", "teríamos", "teriam", "a", "ao", "aos", "às", "ainda", 
        "algum", "alguma", "alguns", "algumas", "ali", "além", "ambos", "ante", 
        "antes", "ao", "aos", "após", "aquela", "aquelas", "aquele", "aqueles", 
        "aquilo", "as", "até", "atrás", "através", "baixo", "bastante", "bem", 
        "boa", "bom", "breve", "cada", "caminho", "catorze", "cedo", "cento", 
        "certamente", "certeza", "cima", "cinco", "coisa", "com", "como", "comprido", 
        "conhecido", "conselho", "contra", "corrente", "custa", "da", "daquela", 
        "daquele", "dar", "das", "de", "debaixo", "demais", "dentro", "depois", 
        "desde", "dessa", "desse", "desta", "deste", "deve", "devem", "deverá", 
        "dez", "dezanove", "dezasseis", "dezassete", "dezoito", "dia", "diante", 
        "direita", "diz", "dizem", "dizer", "do", "dois", "dos", "doze", "duas", 
        "dúvida", "e", "é", "ela", "elas", "ele", "eles", "em", "embora", "enquanto", 
        "então", "entre", "era", "essa", "essas", "esse", "esses", "esta", "está", 
        "estado", "estar", "estará", "estas", "este", "estes", "esteve", "estive", 
        "estivemos", "estiveram", "estivera", "estivéramos", "estivesse", 
        "estivéssemos", "estivessem", "estiver", "estivermos", "estiverem", "eu", 
        "exemplo", "faço", "falta", "fará", "favor", "faz", "fazeis", "fazem", 
        "fazemos", "fazer", "fazes", "fez", "fim", "final", "foi", "fomos", "for", 
        "fora", "foram", "forma", "foste", "fostes", "fui", "geral", "grande", 
        "grandes", "grupo", "há", "hoje", "hora", "horas", "isso", "isto", "já", 
        "lá", "lado", "local", "logo", "longe", "lugar", "maior", "maioria", "mais", 
        "mal", "mas", "máximo", "me", "meio", "menor", "menos", "mês", "meses", 
        "mesmo", "meu", "meus", "mil", "minha", "minhas", "momento", "muito", 
        "muitos", "na", "nada", "não", "naquela", "naquele", "nas", "nem", "nenhuma", 
        "nessa", "nesse", "nesta", "neste", "nível", "no", "noite", "nome", "nos", 
        "nós", "nossa", "nossas", "nosso", "nossos", "nova", "novas", "nove", 
        "novo", "novos", "num", "numa", "número", "nunca", "o", "obra", "obrigada", 
        "obrigado", "oitava", "oitavo", "oito", "onde", "ontem", "onze", "os", 
        "ou", "outra", "outras", "outro", "outros", "para", "parece", "parte", 
        "partir", "paucas", "pela", "pelas", "pelo", "pelos", "pequena", "perto", 
        "pessoal", "pessoas", "pode", "pôde", "podem", "poder", "poderá", "podia", 
        "põe", "põem", "pois", "ponto", "pontos", "por", "porém", "porque", 
        "porquê", "posição", "possível", "possivelmente", "posso", "pouca", "pouco", 
        "poucos", "primeira", "primeiras", "primeiro", "primeiros", "própria", 
        "próprias", "próprio", "próprios", "próxima", "próximas", "próximo", 
        "próximos", "pude", "quáis", "qual", "quando", "quanto", "quarta", "quarto", 
        "quatro", "que", "quê", "quem", "quer", "quereis", "querem", "queremas", 
        "queres", "quero", "questão", "quinta", "quinto", "quinze", "relação", 
        "sabe", "sabem", "são", "se", "segunda", "segundo", "sei", "seis", "sem", 
        "sempre", "ser", "será", "serão", "sete", "sétima", "sétimo", "seu", "seus", 
        "sexta", "sexto", "si", "sido", "sistema", "sob", "sobre", "sois", "somos", 
        "sou", "sua", "suas", "tal", "talvez", "também", "tanta", "tão", "tarde", 
        "te", "tem", "têm", "temos", "tendes", "tendo", "tenho", "tens", "tentar", 
        "tentaram", "tentarão", "tentaremos", "tentas", "tentaste", "tentas", 
        "tente", "tentei", "tentemos", "tentou", "ter", "terá", "terão", "terceira", 
        "terceiro", "terei", "teremos", "teria", "teriam", "teríamos", "teu", "teus", 
        "teve", "tinha", "tinham", "tipo", "tive", "tivemos", "tiveram", "tivera", 
        "tivéramos", "tiverem", "tivermos", "tivesse", "tivessem", "tiveste", 
        "tivestes", "todos", "trabalhar", "trabalho", "três", "treze", "tu", "tua", 
        "tuas", "tudo", "um", "uma", "umas", "uns", "vai", "vais", "vamos", "van", 
        "vão", "vários", "vem", "vêm", "vens", "ver", "vez", "vezes", "viagem", 
        "vindo", "vinte", "você", "vocês", "vos", "vós", "vossa", "vossas", "vosso", 
        "vossos", "zero"
    ]
    lista_palavras = frase.split()
    lista_palavras_sem_stopwords = [palavra for palavra in lista_palavras if palavra.lower() not in lista_stopwords]
    frase_sem_espaco = frase.replace(" ", "")

    if frase == "":
        print("Frase vazia, por favor, insira uma frase valida")
        return True
    elif frase_sem_espaco.isdigit():
        print("Frase está com numeros somente")
        return True
    elif len(lista_palavras) <= 1:
        print("Frase com nenhuma ou somente uma palavra, por favor, insira uma frase valida")
        return True
    elif len(lista_palavras_sem_stopwords) < 1:
        print("Frase com nenhuma ou somente uma palavra, por favor, insira uma frase valida")
        return True
    elif frase in palavras_compostas:
        print("Frase com nenhuma ou somente uma palavra, por favor, insira uma frase valida")
        return True
    else:
        return False
    
def main():
    # Listas originais de palavras
    lista_palavras_positivas = [
        "feliz", "alegria", "amor", "esperança", "gratidão",
        "maravilhoso", "excelente", "perfeito", "brilhante", "incrível",
        "fantástico", "positivo", "sorridente", "bem-sucedido", "vitória",
        "triunfo", "encantador", "otimista", "divertido", "satisfação",
        "sucesso", "ganhar", "bonito", "melhor", "louvor",
        "agradável", "abençoado", "entusiasmado", "vibrante", "radiante",
        "paz", "contente", "prazer", "animado", "estimulante",
        "rico", "saudável", "forte", "liberdade", "inovador",
        "genial", "gênio", "mágico", "milagre", "sonho",
        "paixão", "vivaz", "energia", "energético", "revigorante",
        "curativo", "curar", "herói", "heroico", "bravo",
        "resiliente", "resiliência", "prosperidade", "florescer", "líder",
        "liderança", "inspirador", "inspiração", "motivador", "motivação",
        "amizade", "amigo", "harmonia", "harmonioso", "euforia",
        "eufórico", "fé", "glória", "glorioso", "honra",
        "honrado", "luxo", "luxuoso", "majestoso", "nobres",
        "nobreza", "orgulho", "orgulhoso", "paradisíaco", "paraíso",
        "prestígio", "prestigiado", "proeminente", "sereno", "serenidade",
        "tranquilidade", "tranquilo", "unidade", "único", "valioso", "gostar", "adorar", "otimo"
    ]

    lista_palavras_negativas = [
        "triste", "depressão", "ódio", "medo", "ansiedade",
        "raiva", "frustração", "desapontamento", "dor", "sofrimento",
        "desespero", "desesperança", "solidão", "mágoa", "rejeição",
        "fracasso", "derrota", "insegurança", "preocupação", "ciúme",
        "inveja", "pesar", "culpa", "vergonha", "desgosto",
        "amargura", "rancor", "hostilidade", "irritação", "nervosismo",
        "tensão", "estresse", "aflição", "agonia", "alarma",
        "perigo", "risco", "ameaça", "pânico", "horror",
        "terror", "catástrofe", "desastre", "crise", "urgência",
        "caos", "confusão", "problema", "dificuldade", "obstáculo",
        "barreira", "limitação", "restrição", "enfermidade", "doença",
        "lesão", "ferimento", "prejuízo", "perda", "ruína",
        "destruição", "danos", "corrupção", "decadência", "declínio",
        "desvantagem", "desfavor", "desânimo", "apatia", "indiferença",
        "negligência", "abandono", "abuso", "violência", "crueldade",
        "tortura", "opressão", "perseguição", "discriminação", "injustiça",
        "desigualdade", "pobreza", "miséria", "fome", "sede",
        "exaustão", "cansaço", "fadiga", "sonolência", "desorientação",
        "confusão", "dúvida", "incerteza", "vulnerabilidade", "fragilidade",
        "desilusão", "ceticismo", "pessimismo", "cinismo", "derrotismo"
    ]

    # Preparar listas de palavras com radicais
    palavras_positivas_radicais = preparar_lista_sentimentos(lista_palavras_positivas)
    palavras_negativas_radicais = preparar_lista_sentimentos(lista_palavras_negativas)

    frase_usuario = inserir_frase()

    # Análise de Sentimento
    sentimento = analise_sentimento(frase_usuario, palavras_positivas_radicais, palavras_negativas_radicais)
    print("Análise de Sentimento:", sentimento)

main()