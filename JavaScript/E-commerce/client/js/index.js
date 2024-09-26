const shopContent = document.getElementById("shopContent");
const cart = []; // este es nuestro carrito es un array vacio

productos.forEach((product) =>{
    const content = document.createElement("div");
    content.innerHTML = `
    <img src="${product.img}">
    <h3>${product.productName}</h3>
    <p>${product.price} $<p>
    `;
    shopContent.append(content);
    });