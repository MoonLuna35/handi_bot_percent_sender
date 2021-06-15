#
#   dev's Twitter : @__MoonLuna__
#   project : handi bot petition for the AAH
#
###################################################
from datetime import datetime, timedelta

import tweepy

import dataBase
import error
from CONST import _Const


class Twitter:
    api = None

    def __init__(self):  # constructeur
        CONST = _Const()
        # On mets les paramètre d'authentification
        auth = tweepy.OAuthHandler(CONST.TWITTER_CONSUMER, CONST.TWITTER_CONSUMER_SECRET)
        auth.set_access_token(CONST.TWITTER_ACESS_TOKEN, CONST.TWITTER_ACESS_TOKEN_SECRET)
        try:
            self.api = tweepy.API(auth)  # On essaye de se connecter avec l'API
        except tweepy.TweepError as e:  # SI ON LEVE UNE EXEPTION ALORS
            error.manage_error(41, e)  # On gère l'erreur en envoyant l'exeption

    # Regarder si on a déjà tweeté
    def has_tweet(self, lvl):
        db = dataBase.Db()
        if db.lvl_is_tweeted(lvl):
            return True
        return False

    # Envoyer le thread avec les infos de la petition. On donne les textes du tweet

    def tweet_percent(self, tweet, lvl):
        CONST = _Const()
        media_ids = []
        try:
            # On upload les graphiques
            pic1 = self.api.media_upload(CONST.IMG_PATH + "canard.gif")

            # On récupère leurs identifiants
            media_ids.append(pic1.media_id)
            self.api.create_media_metadata(media_ids[0],
                                           "Un canard tout excité parce qu'on est arrivé à " + str(lvl / 1000) + "%")
            # On tweet le premier tweet
            original_tweet = self.api.update_status(tweet, media_ids=media_ids)

            return original_tweet
        except tweepy.TweepError as e:  # SI ON LEVE UNE EXEPTION de l'API ALORS
            error.manage_error(41, e)  # On gère l'erreur en envoayant l'exeption

    def tweet_lvl(self, tweet, lvl):
        CONST = _Const()
        media_ids = []
        try:
            # On upload les photos
            pic1 = self.api.media_upload(CONST.IMG_PATH + str(lvl - 1) + ".png")
            pic2 = self.api.media_upload(CONST.IMG_PATH + str(lvl) + ".png")

            # On récupère leurs identifiants
            media_ids.append(pic1.media_id)
            media_ids.append(pic2.media_id)
            # On ajoute les descriptions pour l'accéssibilité
            self.api.create_media_metadata(media_ids[0],
                                           "L'image de l'endroit où on signe sur la pétition avec noté : " +
                                           str(lvl - 1) + "/100 000 signatures")
            self.api.create_media_metadata(media_ids[1],
                                           "L'image de l'endroit où on signe sur la pétition avec noté : " +
                                           str(lvl) + "/100 000 signatures")
            # On tweet
            original_tweet = self.api.update_status(tweet, media_ids=media_ids)

            return original_tweet
        except tweepy.TweepError as e:  # SI ON LEVE UNE EXEPTION de l'API ALORS
            error.manage_error(41, e)  # On gère l'erreur en envoayant l'exeption

    def tweet_the_end(self, tweet):
        CONST = _Const()
        media_ids = []
        try:
            # On upload les graphiques
            pic1 = self.api.media_upload(CONST.IMG_PATH + "feu.gif")

            # On récupère leurs identifiants
            media_ids.append(pic1.media_id)
            self.api.create_media_metadata(media_ids[0],
                                           "Un feu d'artifice pour fêter l'arrivée aux 100 000 signatures")
            # On tweet le premier tweet
            original_tweet = self.api.update_status(tweet, media_ids=media_ids)
            return original_tweet
        except tweepy.TweepError as e:  # SI ON LEVE UNE EXEPTION de l'API ALORS
            error.manage_error(41, e)  # On gère l'erreur en envoayant l'exeption
