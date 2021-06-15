#
#   dev's Twitter : @__MoonLuna__
#   project : handi bot petition for the AAH
#
###################################################
from datetime import datetime

import mysql.connector as connector

from mysql.connector import errorcode

import CONST
import error
import utilitaries
from CONST import _Const


class Db:
    cnx = None
    def __init__(self):  # On tente d'acceder à la base de donnée
        CONST = _Const()
        config = {
            "user": CONST.DB_NAME,
            "password": CONST.DB_PWD,
            "host": CONST.DB_HOST,
            "database": CONST.DB_DATA_BASE
        }

        try:
            self.cnx = connector.connect(**config)
        except connector.Error as err:  # SI UNE EXEPTION EST LEVEE ALORS
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:  # Si c'est une erreur de mot de passe
                error.manage_error(22)  # On gère avec le gestionaire d'erreur
            elif err.errno == errorcode.ER_BAD_DB_ERROR:  # Si la base de donnée n'existe pas
                error.manage_error(23)  # On gère avec le gestionaire d'erreur
            else:  # SI c'est une autre erreur
                error.manage_error(21)  # On gère avec le gestionaire d'erreur
    #33%
    #40 000
    #50%
    #60 000
    #70 000
    #75%
    #80%
    #90%
    #95%

    def uptdate_reached(self, lvl):
        query = "UPDATE level SET is_reached=1 WHERE level=" + str(lvl)
        cursor = self.cnx.cursor()
        cursor.execute(query)
        self.cnx.commit()

    def lvl_is_tweeted(self, lvl):
        query = "SELECT * FROM level WHERE level=" + str(lvl) + " AND is_reached=1"
        cursor = self.cnx.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) > 0:
            return True
        else:
            return False

    def make_backup(self):
        CONST = _Const()
        cursor = self.cnx.cursor()
        query = "SELECT * FROM petition"
        c = 1
        cursor.execute(query)
        result = cursor.fetchall()
        str_backup = "-- bakup for handi_bot : " + datetime.now().strftime("%d-%m-%Y %h:%m:%s") + "\n\n" + \
                 "SET SQL_MODE = \"NO_AUTO_VALUE_ON_ZERO\";\n" + \
                 "START TRANSACTION;\n" + \
                 "SET time_zone = \"+00:00\";\n\n" + \
                 "-- Structure of table petition : \n\n" + \
                 "CREATE TABLE `petition` (\n" + \
                 "`id_petition` int(11) NOT NULL,\n" + \
                 "`date` datetime NOT NULL DEFAULT current_timestamp(),\n" + \
                 "`nb` int(11) NOT NULL\n" + \
                 ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n\n" + \
                 "ALTER TABLE `petition`\n" + \
                 "ADD PRIMARY KEY (`id_petition`); \n\n" +\
                 "-- Datas : \n\n" + \
                 "INSERT INTO `petition` (`id_petition`, `date`, `nb`) VALUES \n"

        for (identifier, date, nb) in result:  # On parcours le curseur
            str_backup += "(" + str(identifier)+", \'" + date.strftime("%Y-%m-%d %H:%M:%S") + "\', " + str(nb) + ")"
            if c != len(result):
                str_backup += ", \n"
            else:
                str_backup += "; \n\n"
            c += 1
        str_backup += "COMMIT;"
        backup = open(CONST.IMG_PATH + datetime.now().strftime("%d-%m-%Y") + "/backup.sql", "w")
        backup.write(str_backup)
        backup.close()

