/*
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

*/


function isAnagram(s, t){
    if (s.length !== t.length){
        return false 
    }
    let letterCount = {}

    for (let char of s){
        letterCount[char] = (letterCount[char] || 0) + 1
    }
    /*
    for (let char of t){
        if (!letterCount[char]){
            return false 
        }
        letterCount[char] --
    }
    */

    for (let char of t){
        letterCount[char] = (letterCount[char] || 0) - 1
    }

    for (let count of Object.values(letterCount)) {
        if (count !== 0) {
            return false; 
        }
    }

    return true; 

}

console.log(isAnagram("anagram", "nagaram"))  // true 
console.log(isAnagram("cat", "rat"))  // false 