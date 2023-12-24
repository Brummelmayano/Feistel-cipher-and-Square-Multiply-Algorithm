
# Le chiffrement de Feisteil

#fonction pour la génération des clés
def feistel_keygen(key,left_shift=2, right_shift=1, perm_h = [6, 5, 2, 7, 4, 1, 3, 0]):
    # 1. Application de la permutation H fixe
    h_key = [key[perm_h[i]] for i in range(8)]

    # 2. Division de la clé en deux blocs de 4 bits
    k1_prime = h_key[:4]
    k2_prime = h_key[4:]

    # 3. Calcul des sous-clés k1 et k2
    k1 = [k1_prime[i] ^ k2_prime[i] for i in range(4)]
    k2 = [k2_prime[i] & k1_prime[i] for i in range(4)]

    # 4. Décalage des sous-clés
    k1_shifted = k1[left_shift:] + k1[:left_shift]
    k2_shifted = k2[-right_shift:] + k2[:-right_shift]

    return k1_shifted, k2_shifted




#fonction pour le chiffrement
def feistel_encrypt(N,k1,k2,perm_pi=[4, 6, 0, 2, 7, 3, 1, 5]):
    # 2. Application de la permutation π
    pi_N = [N[perm_pi[i]] for i in range(8)]

    # 3. Division du bloc en deux parties
    G = pi_N[:4]
    D = pi_N[4:]

    # 4. Premier round
    P = [2, 0, 1, 3] # permutation fixe

    GP = [G[P[i]] for i in range(4)] #permutation de G

    D1 = [GP[i] ^ k1[i] for i in range(4)]

    G1 = [D[i] ^ (G[i] | k1[i]) for i in range(4)]


    # 5. Deuxième round
    G1P = [G1[P[i]] for i in range(4)] #permutation de G

    D2 = [G1P[i] ^ k2[i] for i in range(4)]

    G2 = [D1[i] ^ (G1[i] | k2[i]) for i in range(4)]
    # 6. Concaténation des blocs G2 et D2
    C = G2 + D2

    # 7. Application de l'inverse de la permutation π^-1
    perm_pi_inv = [perm_pi.index(i) for i in range(len(perm_pi))]

    # 8. Sortie du texte chiffré C de longueur 8
    C = [C[perm_pi_inv[i]] for i in range(8)]

    return C

def feistel_decrypt(C,k1,k2,perm_pi = [4, 6, 0, 2, 7, 3, 1, 5]):
    

    # 2. Application de la permutation π
    pi_C = [C[perm_pi[i]] for i in range(8)]

    # 3. Division du bloc en deux  parties
    G2 = pi_C[:4]
    D2 = pi_C[4:]

    # 4. Premier round

    P = [2, 0, 1, 3] # permutation fixe
    Pi =  [P.index(i) for i in range(len(P))]

    # P est maintenant une permutation inverse
    G1 = [D2[i] ^ k2[i] for i in range(4)]
    G1 = [G1[Pi[i]] for i in range(4)]
    D1 = [G2[i] ^ (G1[i] | k2[i]) for i in range(4)]

    # 5. Deuxième round    
    G0 = [D1[i] ^ k1[i] for i in range(4)]
    G0 = [G0[Pi[i]] for i in range(4)]
    D0 = [G1[i] ^ (G0[i] | k1[i]) for i in range(4)]

    # 6. Concaténation des blocs G0 et D0
    N = G0 + D0

    # 7. Application de l'inverse de la permutation π^-1
    perm_pi_inv = [perm_pi.index(i) for i in range(len(perm_pi))]
    
    # 8. Sortie de texte clair N de longueur 8
    N = [N[perm_pi_inv[i]] for i in range(8)]

    return N

