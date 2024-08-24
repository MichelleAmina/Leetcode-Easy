function palindrome(x){
    let splitNum = x.toString().split('')
    let reverseNum = splitNum.slice().reverse().join('')

    let originalNum = splitNum.join('')

    return reverseNum === originalNum ? true : false

}

console.log(palindrome(121)) // true 
console.log(palindrome(-121)) // false
console.log(palindrome(120)) // false