import React, { useEffect, useState } from "react";
import { getSeats } from "../api/bookings";

const SeatsList = () => {
  const [seats, setSeats] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchSeats = async () => {
      try {
        const data = await getSeats();
        setSeats(data);
      } catch (error) {
        console.error("Error fetching seats:", error);
      } finally {
        setLoading(false);
      }
    };
    fetchSeats();
  }, []);

  if (loading) return <p>Loading seats...</p>;

  return (
    <div>
      <h2>Seats</h2>
      <ul>
        {seats.map((seat) => (
          <li key={seat.id}>
            {seat.seat_dest_id} - {seat.available ? "Available" : "Not Available"}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SeatsList;
