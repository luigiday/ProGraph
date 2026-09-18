
def calculate(e):
    try:
        a = eval(e)
        print(a)
    except ZeroDivisionError:
        print("Impossible")
    except SyntaxError:
        print("Erreur de syntaxe")
    except Exception as ex:
        print("Pas un calcul")
    


e = input("Expression : ")
calculate(e)