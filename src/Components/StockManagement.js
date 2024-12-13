import React, { useEffect, useState } from "react";

const StockManagement = ({ product, close }) => {
  const [productStock, setProductStock] = useState(0);
  useEffect(() => {
    if(product?.stock){
        setProductStock(product.stock)
    }
  }, [product])
  
 

  const handleSubmit = () => {
    const updatedProduct={
        ...product,
        stock:productStock,
      }
    console.log(updatedProduct);

  };

  return (
    <>
      <div className="loginForm stockContainer">
        <h2 className="h3">Product Stock Details</h2>
        <div className="flex">
          <div className="inputGroup">
            <input
              type="text"
              value={product.name}
              placeholder="Product Name"
              required
            />
          </div>
          <div className="inputGroup">
            <input
              style={{ marginLeft: "16px" }}
              type="text"
              value={product.price}
              placeholder="Price"
            />
          </div>
        </div>
        <div className="inputGroup">
          <input
            type="text"
            value={productStock}
            onChange={(e) => setProductStock(e.target.value)}
            placeholder="Quantity"
          />
        </div>

        <div className="flex">
          <button
            type="submit"
            className="loginButton1"
            style={{ marginRight: "8px" }}
            onClick={close}
          >
            Cancel
          </button>
          <button type="submit" className="loginButton" onClick={handleSubmit}>
            Update
          </button>
        </div>
      </div>
    </>
  );
};

export default StockManagement;
