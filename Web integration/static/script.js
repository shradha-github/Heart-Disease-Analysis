const counters = document.querySelectorAll('.counter');

counters.forEach(counter => {

counter.innerText = '0';

const updateCounter = () => {

const target = +counter.getAttribute('data-target');
const c = +counter.innerText;

const increment = target / 200;

if(c < target){
counter.innerText = `${Math.ceil(c + increment)}`;
setTimeout(updateCounter,10);
}
else{
counter.innerText = target;
}

};

updateCounter();

});

let currentIndex = 0;

function slide(direction) {
    const carouselInner = document.querySelector('.carousel-inner');
    const totalImages = carouselInner.children.length;
    
    currentIndex += direction;
    if(currentIndex < 0) currentIndex = totalImages - 1;
    if(currentIndex >= totalImages) currentIndex = 0;

    carouselInner.style.transform = `translateX(-${currentIndex * 100}%)`;
}