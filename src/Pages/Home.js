import React, { useEffect, useState } from 'react'
import ProductCard from '../Components/Card';

function Home() {

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
              price: el.Price,
              image:el.ProductImage,
            };
          })
        );
        console.log(data);
      };
      fetchData();
    }, []);

  return (
    <div>
         <h1  style={{ textAlign: "center", marginTop: "30px", }}>All Products</h1>
        <div className="cards-container">
          {products.map((product) => (
            <ProductCard product={product} key={product.id} stock={false}/>
          ))}
        </div>
    </div>
  )
}

export default Home