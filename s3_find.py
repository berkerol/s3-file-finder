import boto3


def find_file(s3_bucket_names: list[str], substring: str, prefix='',
              extension=None, access_key_id=None, secret_access_key=None):

    if access_key_id and secret_access_key:
        s3 = boto3.client(
            's3',
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key
        )
    else:
        s3 = boto3.client('s3')

    result = []
    for s3_bucket_name in s3_bucket_names:
        response = s3.list_objects_v2(Bucket=s3_bucket_name, Prefix=prefix)
        while True:
            for obj in response['Contents']:
                name = obj['Key']
                if substring in name and \
                        (not extension or name.endswith(extension)):
                    result.append(s3_bucket_name + '/' + name)
            if 'NextContinuationToken' in response:
                token = response['NextContinuationToken']
                response = s3.list_objects_v2(Bucket=s3_bucket_name,
                                              Prefix=prefix,
                                              ContinuationToken=token)
            else:
                break

    return result


# print('\n'.join(find_file(['berkerol'], '0006')))
