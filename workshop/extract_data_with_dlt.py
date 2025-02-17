import dlt
from dlt.sources.helpers.rest_client import RESTClient
from dlt.sources.helpers.rest_client.paginators import PageNumberPaginator


# your code is here
@dlt.resource(name="ny_taxi")
def paginated_getter():
    client = RESTClient(
        base_url="https://us-central1-dlthub-analytics.cloudfunctions.net",
        paginator=PageNumberPaginator(  
            base_page=1,   
            total_path=None    
        )
    ) 
    for page in client.paginate("data_engineering_zoomcamp_api"):   
        yield page

for page_data in paginated_getter():
    print(page_data)


pipeline = dlt.pipeline(
    pipeline_name="ny_taxi_pipeline",
    destination="duckdb",
    dataset_name="ny_taxi_data"
)

load_info = pipeline.run(paginated_getter())
print(load_info)

import duckdb

# Connect to the DuckDB database
conn = duckdb.connect(f"{pipeline.pipeline_name}.duckdb")
tables = conn.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'ny_taxi_data'").fetchdf()
print(tables)
print("_________________________")

# dataset = pipeline.dataset(dataset_type="default") 
# df = dataset["ny_taxi"].df()
df = pipeline.dataset(dataset_type="default").ny_taxi.df()
print(df.info)
print("_________________________")
with pipeline.sql_client() as client:
    res = client.execute_sql(
            """
            SELECT
            AVG(date_diff('minute', trip_pickup_date_time, trip_dropoff_date_time))
            FROM ny_taxi;
            """
        )
    # Prints column values of the first row
    print(res)
    print("_________________________")

conn.close()
