import pymysql


def query(sql: str, params: dict = None, model=None):
    '''使用pymysql查詢並塞進ViewModel'''
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Sunsda',
        database='company',
        cursorclass=pymysql.cursors.DictCursor
    )
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            rows = cursor.fetchall()
            debugSQL = cursor.mogrify(sql, params)
            print('debugSQL', debugSQL)
            if model:
                return [model(**row) for row in rows]
            return rows
