import React, { useEffect, useState } from "react";
import { getCars } from "../api/bookings";
import "./CarsList.css";

const getCarImage = (type) => {
  if (!type) return "/sedan.png";

  const normalized = type.toLowerCase().trim();

  if (normalized.includes("bakkie") || normalized.includes("pickup")) {
    return "/bakkie.png";
  }

  return "/sedan.png";
};

const CarsList = () => {
  const [cars, setCars] = useState([]);

  useEffect(() => {
    const load = async () => setCars(await getCars());
    load();
  }, []);

  return (
    <div>
      <h1>All Vehicles</h1>

      <div className="top-controls">
        <input placeholder="Search vehicles..." />
        <button>Filter</button>

        <div className="view-toggle">
          <span>Grid</span>
          <span>List</span>
          <span>Calendar</span>
        </div>
      </div>

      <div className="cars-grid">
        {cars.map((car) => (
          <div
            key={car.car_registration}
            className={`car-card ${car.available === "Y" ? "" : "disabled"}`}
          >
            <img
              src={getCarImage(car.car_type)}
              alt={car.car_type}
              className="car-img"
            />

            <h3>{car.car_type}</h3>
            <p className="reg">{car.car_registration}</p>
            <p>{car.capacity} Seats</p>

            <button disabled={car.available !== "Y"}>
              {car.available === "Y" ? "Book Now" : "Unavailable"}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default CarsList;
