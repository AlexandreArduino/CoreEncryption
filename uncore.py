import os
from logs import *
import sys
class CORE_UNENCRYPTION(object):
    def __init__(self):
        if os.name == "posix": os.system("clear")
        elif os.name == "nt": os.system("cls")
        else: pass
        success("Démarrage de CoreUnencryption !")
        self.VerifyDirsArch()
        self.OutputFileName = self.DetectOutputFileInArgs()
        self.WaitUntilFilesSetInOutputs()
        self.ReadOutputFile()
    def VerifyDirsArch(self):
        info("Vérification de l'architecture des dossiers ...")
        try: os.mkdir("Inputs/")
        except: pass
        try: os.mkdir("Outputs/")
        except: pass
        success("L'architecture des répertoires a bien été mise à jour !")
    def DetectOutputFileInArgs(self):
        info("Récupération du nom du fichier de déchiffrement ...")
        if len(sys.argv) == 1:
            error("Aucun fichier de déchiffrement n'est spécifié !")
            error("Merci de rentrer -UnencFile=nom_du_fichier.unenc !")
            sys.exit(1)
        else:
            check = False
            for parameter in range(0, len(sys.argv)):
                if sys.argv[parameter].split("=")[0] == "-UnencFile":
                    check = True
                    try:
                        _OutputName = sys.argv[parameter].split("=")[1]
                        if _OutputName.replace(" ", "") == "": int([1, 2])
                        info(_OutputName + " a été détecté comme nom de fichier !")
                        info("Vérification de l'existence de celui-ci ...")
                        try:
                            file = open(_OutputName, "r")
                            file.readlines()
                            file.close()
                            success(_OutputName + " est disponible comme fichier !")
                            return _OutputName
                        except:
                            error("Erreur pendant l'ouverture de " + _OutputName + " !")
                            error("Fin du processus ...")
                            sys.exit(1)
                    except:
                        error("Merci de spécifier le nom du fichier derrière le paramètre de cette manière : -UnencFile=nom_du_fichier.unenc !")
                        sys.exit(1)
                else: pass
            if not check:
                error("Le paramètre -UnencFile n'a pas été trouvé !")
                error("Merci de le spécifier de cette manière : -UnencFile=nom_du_fichier.unenc !")
                sys.exit(1)
            else: pass
    def WaitUntilFilesSetInOutputs(self):
        input("[.] Merci de mettre vos fichiers chiffrés dans Outputs/ puis d'appuyer sur entrée pour les déchiffrer !\n[.] Ils seront ensuite positionner dans Inputs/ !")
    def GetContentFile(self, _file):
        try:
            file = open(_file, "r")
            _content = file.readlines()
            file.close()
            return _content
        except: return "Une erreur est survenue pendant l'ouverture de ce fichier (" + str(_file) + ")"
    def ReadOutputFile(self):
        info("Lecture du fichier de déchiffrement ...")
        _content = self.Deverse256("".join(self.GetContentFile(self.OutputFileName)))
        print(_content)
    def Deverse256(self, text):
        info("Déchiffrement ascii ...")
        text = list("".join(text))
        for char in range(0, len(text)):
            text[char] = chr(255 + ord(text[char]))
        return "".join(text)
CORE_UNENCRYPTION()