__author__ = 'gabriel'
from django.db import connection
import json

def get_destinations_travel_times(def_name='Salisbury'):

    qry = """SELECT t.travel_time, ST_AsGeoJSON(pd.point) FROM traveltime_traveltime t
    JOIN traveltime_poi po ON t.origin_id = po.rid
    JOIN traveltime_poi pd ON t.destination_id = pd.rid
    WHERE po.def_name = '{0}';""".format(def_name)

    cur = connection.cursor().cursor
    cur.execute(qry)
    res = cur.fetchall()
    return res
    # return [x[0] for x in res], [str(x[1]) for x in res]
