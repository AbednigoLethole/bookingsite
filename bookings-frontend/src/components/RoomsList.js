import React, { useEffect, useState } from "react";
import { getRooms } from "../api/bookings";



const RoomsList = () => {
  const [rooms, setRooms] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchRooms = async () => {
      try {
        const data = await getRooms();
        setRooms(data);
      } catch (error) {
        console.error("Error fetching rooms:", error);
      } finally {
        setLoading(false);
      }
    };
    fetchRooms();
  }, []);

  if (loading) return <p>Loading rooms...</p>;

  return (
    <div>
      <h2>Rooms</h2>
      <ul>
        {rooms.map((room) => (
          <li key={room.room_id}>
            {room.room_id} - {room.bed_type} -{" "}
            {room.available === "Y" ? "Available" : "Not Available"}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default RoomsList;
