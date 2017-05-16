# neogeodis

Demonstate the functions GEOADD and GEORADIUS of Redis


## Run the demo

This requires you to have a running instance of Redis at port 6379. You can do this with Docker:

```
docker run -it -p 6379 --name geodis-redis redis
```

Then to neogeodis. First, run:

```
python import.py
```

Then:

```
python neogeo.py
```


Sample data from [Spatial key's Sample insurance portfolio](https://support.spatialkey.com/spatialkey-sample-csv-data/)
