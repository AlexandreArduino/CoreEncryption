import os
from logs import info, success
def InitAllDirs():
    info("Initialisation des répertoires du logiciel ...")
    try: os.mkdir("Inputs")
    except: pass
    try: os.mkdir("Outputs")
    except: pass
    try: os.remove("core.conf")
    except: pass
    success("Initialisation terminée !")
    info("Merci de mettre vos fichiers à chiffrer dans Inputs/")
    info("Après avoir exécuter ce programme, vous trouverez les fichiers chiffrés dans Outputs/")