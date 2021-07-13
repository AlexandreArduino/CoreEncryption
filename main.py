from logs import *
from dirs import *
from core import *
import os
import sys
def main():
    if os.name == "posix": os.system("clear")
    elif os.name == "nt": os.system("cls")
    else: pass
    success("Démarrage CoreEncryption ...")
    InitAllDirs()
    info("Création de l'objet Core ...")
    MainCore = Core(sys.argv)
if __name__ == "__main__": main()
else: pass