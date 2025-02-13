# Homework

```sql
create or replace table `ny_taxi_dataset.yellow-trip-nonpartitioned-data` 
as select * from `ny_taxi_dataset.yellow-trip-data-2024`;
```
### Question1
```sql
    select count(*) from `ny_taxi_dataset.yellow-trip-data-2024`
```

### Question 2
```sql
SELECT count(distinct PULocationID) FROM `engaged-plasma-448516-r0.ny_taxi_datasetyellow-trip-nonpartitioned-data`
```
<!-- ### Question 3
```sql

``` -->

### Question 4
```sql
SELECT count(*)  FROM `engaged-plasma-448516-r0.ny_taxi_dataset.yellow-trip-nonpartitioned-data`
WHERE fare_amount = 0
```

### Question 5
```sql
CREATE OR REPLACE TABLE `ny_taxi_dataset.yellow-trip-partitioned-data`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID  AS (
  SELECT * FROM `ny_taxi_dataset.yellow-trip-data-2024`
);
```

### Question 6
```sql
SELECT distinct VendorID FROM `engaged-plasma-448516-r0.ny_taxi_dataset.yellow-trip-nonpartitioned-data`
WHERE DATE(tpep_dropoff_datetime) >= '2024-03-01' 
AND DATE(tpep_dropoff_datetime) <= '2024-03-15'

SELECT distinct VendorID FROM `engaged-plasma-448516-r0.ny_taxi_dataset.yellow-trip-partitioned-data`
WHERE DATE(tpep_dropoff_datetime) >= '2024-03-01' 
AND DATE(tpep_dropoff_datetime) <= '2024-03-15'
```
<!-- 
### Question 7
```sql

```

### Question 8
```sql

```

### Question 9 -->
