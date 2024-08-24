function isAnagram(s, t){
    const sortS = s.split('').sort().join()
    const sortT = t.split('').sort().join()

    return sortS === sortT

}


console.log(isAnagram("anagram", "nagaram"))
console.log(isAnagram("cat", "rat"))