console.log('Inicio del programa');  //Se va a ejecutar 1°
//timeset timeout = funciones
setTimeout(() => {
    console.log('Primer Timeout')   //Se va a ejecutar 5°
}, 3000); //despues de los 3 segundos va a estar disponible para ejecutarse 

setTimeout(() => {
    console.log('Segundo Timeout')      //Se va a ejecutar 3°
}, 0);

setTimeout(() => {
    console.log('Tercero Timeout')      //Se va a ejecutar 4°
}, 0);

console.log('Fin del programa');        //Se va a ejecutar 2°

//Estas son instrucciones no bloqueantes, es todo asincrono