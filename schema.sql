CREATE TABLE plant (
     id INT,
     name TEXT,
     PRIMARY KEY(id)
) ;

CREATE TABLE conditions(
     plantID INT,
     time TIMESTAMP,
     lightIntensity FLOAT(5,3),
     soilHumidity FLOAT(5,3),
     soilTemperature FLOAT(5,3),
     airTemperature FLOAT(5,3),
     FOREIGN KEY(plantID) REFERENCES plant(id),
     PRIMARY KEY(plantID, time)
) ;
