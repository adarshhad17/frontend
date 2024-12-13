import React, { useState } from "react";

const ProductInventoryForm = () => {
  const [productName, setProductName] = useState("");
  const [productPrice, setProductPrice] = useState("");

  const [productImage, setProductImage] = useState(null);
  const [variants, setVariants] = useState([{ name: "", options: [""] }]);

  const handleVariantChange = (index, field, value) => {
    const updatedVariants = [...variants];
    updatedVariants[index][field] = value;
    setVariants(updatedVariants);
  };

  const handleOptionChange = (variantIndex, optionIndex, value) => {
    const updatedVariants = [...variants];
    updatedVariants[variantIndex].options[optionIndex] = value;
    setVariants(updatedVariants);
  };

  const handleAddOption = (variantIndex) => {
    const updatedVariants = [...variants];
    updatedVariants[variantIndex].options.push("");
    setVariants(updatedVariants);
  };

  const handleFileChange = (event) => {
    setProductImage(event.target.files[0]);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append("name", productName);
    formData.append("price", productPrice);
    formData.append("image", productImage);
    formData.append("variants", JSON.stringify(variants));

    console.log({
      name: productName,
      price:productPrice,
      image: productImage,
      variants,
    });
    console.log({ formData });

    
  };

  return (
    <>
      <div className="loginContainer">
        <form className={"loginForm"} onSubmit={handleSubmit}>
          <h2 className="h1">Product Details</h2>
          <div className="flex">

          <div className="inputGroup">
            <input
              type="text"
              value={productName}
              onChange={(e) => setProductName(e.target.value)}
              placeholder="Product Name"
              required
            />
          </div>
          <div className="inputGroup">
           
            <input
            style={{marginLeft:"16px"}}
              type="text"
              value={productPrice}
              onChange={(e) => setProductPrice(e.target.value)}
              required
              placeholder="Price"

            />
          </div>


          </div>

          <div className="inputGroup">
            <input
              type="text"
              value={productName}
              onChange={(e) => setProductName(e.target.value)}
              placeholder="HSN Code"
              required
            />
          </div>

          <div className="inputGroup">
            <label>Product Image</label>
            <input type="file" onChange={handleFileChange} />
          </div>

          <div>
            {variants.map((variant, variantIndex) => (
              <div
                key={variantIndex}
                style={{ marginBottom: "1rem" }}
                className="inputGroup"
              >
                <label>Variant Name</label>
                <input
                  type="text"
                  value={variant.name}
                  onChange={(e) =>
                    handleVariantChange(variantIndex, "name", e.target.value)
                  }
                  placeholder="Eg:- size,color...etc"
                  required
                />
                <div style={{marginTop:"8px"}}>
                <label>Options</label>
                  {variant.options.map((option, optionIndex) => (
                    <div key={optionIndex}>
                      <input
                        type="text"
                        value={option}
                        onChange={(e) =>
                          handleOptionChange(
                            variantIndex,
                            optionIndex,
                            e.target.value
                          )
                        }
                        required
                      />
                    </div>
                  ))}

                  <div
                    style={{
                      width: "100%",
                      display: "flex",
                      justifyContent: "center",
                    }}
                  >
                    <button
                      type="button"
                      onClick={() => handleAddOption(variantIndex)}
                      className="registerButton"
                    >
                      Add Option
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>

          <button type="submit" className="loginButton">
            Add Product
          </button>
        </form>
      </div>
    </>
  );
};

export default ProductInventoryForm;
