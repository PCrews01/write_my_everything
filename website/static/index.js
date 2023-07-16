async function setLoader(){
    let ns = document.querySelector('#loaders')
    let n = document.querySelector('#loader')
    console.log(" YO!")
    // n.innerHTML = ""
    let spinner_el = document.createElement('div')
    let span_el = document.createElement('span')

    let spinner_el2 = document.createElement('div')
    let span_el2 = document.createElement('span')

    let spinner_el3 = document.createElement('div')
    let span_el3 = document.createElement('span')
        
    span_el.innerHTML = "Loading..."
    spinner_el.classList.add('spinner-grow', 'text-info')
    span_el.classList.add("visually-hidden")
    spinner_el.appendChild(span_el)
    n.appendChild(spinner_el)


    span_el2.innerHTML = "Loading..."
    spinner_el2.classList.add('spinner-grow', 'text-warning')
    span_el2.classList.add("visually-hidden")
    spinner_el2.appendChild(span_el2)
    n.appendChild(spinner_el2)

    span_el3.innerHTML = "Loading..."
    spinner_el3.classList.add('spinner-grow', 'text-danger')
    span_el3.classList.add("visually-hidden")
    spinner_el3.appendChild(span_el3)
    n.appendChild(spinner_el3)
    
} 