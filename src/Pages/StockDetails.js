import React, { useEffect, useState } from 'react'
import ProductCard from '../Components/Card';

function StockDetails() {

    const [products, setproducts] = useState([]);

    useEffect(() => {
      const fetchData = async () => {
        const resp = await fetch("http://localhost:8000/api/products/");
        const data = await resp.json();
        console.log(data);
        
        setproducts(
          data?.map((el) => {
            return {
              name: el.ProductName,
              price: el.price,
              image:el?.ProductImage,
              stock:el?.TotalStock,
              variants: [{ name: "size", options: ["M", "L"] }],
            };
          })
        );
        console.log(data);
      };
      fetchData();
    }, []);

  return (
    <div>
         <h1 style={{ textAlign: "center", marginTop: "30px" }}>Products Stock Management</h1>
        <div className="cards-container">
          {products.map((product) => (
            <ProductCard product={product} key={product.id} stock={true}/>
          ))}
        </div>
    </div>
  )
}

export default StockDetails