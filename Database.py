import psycopg2


def create_table():
    command = '''
        CREATE TABLE tratados (
                "Nombre del Tratado" VARCHAR,
                "Bilateral" BOOLEAN,
                "Lugar de Adopcion" VARCHAR,
                "Fecha de Adopcion" DATE,
                "Estado-Organismos" VARCHAR,
                "Temas" VARCHAR,
                "Naturaleza del Tratado" VARCHAR,
                "Depositario" VARCHAR,
                "Suscribio por Colombia" VARCHAR,
                "Vigente" BOOLEAN,
                "Fecha ley aprobatoria" VARCHAR,
                "Numero ley aprobatoria" VARCHAR,
                "Sentencia fecha ley" VARCHAR,
                "Sentencia numero" VARCHAR,
                "Decreto fecha diario oficial" VARCHAR,
                "Decreto numero diario oficial" VARCHAR,
                "Pais del tratado" VARCHAR,
                "Codigo de llamadas" VARCHAR,
                "Capital" VARCHAR,
                "Region" VARCHAR,
                "Subregion" VARCHAR,
                "Poblacion" VARCHAR,
                "Area" INTEGER,
                "Zona horaria" VARCHAR,
                "Monedas" VARCHAR,
                "Idiomas" VARCHAR,
                "Cantidad fronteras" INTEGER,
                "Diferencia horas zona horaria" REAL
        )'''
    try:
        conn = psycopg2.connect("dbname='{db}' user='{user}' host='{host}' port='{port}' password='{passwd}'".format(
                            user='postgres',
                            passwd='testadmin',
                            host='localhost',
                            port='5432',
                            db='tratados_colombia'))
        cur = conn.cursor()    
    # create table one by one
        cur.execute(command)
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
    create_table()