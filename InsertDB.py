import psycopg2

def insert_data(data):
    try:
        conn = psycopg2.connect("dbname='{db}' user='{user}' host='{host}' port='{port}' password='{passwd}'".format(
                            user='postgres',
                            passwd='testadmin',
                            host='localhost',
                            port='5432',
                            db='tratados_colombia'))
        cur = conn.cursor()    

        args = [cur.mogrify('(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', x).decode('utf-8')
                for x in data]
        args_str = ', '.join(args)
        cur.execute('''INSERT INTO tratados VALUES'''
                    + args_str)
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
    insert_data()