import logo from "./logo.svg";
import "./App.css";
import ProductInventoryForm from "./Pages/ProductInsert";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Header from "./Components/Header";
import ProductCard from "./Components/Card";
import { useEffect, useState } from "react";
import Home from "./Pages/Home";
import StockManagement from "./Components/StockManagement";
import StockDetails from "./Pages/StockDetails";

function App() {
  
  return (
    <div className="App">
      <Router>
        <Header />

        <Routes>
          <Route path="/create-products" element={<ProductInventoryForm />} />
          
          <Route path="/" element={<Home />} />
          <Route path="/stock-management" element={<StockDetails />} />

          

        </Routes>
      </Router>
    </div>
  );
}

export default App;
