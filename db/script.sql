CREATE DATABASE IF NOT EXISTS events_storage;

USE events_storage;

CREATE TABLE IF NOT EXISTS coordinates (
    id int NOT NULL AUTO_INCREMENT,
    latitude decimal(12, 10) NOT NULL,
    longitude decimal(12, 10) NOT NULL,
    location_key int NOT NULL,
   	PRIMARY KEY (id),
   	UNIQUE KEY unique_lat_lon (latitude, longitude)
);


CREATE TABLE IF NOT EXISTS event (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255),
    initial_date varchar(20) NOT NULL,
    final_date varchar(20) NOT NULL,
    coordinates_id int NOT NULL,
    forecast varchar(255),
   	PRIMARY KEY (id),
   	FOREIGN KEY (coordinates_id) REFERENCES coordinates(id)
);