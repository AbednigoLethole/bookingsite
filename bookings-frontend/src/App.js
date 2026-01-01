import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { useState, useEffect } from "react";
import DashboardLayout from "./layout/DashboardLayout";
import CarsList from "./components/CarsList";
import SeatsList from "./components/SeatsList";
import RoomsList from "./components/RoomsList";
import Login from "./components/Login";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    const loggedIn = localStorage.getItem("isLoggedIn");
    if (loggedIn === "true") setIsLoggedIn(true);
  }, []);

  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={
            isLoggedIn ? <Navigate to="/dashboard" replace /> : <Login setIsLoggedIn={setIsLoggedIn} />
          }
        />

        {/* Removed the "/*" from the path. Child routes are nested inside. */}
        <Route
          path="/dashboard"
          element={isLoggedIn ? <DashboardLayout /> : <Navigate to="/" replace />}
        >
          {/* Use "index" for the default view at /dashboard */}
          <Route index element={<h1>Booking Requests Coming Soon</h1>} />
          
          {/* These paths are now relative to /dashboard */}
          <Route path="cars" element={<CarsList />} />
          <Route path="seats" element={<SeatsList />} />
          <Route path="rooms" element={<RoomsList />} />
        </Route>

        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;