def get_prep():
    with open('prep.txt') as f:
        return f.read().split('\n')


def porc_prep(parrafo):
    prep = get_prep()
    n_prep = 0
    for pal in parrafo.split():
        if pal in prep:
            n_prep = n_prep + 1
    return n_prep / len(parrafo.split())


def lon_prom_pal(parrafo):
    num_letras = sum([len(x) for x in parrafo.split()])
    num_pal = len(parrafo.split())
    return num_letras / num_pal


def lon_prom_ora(parrafo):
    num_ora = len(parrafo.split('.'))
    num_pal = len(parrafo.split())
    return num_pal / num_ora


def porc_punt(parrafo):
    signos = '.,;:?!"'
    num_p = 0
    for c in parrafo:
        if c in signos:
            num_p = num_p + 1
    return num_p / len(parrafo)
