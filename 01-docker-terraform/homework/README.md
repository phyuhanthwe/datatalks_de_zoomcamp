# Homework

## Question 1
```sh
docker run -it --entrypoint=bash python:3.12.8
```

## Question 3
```sql
select 
    count(case when trip_distance <= 1 then 1 end) as "Up to 1 mile",
    count(case when trip_distance > 1 and trip_distance <= 3 then 1 end) as "1-3 miles",
    count(case when trip_distance > 3 and trip_distance <= 7 then 1 end) as "3-7 miles",
    count(case when trip_distance > 7 and trip_distance <= 10 then 1 end) as "7-10 miles",
    count(case when trip_distance > 10 then 1 end) as "Over 10 miles"
from green_taxi_trips
where lpep_pickup_datetime >= '2019-10-01' and lpep_pickup_datetime < '2019-11-01';
```

## Question 4
```sql
select lpep_pickup_datetime, max(trip_distance) as longest_trip
from green_taxi_trips
group by lpep_pickup_datetime
order by longest_trip desc;
```

## Question 5
```sql
select tz."Zone", sum(total_amount) as total
from green_taxi_trips gt
join taxi_zones tz
on gt."PULocationID" = tz."LocationID"
where gt."lpep_pickup_datetime"::date = '2019-10-18'
group by tz."Zone"
having sum(total_amount) > 13000;
```

## Question 6
```sql
select tz_dropoff."Zone", max(tip_amount) as largest_tip
from green_taxi_trips as gt
join taxi_zones as tz_pickup
on gt."PULocationID" = tz_pickup."LocationID"
join taxi_zones as tz_dropoff
on gt."DOLocationID" = tz_dropoff."LocationID"
where tz_pickup."Zone" ='East Harlem North'
and gt."lpep_pickup_datetime" >= '2019-10-01'
and gt."lpep_pickup_datetime" < '2019-11-01'
group by tz_dropoff."Zone"
order by largest_tip desc
limit 1;
```