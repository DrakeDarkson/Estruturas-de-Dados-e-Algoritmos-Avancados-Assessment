def cobertura_gulosa(lojas, armazens):
    cobertura_final = []
    lojas_nao_cobertas = set(lojas)
    
    while lojas_nao_cobertas:
        melhor_armazem = max(armazens, key=lambda a: len(armazens[a] & lojas_nao_cobertas))
        cobertura_final.append(melhor_armazem)
        lojas_nao_cobertas -= armazens[melhor_armazem]
    
    return cobertura_final

lojas = {"L1", "L2", "L3", "L4", "L5", "L6", "L7"}
armazens = {
    "A1": {"L1", "L2", "L3"},
    "A2": {"L2", "L4", "L5"},
    "A3": {"L3", "L5", "L6"},
    "A4": {"L6", "L7"}
}

resultado = cobertura_gulosa(lojas, armazens)
print("Armazéns escolhidos:", resultado)
