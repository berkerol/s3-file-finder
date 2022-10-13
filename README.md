# S3 File Finder

Tool to find files in S3 buckets that contains a certain substring.

## Overview

We need to use boto3 to list all files in buckets then check if a file name contains the substring.

Basically we need to create an s3 client then call `list_objects_v2` to get list of files and then search substring in every file name.

I didn't prefer to use s3 resource, which is `boto3.resource('s3').Bucket('name').objects.all()` because it is not safe to get every object in a bucket in a single call. There might be too many objects to get as a response or load into memory.

I used Python because it is suited for simple scripts to automate infrastructure tasks. I used Python 3.10 because it is the latest stable version. I used pipenv because it is a simple Python package manager. I used flake8 as linter.

## Running

```sh
$ pipenv install
$ pipenv shell # without this you can also do: pipenv run python3 s3_find.py
$ python3 s3_find.py # there is already an example commented line that calls the function, you can use it or call it in your file after importing
```

## Extra Features

1. List of buckets to search in: It was an easy addition and also useful because sometimes you might not know which bucket to search.
2. Prefix: It was an easy addition again and might be useful if you have a clue.
3. Extension: In the description, it was stated as text file. So I assumed that I was searching a `.txt` file but I didn't want to hardcode it instead put it as parameter.
4. Access keys: You can search in accounts other than the configured one with `aws configure`.

## References

* [boto3 S3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html)
