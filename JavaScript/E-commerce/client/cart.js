const modalContainer = document.getElementById("modal-container");
const modalOverlay = document.getElementById("modal-overlay");

const cartBtn = document.getElementById("cart-btn");
const cartCounter = document.getElementById("cart-counter");

const displayCart = () =>{
    modalContainer.innerHTML ="";
    modalContainer.style.display = "block";
    modalOverlay.style.display = "block";
    // modal header
    const modalHeader = document.createElement("div");

    const modalClose = document.createElement("div");
    modalClose.innerText = "❌"
    modalClose.className = "modal-close";
    modalHeader.append(modalClose);

    modalClose.addEventListener("click",()=>{
        modalContainer.style.display = "none";
        modalOverlay.style.display = "none";
    });
    const modalTitle = document.createElement("div");
    modalTitle.innerText = "Cart";
    modalTitle.className = "modal-title";
    modalHeader.append(modalTitle);

    modalContainer.append(modalHeader);
};


//modal Body

    //si no hay nada en el carrito que se muestre lo siguiente:
    if( cart.length > 0 ){
        cart.forEach((product) => {
            const modalBody = document.createElement("div");
            modalBody.className = "modal-body"
            modalBody.innerHTML = `
            <div class="product">
                    <img class="product-img" src="${product.img}" />
                    <div class="product-info">
                        <h4>${product.productName}</h4>
                    </div>
                <div class="quantity">
                    <span class="quantity-btn-decrese">-</span>
                    <span class="quantity-input">${product.quanty}</span>
                    <span class="quantity-btn-increse">+</span>
                </div>
                <div class="price"> $ ${product.price * product.quanty} </div>
                <div class="delete-product">❌</div>
            </div>
            `;
            modalContainer.append(modalBody);
            
            //funcionalidad para el boton de decrese, permite capturar el elemento por su clase css
            const decrese = modalBody.querySelector(".quantity-btn-decrese")
            //paso el evento con el escuchador
            decrese.addEventListener("click", ()=> {
                //esto es para que no se vaya a valores negativos, que el minimo sea 1
                if(product.quanty !== 1){
                    product.quanty--; //cuando se clickee el boton se le reste 1
                //al restar estamos cambiando el valor de elementos en el carrito entonces hay que ACTUALIZARLO, se hace volviendo a hacer correr esta funcion
                displayCart();
                displayCartCounter();
                }
            });

            //funcionalidad para el boton increse
            const increse = modalBody.querySelector(".quantity-btn-increse")
            //paso el evento con el escuchador
            increse.addEventListener("click", ()=> {
                product.quanty++; //cuando se clickee el boton se le suma 1
                //al restar estamos cambiando el valor de elementos en el carrito entonces hay que ACTUALIZARLO, se hace volviendo a hacer correr esta funcion
                displayCart();
                displayCartCounter();
            });

            //Delete element
            const deleteProduct = modalBody.querySelector(".delete-product");
            deleteProduct.addEventListener("click", ()=>{
                //la funcion esta al final
                deleteCartProduct(product.id); //aca me dice cual es id del prod al que el usuario le hace click
            });
    });
    }

            //MODAL FOOTER

        //calcular el total -> usando el metodo reduce, trabaja con 2 parametros=el produco(cantidad) y el precio
        //en acc guarda el precio del producto
        //el: (elemento) representa cada uno de los elementos adentro del carrito
        //el.price = el precio del elemento * la cantidad del elemento + lo que se ha acumulado 
        //0 : arrancando desde el cero, que a cero producto se le vaya sumando todo y guardando en acc
        const total = cart.reduce((acc, el) => acc + el.price * el.quanty, 0);

        const modalFooter = document.createElement("div");
        modalFooter.className = "modal-footer"
        modalFooter.innerHTML = `
        <div class="total-price">Total: ${total} </div>
        <button class="btn-primary" id="checkout-btn"> Ir a checkout</button>
        <div id="wallet_container"></div>
        `;
        modalContainer.append(modalFooter);