import sys
from datetime import datetime, timedelta

import get_online_data
import utilitaries
from CONST import _Const


def cron():
    debug = False
    if not debug: #SI on est pas en session de debug ALORS
        if sys.stdout.isatty(): #SI le script est lancé en terminal ALORS
            return False
        else:
            return True
    return False


def already_tweet():
    answer = ""
    if not cron():  # SI l'app n'a pas été appeler par cron ALORS
        while answer != "N" and answer != "O":  # TANT QUE l'utilisateur n'a pas répondu par oui ou non FAIRE
            print("J'ai déjà tweeté pour la date d'aujourd'hui ! \n Veux tu que je tweet à nouveau ? (O/N)")
            answer = input()  # On lui demande  si il veut modifier la date d'aujourd'hui
            if answer == "N":
                manage_error(12)
    else:
        manage_error(12)


def print_error(str_error):
    CONST = _Const()
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    if cron(): #SI l'app est appeler par Cron ALORS
        utilitaries.sendMail(True, text=str_error) #On envoie un mail avec l'erreur
    print(now + " : " + str_error) #On l'affiche
    #On l'écrit dans le log
    log = open(CONST.LOG_PATH + "log.log", "a")
    log.write("\n" + now + " : " + str_error)
    log.close()


def manage_error(error_code, error=None, today_signature=-1, gap=[]):
    if error_code == 11:
        str_error = "ERREUR : Il y a déjà une valeur pour la date d'aujourd'hui."
        print_error(str_error)
        exit(11)
    elif error_code == 12:
        str_error = "ERREUR : J'ai déjà tweeté aujourd'hui "
        print_error(str_error)
        exit(12)
    elif error_code == 21:
        str_error = "ERREUR : MySQL n\'est pas actif."
        print_error(str_error)
        exit(21)
    elif error_code == 22:
        str_error = "ERREUR : Erreur de mot de passe dans la base de donnée."
        print_error(str_error)
        exit(22)
    elif error_code == 23:
        str_error = "ERREUR : La base de donnée n\'existe pas."
        print_error(str_error)
        exit(23)
    elif error_code == 31:
        str_error = "ATTENTION : aujourd'hui il n'y a eu aucune signature."
        print_error(str_error)
    elif error_code == 41:
        str_error = "ERREUR : L'API Twitter a renvoyé : " + str(error.api_code) + " : " + str(error.args[0][0]['message'])
        print_error(str_error)
        exit(41)
    elif error_code == 52:
        str_error = "ERREUR : Il manque des dates : ("
        c = 1
        for d in gap:
            str_error += d.strftime("%d-%m-%Y")
            if c < len(gap):
                c += 1
                str_error += ", "
        str_error += ")"
        print_error(str_error)
        exit(52)