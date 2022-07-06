from google.cloud import storage

def copy_blobs_with_prefix(source_bucket_name, destination_bucket_name,prefix, delimiter=None):


    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(source_bucket_name, prefix=prefix, delimiter=delimiter)

    source_bucket = storage_client.bucket(source_bucket_name)
    destination_bucket = storage_client.bucket(destination_bucket_name)

    
    for blob in blobs:
        #source_blob = source_bucket.blob(blob)
        blob_copy = source_bucket.copy_blob(
        blob, destination_bucket,blob.name
    )

    
copy_blobs_with_prefix('hydemo002','hydemo001','demo')