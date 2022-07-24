document.getElementById('show').onclick = function () {
    var x = document.getElementById('password')
    if (x.type === 'password') {
        x.type = 'text'
        this.style.color = '#182026'
    } else {
        x.type = 'password'
        this.style.color = '#5C7080'
    }
}

document.getElementById('buttonkirish').addEventListener('click', function () {
    document.querySelector('.loginbox').style.display = 'block'
})
document.querySelector('.x').addEventListener('click', function () {
    document.querySelector('.loginbox').style.display = 'none'
})

$('.autoplay').slick({
    slidesToShow: 4,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    arrows: true,
    responsive: [{
        breakpoint: 1024,
        settings: {
            slidesToShow: 3,
            slidesToScroll: 1,
            infinite: false,
        },
    },
    {
        breakpoint: 600,
        settings: {
            slidesToShow: 2,
            slidesToScroll: 1,
        },
    },
    {
        breakpoint: 480,
        settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
        },
    },
    ],
})