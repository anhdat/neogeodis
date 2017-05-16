import redis


redisConn = redis.StrictRedis(db=7, host='localhost', port=6379)


def geolocation(lat, lon, radius):
    key = 'user_last_visited'
    return redisConn.georadius(key, lat, lon, radius, withdist=True, withcoord=True, unit='km')


if __name__ == '__main__':
    LAT = 28.029942
    LON = -82.666489
    RADIUS = 0.5
    print(geolocation(LAT, LON, RADIUS))
