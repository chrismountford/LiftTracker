import MySQLConn


def dates_for_graph():
    with MySQLConn.conn as cursor:
        cursor.execute("SELECT date FROM Lifts ORDER BY date")
        dates_fetched = cursor.fetchall()

        dates_to_plot = []
        for i, date in enumerate(da['date'] for da in dates_fetched):
            dates_to_plot.append(date)

    return dates_to_plot


def squats_for_graph():
    with MySQLConn.conn as cursor:
        cursor.execute("SELECT squat FROM Lifts ORDER BY date")
        squats_fetched = cursor.fetchall()

        squats_to_plot = []
        for i, squat in enumerate(s['squat'] for s in squats_fetched):
            squats_to_plot.append(squat)

    return squats_to_plot


def benchs_for_graph():
    with MySQLConn.conn as cursor:
        cursor.execute("SELECT bench FROM Lifts ORDER BY date")
        bench_fetched = cursor.fetchall()

        bench_to_plot = []
        for i, bench in enumerate(b['bench'] for b in bench_fetched):
            bench_to_plot.append(bench)

    return bench_to_plot


def deads_for_graph():
    with MySQLConn.conn as cursor:
        cursor.execute("SELECT deadlift FROM Lifts ORDER BY date")
        deadlifts_fetched = cursor.fetchall()

        deadlifts_to_plot = []
        for i, deadlift in enumerate(d['deadlift'] for d in deadlifts_fetched):
            deadlifts_to_plot.append(deadlift)

    return deadlifts_to_plot

all_lifts = squats_for_graph() + benchs_for_graph() + deads_for_graph()
