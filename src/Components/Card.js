"use client";

import { useState } from "react";
import StockManagement from "./StockManagement";

const ProductCard = ({ product, stock }) => {
  const [modalOpen, setModelOpen] = useState(false);
  console.log({stock});
  

  const onCardClick = () => {
    if (stock) {
      setModelOpen(true);
    }
  };

  return (
    <div>
      {modalOpen && <StockManagement product={product} close={()=>setModelOpen(false)}/>}
      <div className="product-card" onClick={onCardClick}>
        <img
          src={product.image}
          alt={product.name}
          className="product-image"
          width={200}
          height={200}
        />
        <h2 className="product-title">{product.name}</h2>
        <p className="product-price">{stock?<>In Stock :<span className="product-price">{product.stock}</span></>:`${product.price} ₹` } </p>
      </div>
    </div>
  );
};

export default ProductCard;
