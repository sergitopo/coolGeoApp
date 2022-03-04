import os
import psycopg2

queryCache = {}
maxCacheSize = os.environ.get('MAX_CACHE_SIZE') if os.environ.get('MAX_CACHE_SIZE') else 5;
print(maxCacheSize)

def executeQuery(query: str):
    conn = psycopg2.connect(
        host="localhost",
        database="carto_test",
        #user=os.environ['DB_USERNAME'],
        user='carto_test',
        password='carto_test')

    # Open a cursor to perform database operations
    cur = conn.cursor()
    cur.execute(query)
    records = cur.fetchall()
    cur.close()
    return records


def getTurnoverInfoByPostalCodeId(postal_code_id):
    if postal_code_id in queryCache:
        print("reading from cache")
        return queryCache[postal_code_id]
    
    groupsByAge = {};
    turnovers_by_age_group_and_gender = executeQuery(f'select p_age, p_gender, sum from paystats_by_gender_and_age_group where postal_code_id = {postal_code_id}')
    for record in turnovers_by_age_group_and_gender:
        if record[0] not in groupsByAge:
            groupsByAge[record[0]] = [];
        groupsByAge[record[0]].append({"gender": record[1], "sum": record[2]})

    if len(queryCache) > maxCacheSize:
        print("deleting cache")
        queryCache.pop(list(queryCache)[0])
    queryCache[postal_code_id] = groupsByAge;
    print("adding cache")
    return groupsByAge

