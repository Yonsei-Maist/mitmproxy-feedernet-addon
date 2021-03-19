"""
library for using database
@author Chanwoo Gwon, Yonsei Univ. Researcher, since 2020.05.~
@Date 2021.03.18
"""
import pymysql


class Connection:
    def __init__(self, host, database, user, password):
        self._host = host
        self._database = database
        self.user = user
        self.password = password
        self._conn = self.create_connection()

    def create_connection(self):
        return pymysql.connect(host=self._host,
                               database=self._database,
                               user=self.user,
                               password=self.password,
                               charset='utf8',
                               cursorclass=pymysql.cursors.DictCursor
                               )

    def get_connection(self):
        if self._conn is None:
            self._conn = self.create_connection()
        return self._conn

    def write(self, sql, *param):
        with self as conn:
            curs = conn.cursor()
            ok = curs.execute(sql, *param)

        return {'rows': ok}


class DataManager(Connection):
    def insert_data(self, request_method, request_url, request_contents, response_url, response_contents):
        sql = "" \
              "INSERT INTO tbl_packet " \
              " (" \
              "     var_method" \
              "     , var_request_url" \
              "     , var_request_contents" \
              "     , var_response_url" \
              "     , var_response_contents" \
              " )" \
              "VALUES" \
              " (" \
              "     '{0}'" \
              "     , '{1}'" \
              "     , '{2}'" \
              "     , '{3}'" \
              "     , '{4}'" \
              " )".format(request_method, request_url, request_contents, response_url, response_contents)
        return self.write(sql)
