import { BrowserRouter, Routes, Route } from "react-router-dom";
import DashboardLayout from "./layout/DashboardLayout";
import CarsList from "./components/CarsList";
import SeatsList from "./components/SeatsList";
import RoomsList from "./components/RoomsList";

function App() {
  return (
    <BrowserRouter>
      <DashboardLayout>
        <Routes>
          <Route path="/" element={<h1>Booking Requests Coming Soon</h1>} />
          <Route path="/cars" element={<CarsList />} />
          <Route path="/seats" element={<SeatsList />} />
          <Route path="/rooms" element={<RoomsList />} />
        </Routes>
      </DashboardLayout>
    </BrowserRouter>
  );
}

export default App;
