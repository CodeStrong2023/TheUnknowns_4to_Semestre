function hola(nombre,miCallback){
    setTimeout(function () {
        console.log("Hola "+ nombre);
        miCallback(nombre);
    },1000)
}

function adios(nombre,otroCallback){
    setTimeout(function(){
        console.log("Adios "+ nombre)
        otroCallback();
    },1000);
}

function hablar(callBackHablar){

}setTimeout(function(){
    console.log("bla bla bla")
},1000);

//Funcion recursiva
function conversacion(nombre, veces, callback){
    if (veces > 0){
        hablar(function() {
            conversacion(nombre, --veces, callback);
        })
    }else{
        callback(nombre, callback);
    }
}

//Proceso principal
console.log("Iniciando el proceso...")

hola("Ariel", function(nombre){
    conversacion(nombre, 4, function(){
        console.log("Terminando el proceso...")
    })
});

//Callback Hell -> Bienvenidos al infierno
// hola("carlos", function (nombre){
//     hablar(function(){
//         hablar(function(){
//             hablar(function(){
//                 hablar(function(){
//                 adios(nombre,function(){
//                     console.log("Terminando el proceso...")
//                     });
//                 });
//             });
//         });
//     });
// });
