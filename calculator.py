
def calculate(e):
    try:
        if "^" in e:
            e = e.replace("^", "**")
        a = eval(e)
        return str(a)
    
    except ZeroDivisionError:
        return "Impossible"
    except SyntaxError:
        raise SyntaxError("Erreur de syntaxe dans l'expression ou l'expression n'est pas un calcul valide")
    except Exception as ex:
        raise SyntaxError("L'expression saisie n'est pas un calcul")