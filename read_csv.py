import boto3
import pandas as pd

def read_csv_from_s3(bucket, prefix):
    s3 = boto3.client('s3',
                      aws_access_key_id="AKIA6NFIZTMI7OVK5WMX",
                      aws_secret_access_key="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")
    result = s3.list_objects(Bucket=bucket, Prefix=prefix)
    df_list = []
    for content in result.get("Contents"):
        key = content.get("Key")
        if key.endswith(".csv"):
            obj = s3.get_object(Bucket=bucket, Key=key)
            df = pd.read_csv(obj['Body'])
            df_list.append(df)
    return pd.concat(df_list, ignore_index=True)

# Call the function and store the result in a variable
#df = read_csv_from_s3('contiamo-challenge', 'data-engineer-challenge/')