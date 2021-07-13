from logs import *
import sys
from random import randint
class Core(object):
    def __init__(self, parameters):
        info("Initialisation du coeur de chiffrement ...")
        self.parameters = parameters
        self.DefaultAlphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTUVWXYZ0123456789"
        self.DetectAllParameters()
        self.alphabet = self.DetectAlphabetInParameters()
        self.key = self.DetectKeyInParameters()
        self.iterations = self.DetectIterationsOfEncryption()
        self.SaveConfiguration()
    def DetectAllParameters(self):
        info("Détection des paramètres à utiliser ...")
        if len(self.parameters) == 1:
            error("Aucuns paramètres spécifiés ! Il est impossible de configurer le logiciel !")
            sys.exit(1)
        else: pass
    def DetectAlphabetInParameters(self):
        info("Récupération de l'alphabet ...")
        for parameter in range(0, len(self.parameters)):
            if self.parameters[parameter].split("=")[0].lower() == "-alphabet":
                try: _alphabet = self.parameters[parameter].split("=")[1]
                except:
                    error("Erreur de syntaxe dans les paramètres, merci de respecter : -parametre=value !")
                    sys.exit(1)
                if _alphabet.lower() == "µauto":
                    success("L'utilisation de l'alphabet par défaut a été détecté, celui va être utilisé >>> " + str(self.DefaultAlphabet))
                    return self.DefaultAlphabet
                elif _alphabet != "":
                    success("Un alphabet a été trouvé ! >>> " + str(_alphabet))
                    return _alphabet
                else:
                    error("L'alphabet doit contenir des caractères ! Il ne doit pas être vide !")
                    sys.exit(1)
            else: pass
        error("Aucun alphabet détecté ! Merci de spécifier -alphabet=\"votre alphabet\" !")
        sys.exit(1)
    def DetectKeyInParameters(self):
        info("Récupération de la clé de chiffrement ...")
        for parameter in range(0, len(self.parameters)):
            if self.parameters[parameter].split("=")[0].lower() == "-key":
                try:
                    _key = self.parameters[parameter].split("=")[1]
                    if _key.lower() == "µrandom":
                        success("Une clé aléatoire va être générée à l'aide de la taille de l'alphabet ...")
                        return randint(0, len(self.alphabet) - 1)
                    else:
                        try:
                            success("La clé a été détectée comme étant : " + str(int(_key)) + " !")
                            if int(_key) < 0 or int(_key) > len(self.alphabet) - 1:
                                error("La clé doit être un nombre entier comprise entre 0 et " + str(len(self.alphabet) - 1) + " !")
                                sys.exit(1)
                            else: return int(_key)
                        except:
                            # error("La clé doit être un nombre entier comprise entre 0 et " + str(len(self.alphabet) - 1) + " !")
                            sys.exit(1)
                except:
                    error("Erreur de syntaxe dans les paramètres, merci de respecter : -parametre=value !")
                    sys.exit(1)
            else: pass
        error("Impossible de trouver la clé de chiffrement ! Merci de la spécifier avec -key=valeur !")
        sys.exit(1)
    def DetectIterationsOfEncryption(self):
        info("Récupération du nombre d'itérations de chiffrement ...")
        for parameter in range(0, len(self.parameters)):
            if self.parameters[parameter].split("=")[0].lower() == "-i":
                try:
                    _iterations = self.parameters[parameter].split("=")[1]
                except:
                    error("Vous devez spécifier une valeur pour le nombre d'itérations !")
                    sys.exit(1)
                try: _iterations = int(_iterations)
                except:
                    error("Le nombre d'itérations doit être un nombre entier !")
                    sys.exit(1)
                if _iterations < 0:
                    error("Le nombre d'itérations doit être >= 0 !")
                    sys.exit(1)
                else: return _iterations
            else: pass
        error("Impossible de trouver le nombre d'itérations ! Merci de spécifier cette valeur avec -i=valeur !")
        sys.exit(1)
    def SaveConfiguration(self):
        info("Sauvegarde de la configuration actuelle ...")
        file = open("core.conf", "w")
        file.write("ALPHABET=" + str(self.alphabet) + "\nKEY=" + str(self.key) + "\nITERATIONS=" + str(self.iterations))
        file.close()
        success("La configuration a été sauvegardée !")