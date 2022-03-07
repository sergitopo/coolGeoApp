import os
import psycopg2

queryCache = {}
maxCacheSize = os.environ.get('MAX_CACHE_SIZE') if os.environ.get('MAX_CACHE_SIZE') else 5;
print(maxCacheSize)

def executeQuery(query: str):
    conn = psycopg2.connect(
        host=os.environ['POSTGRES_HOST'],
        database=os.environ['POSTGRES_DB'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD'])

    # Open a cursor to perform database operations
    cur = conn.cursor()
    cur.execute(query)
    records = cur.fetchall()
    cur.close()
    return records


def getTurnoverInfoByPostalCodeId(postalCode):
    if postalCode in queryCache:
        print("reading from cache")
        return queryCache[postalCode]
    
    groupsByAge = {};
    turnovers_by_age_group_and_gender = executeQuery(f'select p_age, p_gender, sum from paystats_by_gender_and_age_group where code = {postalCode}')
    for record in turnovers_by_age_group_and_gender:
        if record[0] not in groupsByAge:
            groupsByAge[record[0]] = [];
        groupsByAge[record[0]].append({"gender": record[1], "sum": record[2]})

    if len(queryCache) > maxCacheSize:
        print("deleting cache")
        queryCache.pop(list(queryCache)[0])
    queryCache[postalCode] = groupsByAge;
    print("adding cache")
    return groupsByAge


def getBoundaryPostalCodesStats(geometry: str, startdate: str, enddate: str):
    query = f"""
        SELECT pc.code, sum(ps.amount) as sum, st_asText(pc.the_geom) as geometry
        FROM paystats ps
        JOIN postal_codes pc using(postal_code_id)
        WHERE ST_Intersects(pc.the_geom, ST_GeomFromText('{geometry}', 4326))
    """
    if startdate and enddate:
        query = query + f" AND ps.p_date between '{startdate}' and '{enddate}'"

    query = query + " GROUP BY pc.the_geom, pc.code;"
    postal_codes_with_stats = executeQuery(query)

    return postal_codes_with_stats
    

