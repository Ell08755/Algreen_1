amino_acid={
    'Ala':{'name':'Alanine','single':'A','type':'nonpolar'},
    'Arg':{'name':'Arginine','single':'R','type':'positive'},
    'Asn':{'name':'Asparagine','single':'N','type':'uncharged polar'},
    'Asp':{'name':'Aspartic','single':'D','type':'negative'},
    'Cys':{'name':'Cysteine','single':'C','type':'nonpolar'},
    'Gly':{'name':'Glycine','single':'G','type':'nonpolar'},
    'Gln':{'name':'Glutamine','single':'Q','type':'uncharged polar'},
    'Glu':{'name':'Glutamic','single':'E','type':'negative'},
    'His':{'name':'Histidine','single':'H','type':'uncharged polar'},
    'Ile':{'name':'Isoleucine','single':'I','type':'nonpolar'},
    'Lys':{'name':'Lysine','single':'K','type':'positive'},
    'Leu':{'name':'Leucine','single':'L','type':'nonpolar'},
    'Met':{'name':'Methionine','single':'M','type':'nonpolar'},
    'Phe':{'name':'Phenylalanine','single':'F','type':'nonpolar'},
    'Pro':{'name':'Proline','single':'P','type':'nonpolar'},
    'Ser':{'name':'Serine','single':'S','type':'uncharged polar'},
    'Thr':{'name':'Threonine','single':'T','type':'uncharged polar'},
    'Trp':{'name':'Tryptophan','single':'W','type':'nonpolar'},
    'Tyr':{'name':'Tyrosine','single':'Y','type':'uncharged polar'},
    'Val':{'name':'Valine','single':'V','type':'nonpolar'},
}
import random
import re
def random_amino_acid_name(amino_acids):
    code = random.choice(list(amino_acids.keys()))
    print(f"know: {amino_acids[code]['name']}")
    input('ready?')
    info = amino_acids[code]
    print(f"{info['name']}-{code}-{info['single']}-{info['type']}")

def random_amino_acid_3abbr(amino_acids):
    code = random.choice(list(amino_acids.keys()))
    print(f"know: {code}")
    input('ready?')
    info = amino_acids[code]
    print(f"{info['name']}-{code}-{info['single']}-{info['type']}")

def random_amino_acid_single(amino_acids):
    code = random.choice(list(amino_acids.keys()))
    print(f"know: {amino_acids[code]['single']}")
    input('ready?')
    info = amino_acids[code]
    print(f"{info['name']}-{code}-{info['single']}-{info['type']}")

def print_amino_acid_info(amino_acids, code):
    info = amino_acids[code]
    print(f"{info['name']}-{code}-{info['single']}-{info['type']}")
    print(f"Full name: {info['name']}")
    print(f"Type: {info['type']}")

def main():
    global amino_acid
    while True:
        print("\n\n1. name")
        print("2. single abbr")
        print("3. three abbr")
        choice = input("Choose:")
        if choice == "1":
            random_amino_acid_name(amino_acid)
        elif choice == "2":
            random_amino_acid_single(amino_acid)
        elif choice == '3':
            random_amino_acid_3abbr(amino_acid)
        break

while True:
    main()
