 # Méthode pour l'opération d'addition
def addition(a, b):
    return a + b

# Méthode pour l'opération de soustraction
def soustraction(a, b):
    return a - b

# Méthode pour l'opération de multiplication
def multiplication(a, b):
    return a * b

 # Méthode pour l'opération de division
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur"

def calculatrice():
    while True:
        try:
            print("\nOpérations disponibles:")
            print("1. Addition")
            print("2. Soustraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Quitter")

 # Sélection de l'opération par l'utilisateur
            choix = int(input("Choisissez une opération (1/2/3/4/5): "))

            if choix == 5:
                print("Quitter")
                break

 # Entrée des nombres sur lesquels effectuer l'opération
            nombre1 = float(input("Entrez le premier nombre ou chiffre: "))
            nombre2 = float(input("Entrez le deuxième nombre ou chiffre : "))

# Exécution de l'opération sélectionnée
            if choix == 1:
                resultat = addition(nombre1, nombre2)
                print(f"Résultat: {resultat}")
            elif choix == 2:
                resultat = soustraction(nombre1, nombre2)
                print(f"Résultat: {resultat}")
            elif choix == 3:
                resultat = multiplication(nombre1, nombre2)
                print(f"Résultat: {resultat}")
            elif choix == 4:
                resultat = division(nombre1, nombre2)
                print(f"Résultat: {resultat}")
            else:
                print("Choix invalide. Veuillez entrer un nombre .")

        except ValueError:
            print("Erreur Veuillez entrer des nombres valides.")

if __name__ == "__main__":
    calculatrice()
