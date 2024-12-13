import { Link } from "react-router-dom";
import { useState } from "react";

const Header = () => {
  
  const [activeLink, setActiveLink] = useState("/");

  const handleClick = (path) => {
    setActiveLink(path); 
  };

  return (
    <header className="header">
      <nav>
        <ul>
          <li>
            <Link
              className={`h2 ${activeLink === "/" ? "active" : ""}`}
              to="/"
              onClick={() => handleClick("/")}
            >
              Home
            </Link>
          </li>
          <li>
            <Link
              className={`h2 ${activeLink === "/create-products" ? "active" : ""}`}
              to="/create-products"
              onClick={() => handleClick("/create-products")}
            >
              Add Products
            </Link>
          </li>
          <li>
            <Link
              className={`h2 ${activeLink === "/stock-management" ? "active" : ""}`}
              to="/stock-management"
              onClick={() => handleClick("/stock-management")}
            >
              Stock Management
            </Link>
          </li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
