from google.cloud import bigquery, storage

def gcs_to_bq(table_name, file_prefix):
    client = bigquery.Client()
    storage_client = storage.Client()

    bucket_name = "engaged-plasma-448516-r0-de-dw-bucket"
    table_id = f"engaged-plasma-448516-r0.ny_taxi_dataset.{table_name}"
    
    # Get all files matching the prefix
    bucket = storage_client.bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=file_prefix)  # List files with the prefix
    file_uris = [f"gs://{bucket_name}/{blob.name}" for blob in blobs]

    if not file_uris:  # If no files found, print an error and exit
        print(f"No files found in gs://{bucket_name}/{file_prefix}")
        return

    job_config = bigquery.LoadJobConfig(
    #     schema=[
    #     bigquery.SchemaField("passenger_count", "FLOAT64"),  # Correct type
    # ],
        source_format=bigquery.SourceFormat.PARQUET,
        autodetect=True
    )

    load_job = client.load_table_from_uri(file_uris, table_id, job_config=job_config)
    load_job.result()  # Wait for the job to complete

    print(f"Successfully loaded {len(file_uris)} files into {table_id}")

gcs_to_bq("green_trip_data_2019", "green/green_tripdata_2019")
