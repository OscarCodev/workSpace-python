def main():
    dollars = dollars_a_float(input("¿Cuánto fue la comida ? "))
    porcentaje = porcentaje_a_float(input("¿Qué porcentaje le gustaria dejar de propina? "))
    propina = dollars * porcentaje
    print(f"Deja ${propina:.2f}")

def dollars_a_float(d):
    return float(d.replace("$", ""))


def porcentaje_a_float(p):
    return float(p.replace("%", "")) * 0.01

main()