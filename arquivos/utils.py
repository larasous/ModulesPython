def format_tam(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5
    
    if tamanho < kilo:
        txt = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        txt = 'K'
    elif tamanho < giga:
        tamanho /= mega
        txt = 'M'
    elif tamanho < tera:
        tamanho /= giga
        txt = 'G'
    elif tamanho < peta:
        tamanho /= tera
        txt = 'T'
    else:
        tamanho /= peta
        txt = 'P'
        
    tamanho = round(tamanho, 2)
    return f'{tamanho}{txt}'.replace('.', ',')