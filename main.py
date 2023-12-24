from FeistelCipher import feistel_keygen, feistel_encrypt, feistel_decrypt
from SquareMultiply import square_and_multiply

print("\n\n================================================================\n")
print("BIENVENU DANS NOTRE PROGRAMME\nCryptographie et Sécurité Informatique")
print("UNIKIN L3 INFORMATIQUE 2022-2023\n")
print("Ce petit programme est conçu envue de tester les algorithmes implementés dans ma repository")

menu = int(input("entrez l'algorithme de chiffrement que vous souhaiter exécuter: \nPour le chiffrement de Feistel tapez 1\nPour le Square & Multiply Algorithm tapez 2 :  \n\n===>> "))

if menu == 1:
    K = input("Entrez la clé K de longueur 8  pour la generation de la clé \nex: 11001010\n")
    N1 = input("Entrez le message à chiffrer qui doit etre un bloc N de 8 bits \nex: 00110011\n\n")
        
    # Convertir les entrées en listes
    K = [int(x) for x in K]
    N1 = [int(x) for x in N1]

    temp = input("\n\nVoulez-vous configurer l'algorithme? entrez: \nO pour modifier les permutations et l'ordre de décalage et\nN pour utiliser des valeurs par defaut. \n\n===>> ")

    k1,k2 = feistel_keygen([1,1,1,0,1,1,0,0],2,1)
    if temp == "O" or "o":

        perm_h = input("\n\nEntrez la permutation H pour la generation de clé, ex= 65274130 :\n===>> ")
        perm_pi = input("Entrez la permutation π pour le chiffrement et déchiffrement ex= 46027315:\n===>> ")


        # Convertir les entrées en listes
        perm_h = [int(x) for x in perm_h]
        perm_pi = [int(x) for x in perm_pi]

        left_shift_order = int(input("Entrez l'ordre de décalage à gauche : "))
        right_shift_order = int(input("Entrez l'ordre de décalage à droite : "))

        #appel de trois fonction (algorithme de Feistel)  avec argument personalisé
        k1,k2 = feistel_keygen(K,left_shift_order,right_shift_order,perm_h)
        C = feistel_encrypt(N1,k1,k2,perm_pi)
        N2 = feistel_decrypt(C,k1,k2,perm_pi)
        print("\n\nLe bloc N de 8 bits",N1,"\nLe texte chiffré C de longueur 8. =",C,"\nLe texte clair N de longueur 8.",N2)
    
    elif temp == "N" or "n":
        #appel de trois fonction (algorithme de Feistel ) sans argument
        k1,k2 = feistel_keygen(K)
        C = feistel_encrypt(N1,k1,k2)
        N2 = feistel_decrypt(C,k1,k2)
        print("\n\nLe bloc N de 8 bits",N1,"\nLe texte chiffré C de longueur 8. =",C,"\nLe texte clair N de longueur 8.",N2)

    else:
        print("\nmerci de bien répondre svp\n")
        

        
elif menu == 2:
    # Demander à l'utilisateur d'entrer les valeurs
    x = int(input("Entrez la valeur de x : "))
    b = int(input("Entrez la valeur de b : "))
    n = int(input("Entrez la valeur de n : "))

    # Appeler la fonction et afficher le résultat
    resultat = square_and_multiply(x, b, n)
    print(f"Le résultat de {x}^{b} (mod {n}) est : {resultat}\n")
    
else:
    print("veuillez choisir le bon numero")

    