monedas = 0
eleccion = int(input("hey mark, hace tiempo que no nos vemos, que tal ha ido todo?   "))
if eleccion == 1:
    eleccion = int(input("y que tal con los estudios?"))
    if eleccion == 2:
        print("bien tio")
        eleccion = int(input(" quieres monedas gratis?   "))
        if eleccion == 1:
            monedas = monedas + 100
            print("has ganado", monedas, "monedas")
    
else:
    print("mark?")
    eleccion2 = int(input("estas dormido mark?" ))
    if eleccion2 == 1:
        print(" si perdon jajaja")
    else:
        print("MARK")
