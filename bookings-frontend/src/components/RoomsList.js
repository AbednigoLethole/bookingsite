import React, { useEffect, useState } from "react";
import { getRooms } from "../api/bookings";
import "./RoomsList.css";

const RoomsList = () => {
  const [rooms, setRooms] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedRoom, setSelectedRoom] = useState(null);

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

  // Group rooms by house
  const groupedRooms = rooms.reduce((acc, room) => {
    const houseCode = room.room_id.slice(0, 4); // e.g., KFH1
    if (!acc[houseCode]) acc[houseCode] = [];
    acc[houseCode].push(room);
    return acc;
  }, {});

  const houseNames = {
    KFH1: "Klerefontein House 1",
    KFH3: "Klerefontein House 3",
    LBH1: "Losberg House 1",
  };

  return (
    <div className="rooms-page">
      <h2>Rooms</h2>
      {Object.entries(groupedRooms).map(([houseCode, houseRooms]) => (
        <div key={houseCode} className="house-group">
          <h3>{houseNames[houseCode] || houseCode}</h3>
          <div className="rooms-container">
            {houseRooms.map((room) => (
              <div
                key={room.room_id}
                className={`room-block ${
                  room.available === "Y" ? "available" : "unavailable"
                } ${selectedRoom === room.room_id ? "selected" : ""}`}
                onClick={() =>
                  room.available === "Y" && setSelectedRoom(room.room_id)
                }
              >
                <h4>{room.room_id}</h4>
                <p>{room.bed_type}</p>
              </div>
            ))}
          </div>
        </div>
      ))}

      <button
        disabled={!selectedRoom}
        onClick={() => alert(`You selected Room ${selectedRoom}`)}
        className="confirm-btn"
      >
        Choose Room
      </button>
    </div>
  );
};

export default RoomsList;
