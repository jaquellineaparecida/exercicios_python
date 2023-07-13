linguagem = input("Qual linguagem de programação você gostaria de aprender? ")

match linguagem:
    case "Javascript": 
        print("Você poderia ser um desenvolvedor web")
    
    case "Python":
        print("Você poderia ser um cientista de dados")
    
    case "PHP":
        print("Você pode se tornar um dev back-end")
    
    case "Java":
        print("Você pode ser um dev mobile")
    
    case "Solid":
        print("Você pode se tornar um dev block-chain")

    case _:
        print("Não conheço essa linguagem")
