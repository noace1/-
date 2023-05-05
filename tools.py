import pymysql


class Text_mysql():
    can = dict(host='localhost', port=3306, user='root', password='123456',
               db=f'music', charset='utf8')

    def __init__(self) -> None:
        self.con = pymysql.connect(**Text_mysql.can)
        self.cursor = self.con.cursor()

    def close(self) -> None:
        if self.cursor:
            self.cursor.close()
        if self.con:
            self.con.close()

    def dml(self, sql, *args):
        try:
            self.cursor.execute(sql, args)
            id = self.con.insert_id()
            self.con.commit()
            return id
        except Exception as e:
            print(e)
            if self.con:
                self.con.rollback()
        finally:
            self.close()
    def dql(self, sql, number, *args):
        try:
            self.cursor.execute(sql, args)
            return self.cursor.fetchmany(number)
        except Exception as e:
            print(e)
            if self.con:
                self.con.rollback()
        finally:
            self.close()

if __name__ == '__main__':
        sql = 'select employee_id, last_name, salary from employees where last_name = %s or last_name = %s'
        a = Text_mysql()
        c = a.dql(sql, 5, 'king', 'chen')
        print(c)