function mainaKrasu(){
    document.body.style.backgroundColor = "	#c08ddd"
}

function mainaKrasu2(){
    document.body.style.backgroundColor = "	#ff93ac"
}
function petaJs(){
    console.log('izvade konsolē')
    console.log(123+3*5/2)
}

function dzivnieki(){
    let text = 'Dzīvnieki, kas sākas ar burtu b ir: '
    let animals = ["bear","cat","bull"]
    let animalName = ''
    for(let i=0;i<animals.length;i++) {
        animalName = animals[i]         /*panemam viena dzivnieka nosaukumu*/
        if(animalName[0] === 'b') {           /*izvelas pirmo burtu*/
            text = text + animalName + ' '         /*likam konkreta dzivnieka nosaukumu un atstarpi saliek starp vārdiem*/
        }           
    }
    console.log(text)              /*izvadit konsole tekstu*/
}

