# pyspark-ecs-lambda-example

cd into docker-example folder

on local run

docker build -t test-image .

then

docker run --platform linux/amd64 -p 9000:8080 test-image

after that  you can test locally by performing post
powershell command

**Invoke-WebRequest -Uri "http://localhost:9000/2015-03-31/functions/function/invocations" -Method Post -Body '{}' -ContentType "application/json"**
