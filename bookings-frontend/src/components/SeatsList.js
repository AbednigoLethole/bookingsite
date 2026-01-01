import React, { useEffect, useState } from "react";
import { getSeats } from "../api/bookings";
import "./SeatsList.css";

const SeatsList = () => {
  const [seats, setSeats] = useState([]);
  const [loading, setLoading] = useState(true);

  const [departure, setDeparture] = useState("CPT");
  const [destination, setDestination] = useState("LSB");
  const [isReturnTrip, setIsReturnTrip] = useState(false);

  const [selectedSeat, setSelectedSeat] = useState(null);

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

  // --- Build route pattern like CPT_TO_LSB ---
  const routeKey = `${departure}_TO_${destination}`;

  // --- Filter seats for selected route (max 8) ---
  const filteredSeats = seats
    .filter((seat) => seat.seat_dest_id.startsWith(routeKey))
    .slice(0, 8);

  const handleSelect = (seat) => {
    if (!seat.available) return;
    setSelectedSeat(seat.seat_dest_id);
  };

  return (
    <div className="seats-container">
      <h2>Flight Seat Booking</h2>

      {/* ===== Dropdown Controls ===== */}
      <div className="flight-controls">
        <div>
          <label>Departure:</label>
          <select value={departure} onChange={(e) => setDeparture(e.target.value)}>
            <option value="CPT">Cape Town</option>
            <option value="LSB">Losberg</option>
            <option value="HLA">Lanseria</option>
          </select>
        </div>

        <div>
          <label>Destination:</label>
          <select value={destination} onChange={(e) => setDestination(e.target.value)}>
            <option value="LSB">Losberg</option>
            <option value="CPT">Cape Town</option>
            <option value="HLA">Lanseria</option>
          </select>
        </div>

        <div className="return-box">
          <label>
            <input
              type="checkbox"
              checked={isReturnTrip}
              onChange={(e) => setIsReturnTrip(e.target.checked)}
            />
            Return Trip
          </label>
        </div>
      </div>

      {/* ===== Seats Grid ===== */}
      <div className="seats-grid">
        {filteredSeats.length === 0 && <p>No seats available for this route.</p>}

        {filteredSeats.map((seat, index) => (
          <div
            key={seat.id}
            className={`seat-box 
              ${seat.available ? "available" : "unavailable"}
              ${selectedSeat === seat.seat_dest_id ? "selected" : ""}`}
            onClick={() => handleSelect(seat)}
          >
            Seat {index + 1}
            <div className="seat-id">{seat.seat_dest_id}</div>
          </div>
        ))}
      </div>

      {/* ===== Bottom Right Button ===== */}
      <button
        className={`choose-seat-btn ${selectedSeat ? "active" : ""}`}
        disabled={!selectedSeat}
      >
        {selectedSeat ? `Chosen Seat: ${selectedSeat}` : "Choose Seat"}
      </button>
    </div>
  );
};

export default SeatsList;
