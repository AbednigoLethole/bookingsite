import React from "react";
import { Link } from "react-router-dom";
import "./Sidebar.css";

const Sidebar = () => {
  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        <h2>Booking System</h2>
      </div>

      <ul className="menu">
        <li><Link to="/">View Booking Requests</Link></li>
        <li><Link to="/cars">Book Bakkie / Car</Link></li>
        <li><Link to="/seats">Book Flight Seat</Link></li>
        <li><Link to="/rooms">Book Accommodation</Link></li>
      </ul>
    </aside>
  );
};

export default Sidebar;
