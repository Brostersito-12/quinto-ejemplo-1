while True:
    print("""Bienvenido a mi sistema de circunferencia

    ███████╗██╗     ███████╗██╗  ██╗██╗   ██╗██████╗ ███████╗██╗  ██╗██╗   ██╗
    ██╔════╝██║     ██╔════╝╚██╗██╔╝╚██╗ ██╔╝██╔══██╗██╔════╝╚██╗██╔╝╚██╗ ██╔╝
    █████╗  ██║     █████╗   ╚███╔╝  ╚████╔╝ ██████╔╝█████╗   ╚███╔╝  ╚████╔╝ 
    ██╔══╝  ██║     ██╔══╝   ██╔██╗   ╚██╔╝  ██╔═══╝ ██╔══╝   ██╔██╗   ╚██╔╝  
    ██║     ███████╗███████╗██╔╝ ██╗   ██║   ██║     ███████╗██╔╝ ██╗   ██║   
    ╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   

                    ████████╗███████╗ ██████╗██╗  ██╗
                    ╚══██╔══╝██╔════╝██╔════╝██║  ██║
                       ██║   █████╗  ██║     ███████║
                       ██║   ██╔══╝  ██║     ██╔══██║
                       ██║   ███████╗╚██████╗██║  ██║
                       ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝

    """)
    try:
        area = 0
        perimetro = 0
        print("Área y perimetro de la circunferencia")
        print("=====================================")
        print()
        radio = float(input("Ingrese el radio: "))
        area = 3.14 * radio * radio
        perimetro = 2 * 3.14 * radio
        print("Mostrando resultados")
        print("Area:   ", area.__round__(2))
        print("Perimetro: ", perimetro.__round__(2))
        
        while True:
            op = input("¿Desea continuar? (s/n): ")
            if op == "s" or op == "S":
                break
            elif op == "n" or op == "N":
                print()
                print("usted ha salido del sistema, gracias por usarlo")
                print("vistanos en www.flexypexytech.com")
                break
            else:
                print("Opción no válida, intente de nuevo")
    except:
        print("Ocurrió un error, intente de nuevo")