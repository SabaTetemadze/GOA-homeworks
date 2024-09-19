function numbersBetween(num1,num2) {
    const result = []
    while (num1 != num2) {
        result.push(num1)
        num1 += 1
    }
    console.log(result)
}

function calculateAverage(array) {
    let sum = 0

    for ( let i of array) {
        sum += i
    }
    let result = sum/array.length
    console.log(result)
}

function func() {

    let database = [
        name = document.getElementById("inputName"),
        email = document.getElementById("inputEmail"),
        password = document.getElementById("inputPassword")
    ]
    console.log(database)
}