FROM public.ecr.aws/lambda/python:3.10

COPY . ${LAMBDA_TASK_ROOT}

RUN yum update -y

RUN yum -y remove java

RUN yum install -y \
    java-1.8.0-openjdk \
    java-1.8.0-openjdk-devel 

RUN yum install unzip -y

RUN python -m pip install --upgrade pip

RUN pip --no-cache-dir install pyspark>=3.5

RUN unzip ${LAMBDA_TASK_ROOT}/test_libraries.zip

CMD ["lambda_function.lambda_handler"]
