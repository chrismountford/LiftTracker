import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='pa55w0rd',
                       db='lifttracker',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

# test insert:
# try:
#     with conn.cursor() as cursor:
#         cursor.execute("""
#         insert into Lifts (user, squat, bench, deadlift) values ("Chris", 205, 130, 205)
#         """)
#
#     conn.commit()
#
#     with conn.cursor() as cursor:
#         cursor.execute("""
#         select * from Lifts
#         """)
#         print(cursor.fetchone())
#
# finally:
#     conn.close()
