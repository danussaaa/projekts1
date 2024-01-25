

function peta(){
    let text = 'Mēs tev sniedzam iedvesmu: ';                        /*  teksts */
    let recepte = ["Siera kūka", "Tomātu zupa", "Plāceņi", "https://www.youtube.com/watch?v=zPAEXW54AP4"];          
    /*  nejaušo recepšu saraksts un links uz youtube video  */
    let numurs = Math.floor(Math.random() * recepte.length);         /*  random funkcija */

        recepteName = recepte[numurs];                               /*  mainīgais receptei  */
      
        text = text + recepteName + ' ';                             /*  izvada tekstu ar nejaušo recepti  */
        console.log(text)                                            /*  izvada random recepti konsolē  */
    
    }

