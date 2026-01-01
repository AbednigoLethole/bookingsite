import React from "react";
import { Outlet } from "react-router-dom";
import Sidebar from "../components/Sidebar";
import "./DashboardLayout.css";

const DashboardLayout = () => {
  return (
    <div className="dashboard-layout">
      <Sidebar />

      <main className="dashboard-content">
        {/* THIS IS CRUCIAL: Outlet renders nested pages */}
        <Outlet />
      </main>
    </div>
  );
};

export default DashboardLayout;
