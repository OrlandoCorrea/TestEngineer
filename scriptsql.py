import psycopg2

def querysql():
    try:
        conn = psycopg2.connect("dbname='{db}' user='{user}' host='{host}' port='{port}' password='{passwd}'".format(
                            user='postgres',
                            passwd='testadmin',
                            host='localhost',
                            port='5432',
                            db='tratados_colombia'))
        cur = conn.cursor()    
        sql_file = open('querysql.sql','r')
        cur.execute(sql_file.read())
    # close communication with the PostgreSQL database server
        cur.close()
    # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    querysql()