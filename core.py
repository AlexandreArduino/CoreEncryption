from logs import *
import sys
from random import randint
import glob
import os
import shutil
from time import sleep
from datetime import datetime
class Core(object):
    def __init__(self, parameters):
        info("Initialisation du coeur de chiffrement ...")
        self.parameters = parameters
        self.DefaultAlphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTUVWXYZ0123456789"
        self.DetectAllParameters()
        # self.alphabet = self.DetectAlphabetInParameters()
        self.key = self.DetectKeyInParameters()
        self.iterations = self.DetectIterationsOfEncryption()
        self.FilesTOEncrypt = []
        self.SaveConfiguration()
        self.WaitUntilFilesSetInInputs()
        self.GetIndexDatabase()
        self.ShowIndexDatabase()
        self.AskForConfirmationBeforeEncryptation()
        self.Encryption()
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
                        success("Une clé aléatoire va être générée ...")
                        return randint(0, 1000)
                    else:
                        try:
                            success("La clé a été détectée comme étant : " + str(int(_key)) + " !")
                            if int(_key) < 0 or int(_key) > 1000:
                                error("La clé doit être un nombre entier >= 0 et <= 1000 !")
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
        file.write("KEY=" + str(self.key) + "\nITERATIONS=" + str(self.iterations))
        file.close()
        success("La configuration a été sauvegardée !")
    def WaitUntilFilesSetInInputs(self):
        input("[.] Merci d'appuyer sur entrée quand vos fichiers et/ou dossiers à chiffrer ont été déplacés dans Inputs/ ...")
    def GetIndexDatabase(self):
        success("Lecture de la base de données ...")
        os.chdir("Inputs/")
        self.FilesToEncrypt = []
        # self.HistorysSubDirs = []
        _count = 0
        for (directory, SubDirectory, files) in os.walk(os.getcwd()):
            # self.HistorysSubDirs.append(SubDirectory)
            for file in range(0, len(files)):
                if directory[len(directory) - 1] != '/': directory += '/'
                else: pass
                files[file] = directory + files[file]
            self.FilesToEncrypt.extend(files)
        os.chdir("../")
    def ShowIndexDatabase(self):
        success("Liste des fichiers à chiffrer : ")
        for file in range(0, len(self.FilesToEncrypt)): print("\t- " + self.FilesToEncrypt[file])
        info(str(len(self.FilesToEncrypt)) + " fichiers ont été détectés!")
    def AskForConfirmationBeforeEncryptation(self):
        if not len(self.FilesToEncrypt):
            error("Aucun fichier n'est à chiffrer!")
            sys.exit(0)
        elif len(self.FilesToEncrypt):
            _choice = input("[?] Ête-vous sûr de vouloir chiffrer ce(s) fichier(s) ? oui/non >>> ").lower()
            if _choice == "non":
                error("Annulation du chiffrement de ce(s) fichier(s)!")
                sys.exit(0)
            elif _choice == "oui":
                info("Le chiffrement va démarrer...")
                input("[!] Pensez bien à vous souvenir des valeurs qui vont être affichées à la fin du processus!\n[!] Elles permettront de déchiffrer vos fichiers!\n[!] Pensez aussi à faire une copie de ceux-ci au cas où le chiffrement ne se passe pas correctement!\n[.] Appuyez quand vous êtes prêt...")
            else:
                error("Ce n'est pas une réponse attendue, elle sera considérée comme non!")
                error("Annulation du chiffrmeent de ce(s) fichier(s)!")
                sys.exit(0)
        else:
            error("Erreur pendant avec self.FilesToEncrypt!")
            sys.exit(1)
    def Encryption(self):
        print("#"*50)
        info("Démarrage du chiffrement ...")
        self.CreateDirArch()
        self.SetOutput()
        for file in range(0, len(self.FilesToEncrypt)):
            OutputFile = ""
            info("Chiffrement de " + self.FilesToEncrypt[file] + " ...")
            info("Récupération du contenu du fichier ...")
            _content = self.GetContentFile(self.FilesToEncrypt[file])
            if not _content:
                error("Une erreur est survenue pendant la lecture du fichier!")
                error(self.FilesToEncrypt[file] + " ne sera pas chiffré!")
            else:
                info("Ouverture de la sortie ...")
                print(self.FilesToEncrypt[file].replace("Inputs", "Outputs"))
                output = open(self.OutputsIndex[file], "w")
                OutputFile = "".join(self.ReverseString256(_content))
                OutputFile = self.AddKey(OutputFile)
                OutputFile = self.FinalEncryption(OutputFile)
                output.write(OutputFile)
                output.close()
                success(self.FilesToEncrypt[file] + " a bien été chiffré!")
        self.SaveOutputConfiguration()
        print("#"*50)
        success("Le chiffrement s'est terminé avec succès !")
    def GetContentFile(self, path):
        try:
            file = open(path, "r")
            l = file.readlines()
            file.close()
            return l
        except: return False
    def CreateDirArch(self):
        info("Création de l'architecture des dossiers en sortie ...")
        shutil.rmtree("Outputs/")
        shutil.copytree("Inputs/", "Outputs")
        info("Création du nouveau index ...")
        self.OutputsIndex = []
        for file in range(0, len(self.FilesToEncrypt)):
            self.OutputsIndex.append(self.FilesToEncrypt[file].replace("Inputs", "Outputs"))
            success(self.OutputsIndex[file])
    def ReverseString256(self, text):
        #Prend le _content d'un fichier
        info("Inversion ascii ...")
        _ascii_input = []
        text = list("".join(text))
        for char in range(0, len(text)): text[char] = chr(255 - ord(text[char]))
        return text
    def AddKey(self, text):
        info("Ajout de la clé ...")
        text = list(text)
        for char in range(0, len(text)): text[char] = chr(ord(text[char]) + int(self.OutputToSave[0]))
        return "".join(text)
    def FinalEncryption(self, text):
        info("Finalisation du chiffrement ...")
        text = list(text)
        for char in range(0, len(text)): text[char] = chr(ord(text[char]) + abs(int(self.OutputToSave[2]) - int(self.OutputToSave[3]) + int(self.OutputToSave[4]) + int(self.OutputToSave[5]) + int(self.OutputToSave[6])))
        return "".join(text)
    def SetOutput(self):
        info("Préparation du fichier de sortie ...")
        self.OutputToSave = []
        self.OutputToSave.append(str(self.key))
        self.OutputToSave.append(str(datetime.now().year))
        self.OutputToSave.append(str(datetime.now().month))
        self.OutputToSave.append(str(datetime.now().day))
        self.OutputToSave.append(str(datetime.now().hour))
        self.OutputToSave.append(str(datetime.now().minute))
        self.OutputToSave.append(str(datetime.now().second))
    def SaveOutputConfiguration(self):
        info("Enregistrement de la configuration de déchiffrement ...")
        file = open("output.unenc", "w")
        for element in range(0, len(self.OutputToSave)): file.write(self.OutputToSave[element] + '\n')
        file.close()
        OutputEncrypt = self.ReverseString256(self.GetContentFile("output.unenc"))
        file = open("output.unenc", "w")
        file.write("".join(OutputEncrypt))
        file.close()
        success("Le fichier de sortie a été écrit avec succès !")