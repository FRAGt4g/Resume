const mouse_bg = document.getElementById('mouse_glow')

document.addEventListener('mousemove', function(e) {
    mouse_bg.style.left = e.clientX + 'px'
    mouse_bg.style.top = e.clientY + 'px'
})