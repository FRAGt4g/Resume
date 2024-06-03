// const mouse_bg = document.getElementById('mouse_glow')

// document.addEventListener('mousemove', function(e) {
//     mouse_bg.style.left = e.clientX + 'px'
//     mouse_bg.style.top = e.clientY + 'px'
// })

function test(el) {
    rect = el.getBoundingClientRect();
	const maxWidth = rect.width;
	const maxHeight = rect.height;

    text_holder = document.createElement('span')
    text_holder.textContent = el.textContent.trim()
    text_holder.style.width = 'auto';
    el.textContent = '';
    el.appendChild(text_holder)

    text_holder.style.fontSize = '1px';
    console.log("max-width: " + el.offsetWidth)
    console.log("max-height: " + el.offsetWidth)
    while (text_holder.offsetWidth < maxWidth && text_holder.offsetHeight < maxHeight) {
        text_holder.style.fontSize = (Number(text_holder.style.fontSize.slice(0, -2)) + 1) + 'px';
    }
    console.log("width: " + text_holder.offsetWidth)
    console.log("height: " + text_holder.offsetHeight)
    console.log("font-size: " + text_holder.style.fontSize)
    text_holder.style.fontSize = text_holder.style.fontSize.slice(0, -2) - 1 + 'px';
}

document.addEventListener('keypress', function(e) {
    if (e.key == ' ') {
        document.querySelectorAll(".fit-text-to-screen").forEach(function (el) {
            test(el);
        })
    }
    if (e.key == 'w') {
        document.querySelectorAll(".fit-text-to-screen").forEach(function (el) {
            el.style.fontSize = (Number(el.style.fontSize.slice(0, -2)) + 1) + 'px';
            console.log('incrementing font size to ' + el.style.fontSize)
        })
    }
    if (e.key == 's') {
        document.querySelectorAll(".fit-text-to-screen").forEach(function (el) {
            el.style.fontSize = (Number(el.style.fontSize.slice(0, -2)) - 1) + 'px';
            console.log('decrementing font size to ' + el.style.fontSize)
        })
    }
})

// window.addEventListener("resize", function (el) {
// 	document.querySelectorAll(".fit-text-to-screen").forEach(function (el) {
//         test(el);

// 		// txt = el.textContent.trim()
// 		// rect = el.getBoundingClientRect()

// 		// console.log("element: " + txt + "\n\twidth: " + rect.width + "\n\tlength: " + txt.length);

// 		// el.style.fontSize = rect.width/txt.length + 'px';
// 	});
// });