document.addEventListener("DOMContentLoaded", function(){
    let sprites = document.querySelectorAll('.sprite');

    sprites.forEach(function(element){
        let spriteValue = element.innerHTML.trim();

        if(spriteValue==="magmitar"){
            element.classList.add('magmitar_class');
        }else if(spriteValue==="orejon"){
            element.classList.add('orejon_class');
        }
    });
    
});