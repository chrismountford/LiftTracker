import MySQLConn


with MySQLConn.conn as cursor:
    cursor.execute("SELECT date FROM Lifts ORDER BY date")
    dates_fetched = cursor.fetchall()

    dates_to_plot = []
    for i, date in enumerate(da['date'] for da in dates_fetched):
        dates_to_plot.append(date)

    cursor.execute("SELECT squat FROM Lifts ORDER BY date")
    squats_fetched = cursor.fetchall()

    squats_to_plot = []
    for i, squat in enumerate(s['squat'] for s in squats_fetched):
        squats_to_plot.append(squat)

    cursor.execute("SELECT bench FROM Lifts ORDER BY date")
    bench_fetched = cursor.fetchall()

    bench_to_plot = []
    for i, bench in enumerate(b['bench'] for b in bench_fetched):
        bench_to_plot.append(bench)

    cursor.execute("SELECT deadlift FROM Lifts ORDER BY date")
    deadlifts_fetched = cursor.fetchall()

    deadlifts_to_plot = []
    for i, deadlift in enumerate(d['deadlift'] for d in deadlifts_fetched):
        deadlifts_to_plot.append(deadlift)

