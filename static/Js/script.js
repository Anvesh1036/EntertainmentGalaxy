function page1animation(){
    var tl = gsap.timeline()

tl.from("nav h1, nav h4, nav a",{
    y:-40,
    duration:1,
    delay:0.4,
    opacity:0,
    stagger:0.15
})

tl.from(".center-part1 h1",{
    x:-300,
    opacity:0,
    duration:0.5
})
tl.from(".center-part1 p",{
    x:-100,
    opacity:0,
    duration:0.4
})
tl.from(".center-part1 .typing-animation",{
    x:-100,
    opacity:0,
    duration:0.4
})
tl.from(".center-part2 img",{
    opacity:0,
    duration:0.5,
    x:2
},"-=0.3")

tl.from(".section1bottom h3",{
    opacity:0,
    y:30,
    stagger:0.15,
    duration:0.6
})
}
page1animation()


function page2animation(){
    var tl2=gsap.timeline({
        scrollTrigger:{
            trigger:".section2",
            scroller:"body",
            start:"top 50%",
            end:"top -50%", 
            scrub:2,
        }
    })
    
    
    tl2.from(".services",{
        x:-3000,
        opacity:0,
        duration:0.5,
    })
    
    tl2.from(".elem",{
        x:-300,
        opacity:0,
        duration:0.5
    })
    tl2.from(".elem1",{
        x:-300,
        opacity:0,
        duration:0.5
    })
}
page2animation()


const words = ["Movies","Trailers","Songs","Stories","Games","News"];
let wordIndex = 0;
let charIndex = 0;
let typingElement = document.getElementById("typing-text");

function typeWord() {
    if (charIndex < words[wordIndex].length) {
        typingElement.textContent += words[wordIndex].charAt(charIndex);
        charIndex++;
        setTimeout(typeWord, 200); // Typing speed
    } else {
        setTimeout(eraseWord, 800); // Pause before erasing
    }
}

function eraseWord() {
    if (charIndex > 0) {
        typingElement.textContent = typingElement.textContent.slice(0, -1);
        charIndex--;
        setTimeout(eraseWord, 50); // Erasing speed
    } else {
        wordIndex = (wordIndex + 1) % words.length;
        setTimeout(typeWord, 300); // Pause before typing next word
    }
}

// Start the typing effect
typeWord();


document.querySelector('.hover-trigger1').addEventListener('mouseenter', function() {
    document.querySelector('.image1').style.display = 'block';
    document.querySelector('.image2').style.display = 'none';
    document.querySelector('.image3').style.display = 'none';
    document.querySelector('.image4').style.display = 'none';
    document.querySelector('.image5').style.display = 'none';
    document.querySelector('.image6').style.display = 'none';
  });
  
  document.querySelector('.hover-trigger1').addEventListener('mouseleave', function() {
    document.querySelector('.image1').style.display = 'block';
    document.querySelector('.image2').style.display = 'none';
    document.querySelector('.image3').style.display = 'none';
    document.querySelector('.image4').style.display = 'none';
    document.querySelector('.image5').style.display = 'none';
    document.querySelector('.image6').style.display = 'none';
  });





  
  document.querySelector('.hover-trigger2').addEventListener('mouseenter', function() {
    document.querySelector('.image1').style.display = 'none';
    document.querySelector('.image2').style.display = 'block';
    document.querySelector('.image3').style.display = 'none';
    document.querySelector('.image4').style.display = 'none';
    document.querySelector('.image5').style.display = 'none';
    document.querySelector('.image6').style.display = 'none';
  });
  
  document.querySelector('.hover-trigger2').addEventListener('mouseleave', function() {
    document.querySelector('.image1').style.display = 'none';
    document.querySelector('.image2').style.display = 'block';
    document.querySelector('.image3').style.display = 'none';
    document.querySelector('.image4').style.display = 'none';
    document.querySelector('.image5').style.display = 'none';
    document.querySelector('.image6').style.display = 'none';
  });




  document.querySelector('.hover-trigger3').addEventListener('mouseenter', function() {
    document.querySelector('.image1').style.display = 'none';
    document.querySelector('.image2').style.display = 'none';
    document.querySelector('.image3').style.display = 'block';
    document.querySelector('.image4').style.display = 'none';
    document.querySelector('.image5').style.display = 'none';
    document.querySelector('.image6').style.display = 'none';
  });
  
  document.querySelector('.hover-trigger3').addEventListener('mouseleave', function() {
    document.querySelector('.image1').style.display = 'none';
    document.querySelector('.image2').style.display = 'none';
    document.querySelector('.image3').style.display = 'block';
    document.querySelector('.image4').style.display = 'none';
    document.querySelector('.image5').style.display = 'none';
    document.querySelector('.image6').style.display = 'none';
  });




  document.querySelector('.hover-trigger4').addEventListener('mouseenter', function() {
    document.querySelector('.image1').style.display = 'none';
    document.querySelector('.image2').style.display = 'none';
    document.querySelector('.image3').style.display = 'none';
    document.querySelector('.image4').style.display = 'block';
    document.querySelector('.image5').style.display = 'none';
    document.querySelector('.image6').style.display = 'none';
  });
  
  document.querySelector('.hover-trigger4').addEventListener('mouseleave', function() {
    document.querySelector('.image1').style.display = 'none';
    document.querySelector('.image2').style.display = 'none';
    document.querySelector('.image3').style.display = 'none';
    document.querySelector('.image4').style.display = 'block';
    document.querySelector('.image5').style.display = 'none';
    document.querySelector('.image6').style.display = 'none';
  });



  document.querySelector('.hover-trigger5').addEventListener('mouseenter', function() {
    document.querySelector('.image1').style.display = 'none';
    document.querySelector('.image2').style.display = 'none';
    document.querySelector('.image3').style.display = 'none';
    document.querySelector('.image4').style.display = 'none';
    document.querySelector('.image5').style.display = 'block';
    document.querySelector('.image6').style.display = 'none';
  });
  
  document.querySelector('.hover-trigger5').addEventListener('mouseleave', function() {
    document.querySelector('.image1').style.display = 'none';
    document.querySelector('.image2').style.display = 'none';
    document.querySelector('.image3').style.display = 'none';
    document.querySelector('.image4').style.display = 'none';
    document.querySelector('.image5').style.display = 'block';
    document.querySelector('.image6').style.display = 'none';
  });


  document.querySelector('.hover-trigger6').addEventListener('mouseenter', function() {
    document.querySelector('.image1').style.display = 'none';
    document.querySelector('.image2').style.display = 'none';
    document.querySelector('.image3').style.display = 'none';
    document.querySelector('.image4').style.display = 'none';
    document.querySelector('.image5').style.display = 'none';
    document.querySelector('.image6').style.display = 'block';
  });
  
  document.querySelector('.hover-trigger6').addEventListener('mouseleave', function() {
    document.querySelector('.image1').style.display = 'none';
    document.querySelector('.image2').style.display = 'none';
    document.querySelector('.image3').style.display = 'none';
    document.querySelector('.image4').style.display = 'none';
    document.querySelector('.image5').style.display = 'none';
    document.querySelector('.image6').style.display = 'block';
  });



  