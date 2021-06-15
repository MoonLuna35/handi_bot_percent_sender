import dataBase
import utilitaries


def percent_reached(twitter, str_tweet, img_path, lvl):
    db = dataBase.Db()
    db.uptdate_reached(lvl)
    t = twitter.tweet_percent(str_tweet, lvl)
    utilitaries.sendMail(0, tweet=t)


def level_reached(twitter, str_tweet, lvl):
    db = dataBase.Db()
    db.uptdate_reached(lvl)
    t = twitter.tweet_lvl(str_tweet, lvl)
    utilitaries.sendMail(0, lvl=lvl, str_tweet=str_tweet, tweet=t)

def the_end(twitter, str_tweet):
    db = dataBase.Db()
    db.uptdate_reached(100000)
    t = twitter.tweet_the_end(str_tweet)
    utilitaries.sendMail(0)