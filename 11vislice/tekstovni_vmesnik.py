
SLIKE = [
"""   _____
   |   |
   |   o
   |  /|\\
   |  / \\
  _|______ """,
"""   _____
   |   |
   |   o
   |  /|\\
   |  / 
  _|______ """,
  """   _____
   |   |
   |   o
   |  /|\\
   |  
  _|______ """,
  """   _____
   |   |
   |   o
   |  /|
   |  
  _|______ """,
  """   _____
   |   |
   |   o
   |   |
   |  
  _|______ """,
  """   _____
   |   |
   |   o
   |  
   |  
  _|______ """,
  """   _____
   |   |
   |   
   |  
   |  
  _|______ """,
  """   _____
   |   
   |   
   |  
   |  
  _|______ """,
  """   
   |   
   |   
   |  
   |  
  _|______ """,
  """   
      
      
     
     
  _______ """,
  """


   
   
  """
]



import model
from model import nova_igra

def izpis_igre(igra):
    niz = f"""{SLIKE[-igra.stevilo_napak() - 1]}
{igra.pravilni_del_gesla()}
Nepravilni ugibi: {igra.nepravilni_ugibi()}
Napačno lahko ugibaš še {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()}"""
    return niz

def izpis_zmage(igra):
    niz = f"Čestitke, zmagal si! Pravilno ste uganili geslo {igra.geslo}!"
    return niz

def izpis_poraza(igra):
    niz = f"""{SLIKE[0]}
Obesili so te! Več sreče prihodnjič. Pravilno geslo je bilo {igra.geslo}."""
    return niz

def zahtevaj_vnos():
    return input("Ugibaj črko: ")

def pozeni_vmesnik():
    igra = model.nova_igra()
    while not igra.zmaga() and not igra.poraz():
        print(izpis_igre(igra))
        crka = zahtevaj_vnos()
        while len(crka) != 1 or not crka.isalpha():
            print("To ni črka!")
            crka = zahtevaj_vnos()
        stanje = igra.ugibaj(crka)
    if igra.zmaga():
        print(izpis_zmage(igra))
    else:
        print(izpis_poraza(igra))
    odlocitev = input("Bi želeli igrati ponovno? (D/N): ")
    if odlocitev.upper() == "D":
        pozeni_vmesnik()

pozeni_vmesnik()