#
#   dev's Twitter : @__MoonLuna__
#   project : handi bot petition for the AAH
#
###################################################

#!/usr/bin/env python3
import os
from datetime import datetime

import interact_twitter
import load_data
import get_online_data
import dataBase
import manage_data
import utilitaries
from CONST import _Const

CONST = _Const()
no_tweet = False  #True si on veut que l'app ne tweet pas False si on veux qu'elle tweet

db = dataBase.Db()
nb = get_online_data.get_online_data()


def check(nb):
    if 5000 <= nb < 10000:
        twitter = interact_twitter.Twitter()  # Instanciaition de Twitter
        if not twitter.has_tweet(5000):  # on regarde si on a déjà tweeté aujourd'hui
            if not no_tweet:  # SI l'app a prévue de tweeter ALORS
                tweet_str = "Tiens, tiens 5 000 signatures !\n\n" + \
                    "C'est un bon début ! \n\n" + \
                    "Aller on se motive les p'tits loups !\n\n" + \
                    "On vas en finir avec la dépendance financière des personnes  handicapées !\n\n" + \
                    "#SignezPourNotreAutonomie\n\n" + \
                    "https://petitions.assemblee-nationale.fr/initiatives/i-358"
                manage_data.level_reached(twitter, tweet_str, 5000)

    elif 10000 <= nb < 20000:
        twitter = interact_twitter.Twitter()  # Instanciaition de Twitter
        if not twitter.has_tweet(10000):  # on regarde si on a déjà tweeté aujourd'hui
            if not no_tweet:  # SI l'app a prévue de tweeter ALORS
                tweet_str = "10 000 Signatures, on rajoute un chiffre !\n\n" + \
                        "Embêtez mon humaine les p'tits loups ! \n\n" + \
                        "Avant 20 000 il faut qu'ael prenne des screens ! \n\n" + \
                        "On vas en finir avec la dépendance financière des personnes  handicapées !\n\n" + \
                        "#SignezPourNotreAutonomie\n\n" + \
                        "https://petitions.assemblee-nationale.fr/initiatives/i-358"
                manage_data.percent_reached(twitter, tweet_str, None, 10000)

    elif 20000 <= nb < 25000:
        twitter = interact_twitter.Twitter()  # Instanciaition de Twitter

        if not twitter.has_tweet(20000):  # on regarde si on a déjà tweeté aujourd'hui

            if not no_tweet:  # SI l'app a prévue de tweeter ALORS
                tweet_str = "20 000 singnatures !\n\n" + \
                        "Je suis fier de vous les p'tits loups ! \n\n" + \
                        "Ca commence à bien avancer ! \n\n" + \
                        "On vas en finir avec la dépendance financière des personnes  handicapées !\n\n" + \
                        "#SignezPourNotreAutonomie\n\n" + \
                        "https://petitions.assemblee-nationale.fr/initiatives/i-358"
                manage_data.level_reached(twitter, tweet_str, 20000)


    elif 25000 <= nb < 30000:
        twitter = interact_twitter.Twitter()  # Instanciaition de Twitter
        if not twitter.has_tweet(25000):  # on regarde si on a déjà tweeté aujourd'hui
            if not no_tweet:  # SI l'app a prévue de tweeter ALORS
                tweet_str = "On l'a fait les p'tits loup.\n\n" + \
                    "On en est à 25% ! Le quart. \n\n" + \
                    "Nos députés vont nous écouter" + \
                    "Prochaine étape 33%\n\n" + \
                    "On vas en finir avec la dépendance financière des personnes  handicapées !\n\n" + \
                    "#SignezPourNotreAutonomie\n\n" + \
                    "https://petitions.assemblee-nationale.fr/initiatives/i-358"
                manage_data.percent_reached(twitter, tweet_str, None, 25000)

    elif 30000 <= nb < 33000:
        twitter = interact_twitter.Twitter()  # Instanciaition de Twitter
        if not twitter.has_tweet(30000):  # on regarde si on a déjà tweeté aujourd'hui
            if not no_tweet:  # SI l'app a prévue de tweeter ALORS
                tweet_str = "Whaaa 30 000 singnatures !\n\n" + \
                        "Et bien ça commence à bien monter ! \n\n" + \
                        "Aller on vas y arriver avant le 17 Juin ! \n\n" + \
                        "On vas en finir avec la dépendance financière des personnes  handicapées !\n\n" + \
                        "#SignezPourNotreAutonomie\n\n" + \
                        "https://petitions.assemblee-nationale.fr/initiatives/i-358"
                manage_data.level_reached(twitter, tweet_str, 30000)

    elif 33333 <= nb < 40000:
        twitter = interact_twitter.Twitter()  # Instanciaition de Twitter
        if not twitter.has_tweet(33333):  # on regarde si on a déjà tweeté aujourd'hui
            if not no_tweet:  # SI l'app a prévue de tweeter ALORS
                tweet_str = "On l'a fait les p'tits loup.\n\n" + \
                        "On en est à 33% c'est le tiers. \n\n" + \
                        "Nos députés vont nous écouter" + \
                        "Prochaine étape 50%\n\n" + \
                        "On vas en finir avec la dépendance financière des personnes  handicapées !\n\n" + \
                        "#SignezPourNotreAutonomie\n\n" + \
                        "https://petitions.assemblee-nationale.fr/initiatives/i-358"
                manage_data.percent_reached(twitter, tweet_str, None, 33333)
    elif 40000 <= nb < 50000:
        twitter = interact_twitter.Twitter()  # Instanciaition de Twitter
        if not twitter.has_tweet(40000):  # on regarde si on a déjà tweeté aujourd'hui
            if not no_tweet:  # SI l'app a prévue de tweeter ALORS
                tweet_str = "Owiiiii 40 000 signatures !\n\n" + \
                        "Dans 10 000 c'est la moitié ! \n\n" + \
                        "Exelent ça les p'tits loups !\n\n" + \
                        "On vas en finir avec la dépendance financière des personnes  handicapées !\n\n" + \
                        "#SignezPourNotreAutonomie\n\n" + \
                        "https://petitions.assemblee-nationale.fr/initiatives/i-358"
                manage_data.level_reached(twitter, tweet_str, 40000)
    elif 50000 <= nb < 60000:
        twitter = interact_twitter.Twitter()  # Instanciaition de Twitter
        if not twitter.has_tweet(50000):  # on regarde si on a déjà tweeté aujourd'hui
            if not no_tweet:  # SI l'app a prévue de tweeter ALORS
                tweet_str = "On l'a fait les p'tits loup.\n\n" + \
                    "On en est à 50% ! La moitié. Franchement ça donne de l'espoir\n\n" + \
                    "Prochaine étape 66%\n\n" + \
                    "On vas en finir avec la dépendance financière des personnes  handicapées !\n\n" + \
                    "#SignezPourNotreAutonomie\n\n" + \
                    "https://petitions.assemblee-nationale.fr/initiatives/i-358"
                manage_data.percent_reached(twitter, tweet_str, None, 50000)
    elif 60000 <= nb < 66666:
        twitter = interact_twitter.Twitter()  # Instanciaition de Twitter
        if not twitter.has_tweet(60000):  # on regarde si on a déjà tweeté aujourd'hui
            if not no_tweet:  # SI l'app a prévue de tweeter ALORS
                tweet_str = "OMG 60 000 signatures !\n\n" + \
                    "Un peut d'espoir en plus pour nos droits\n\n" + \
                    "C'est trop bien !\n\n" + \
                    "On vas en finir avec la dépendance financière des personnes  handicapées !\n\n" + \
                    "#SignezPourNotreAutonomie\n\n" + \
                    "https://petitions.assemblee-nationale.fr/initiatives/i-358"
                manage_data.level_reached(twitter, tweet_str, 60000)
    elif 66666 <= nb < 70000:
        twitter = interact_twitter.Twitter()  # Instanciaition de Twitter
        if not twitter.has_tweet(66666):  # on regarde si on a déjà tweeté aujourd'hui
            if not no_tweet:  # SI l'app a prévue de tweeter ALORS
                tweet_str = "On l'a fait les p'tits loup.\n\n" + \
                    "On en est à 66% ! C'est les 2/3\n\n" + \
                    "Prochaine étape 75%\n\n" + \
                    "On vas en finir avec la dépendance financière des personnes  handicapées !\n\n" + \
                    "#SignezPourNotreAutonomie\n\n" + \
                    "https://petitions.assemblee-nationale.fr/initiatives/i-358"
                manage_data.percent_reached(twitter, tweet_str, None, 66666)
    elif 70000 <= nb < 75000:
        twitter = interact_twitter.Twitter()  # Instanciaition de Twitter
        if not twitter.has_tweet(70000):  # on regarde si on a déjà tweeté aujourd'hui
            if not no_tweet:  # SI l'app a prévue de tweeter ALORS
                tweet_str = "Déjà 70 000 signatures\n\n" + \
                    "ça se fête moi je dit !\n\n" + \
                    "Bientôt les 3/4\n\n" + \
                    "On vas en finir avec la dépendance financière des personnes  handicapées !\n\n" + \
                    "#SignezPourNotreAutonomie\n\n" + \
                    "https://petitions.assemblee-nationale.fr/initiatives/i-358"
                manage_data.level_reached(twitter, tweet_str, 70000)
    elif 75000 <= nb < 80000:
        twitter = interact_twitter.Twitter()  # Instanciaition de Twitter
        if not twitter.has_tweet(75000):  # on regarde si on a déjà tweeté aujourd'hui
            if not no_tweet:  # SI l'app a prévue de tweeter ALORS
                tweet_str = "On l'a fait les p'tits loup.\n\n" + \
                    "On en est à 75% ! C'est les 3/4\n\n" + \
                    "Prochaine étape 80%\n\n" + \
                    "On vas en finir avec la dépendance financière des personnes  handicapées !\n\n" + \
                    "#SignezPourNotreAutonomie\n\n" + \
                    "https://petitions.assemblee-nationale.fr/initiatives/i-358"
                manage_data.percent_reached(twitter, tweet_str, None, 75000)
    elif 80000 <= nb < 90000:
        twitter = interact_twitter.Twitter()  # Instanciaition de Twitter
        if not twitter.has_tweet(80000):  # on regarde si on a déjà tweeté aujourd'hui
            if not no_tweet:  # SI l'app a prévue de tweeter ALORS
                tweet_str = "On l'a fait les p'tits loup.\n\n" + \
                    "On en est à 80% !\n\n" + \
                    "Prochaine étape 90%\n\n" + \
                    "On vas en finir avec la dépendance financière des personnes  handicapées !\n\n" + \
                    "#SignezPourNotreAutonomie\n\n" + \
                    "https://petitions.assemblee-nationale.fr/initiatives/i-358"
                manage_data.percent_reached(twitter, tweet_str, None, 80000)
    elif 90000 <= nb < 95000:
        twitter = interact_twitter.Twitter()  # Instanciaition de Twitter
        if not twitter.has_tweet(90000):  # on regarde si on a déjà tweeté aujourd'hui
            if not no_tweet:  # SI l'app a prévue de tweeter ALORS
                tweet_str = "On l'a fait les p'tits loup.\n\n" + \
                    "On en est à 90 000 signatures ! \n\n" + \
                    "La fin se rapproche\n\n" + \
                    "On vas en finir avec la dépendance financière des personnes  handicapées !\n\n" + \
                    "#SignezPourNotreAutonomie\n\n" + \
                    "https://petitions.assemblee-nationale.fr/initiatives/i-358"
                manage_data.level_reached(twitter, tweet_str, 90000)
    elif 95000 <= nb < 100000:
        twitter = interact_twitter.Twitter()  # Instanciaition de Twitter
        if not twitter.has_tweet(95000):  # on regarde si on a déjà tweeté aujourd'hui
            if not no_tweet:  # SI l'app a prévue de tweeter ALORS
                tweet_str = "On l'a fait les p'tits loup.\n\n" + \
                    "On en est à 95% !\n\n" + \
                    "Encore un petit effort et on en sera venu à bout !\n\n" + \
                    "On vas en finir avec la dépendance financière des personnes  handicapées !\n\n" + \
                    "#SignezPourNotreAutonomie\n\n" + \
                    "https://petitions.assemblee-nationale.fr/initiatives/i-358"
                manage_data.percent_reached(twitter, tweet_str, None, 95000)
    elif nb >= 100000:
        twitter = interact_twitter.Twitter()  # Instanciaition de Twitter
        if not twitter.has_tweet(100000):  # on regarde si on a déjà tweeté aujourd'hui
            if not no_tweet:  # SI l'app a prévue de tweeter ALORS
                tweet_str = "OMG ! On est arriver à la fin ! \n\n" + \
                    "Merci à tous, maintenant on attends le débat à l'assemblée.\n\n" + \
                    "C'est un espoir pour toutes les personnes handi qui s'allume !\n\n" + \
                    "Bientôt elles n'auront plus à choisir entre amour et argent. \n\n" +\
                    "https://petitions.assemblee-nationale.fr/initiatives/i-358"
                manage_data.the_end(twitter, tweet_str)

check(nb)