#coding:utf-8
import psycopg2



class DBConn (object):
    def __init__(self, dbname, user, host, port, password):
        try:
            self.__conn = psycopg2.connect("dbname='"+dbname+"' user='"+user+"'"
                        "host='"+host+"' port ="+port+" password='"+password+"'")
        except:
            raise IOError('DataBase Unreacheble')
        self.cur = self.__conn.cursor()
    '''
    """Select ***""" - str format
    '''
    def select(self, executestr):
        self.cur.execute(executestr)
        return self.cur.fetchall()

    def close(self):
        self.__conn.close()

