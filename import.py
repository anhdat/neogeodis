import csv
import redis


redisConn = redis.StrictRedis(db=7, host='localhost', port=6379)


def import_data(file_path):
    with open(file_path) as data_file:
        reader = csv.reader(data_file)
        next(reader, None)  # skip the headers
        for row in reader:
            user_id = row[0]
            lat = float(row[13])
            lon = float(row[14])
            try:
                save_user_location(user_id, lat, lon)
            except redis.exceptions.ResponseError as e:
                print(e)


def save_user_location(user_id, lat, lon):
    key = 'user_last_visited'
    redisConn.geoadd(key, lat, lon, user_id)


if __name__ == '__main__':
    FILE_PATH = './FL_insurance_sample.csv'
    import_data(FILE_PATH)
