import pymysql
from tkinter import messagebox

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='pa55w0rd',
                       db='lifttracker',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)


def conn_update(date, squat, bench, deadlift):
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
            INSERT INTO Lifts (user, date, squat, bench, deadlift) VALUES ('Chris', "{0}", {1}, {2}, {3})
            """.format(date, squat, bench, deadlift))  # TODO: re-format date

        conn.commit()

        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Lifts #WHERE id = MAX(id)")
            # print(cursor.fetchone())

    except pymysql.err.ProgrammingError:
        messagebox.showwarning(title="Error Writing to Database",
                               message="Error in SQL syntax. Make sure all boxes are completed")

    finally:
        pass


def return_all_dates():
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT date from Lifts")
            all_dates_fetched = cursor.fetchall()

            all_dates = []
            for i, date in enumerate(d['date'] for d in all_dates_fetched):
                all_dates.append(date)

            return all_dates

    finally:
        pass

