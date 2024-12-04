from itertools import product

def narcissique(n_chiffre):
    for chiffres in product(range(10), repeat=n_chiffre):
        #if chiffres[-1] == 0: continue #si on veut exclure les chiffres commençant par 0
        normal_num = sum(e*10**n for n, e in enumerate(chiffres))
        narcissique_version = sum(e**n_chiffre for e in chiffres)
        if narcissique_version == normal_num:
            yield normal_num

def narcissique_list(n_chiffre):
    return [str(n).zfill(n_chiffre) for n in narcissique(n_chiffre)]

# @Jules
def narcissique_oneline(n_chiffre):
    return (nn for chiffres in product(range(10), repeat=n_chiffre) if (nn := sum(e*10**n for n, e in enumerate(chiffres))) == sum(e**n_chiffre for e in chiffres))

if __name__ == "__main__":
    print(narcissique_list(5))
    print(list(narcissique_oneline(3)))