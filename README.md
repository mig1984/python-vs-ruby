## microframework benchmarks

### testing URLs:

```
/
  return string 'Hello World!'


everything under /api is Content-Type: application/json:

/api/current-time  
  {'timestamp'=>12345678}

/api/bigdata  
  {0=>[99, 98, 97, .. 0],  
   1=>[99, 98, 97, .. 0],  
   ..  
   1999=>[99, 98, 97, .. 0] }  

TODO in python (not implemented yet)  
/api/INTEGER/[a-z]+  
  {"int"=>INTEGER, "regex"=>"matching_string"}  
  example: http://127.0.0.1:8080/api/12/foobar  
  returns json {"int":12,"regex":"foobar"}  

other URLs return error 404
```

### how to run a benchmark

```bash
  cd ruby-roda  
  ./install # expects ruby version 3 installed  
  ./start   # starts webserver on port 8080 with 4 workers
```

```bash
  cd python-fastapi  
  ./install # expects python version 3 installed  
  ./start   # starts webserver on port 8080 with 4 workers
```

### example benchmarks

ab -n 50000 -c 1000 http://127.0.0.1:8080/api/current-time

my results (4 cores):
  python Requests per second:    2990.25 [#/sec] (mean)  
  ruby Requests per second:    14904.16 [#/sec] (mean)

ab -n 1000 -c 100 http://127.0.0.1:8080/api/bigdata

my results (4 cores):
  python Requests per second:    6.59 [#/sec] (mean)  
  ruby Requests per second:    117.84 [#/sec] (mean)


## direcotries bench1-*

is just the algorithm used in the /api/bigdata

