const greeting = 'Hello, how are you?'

const word = 'Welcome'
word.split("")

const letters = word.split('')
letters.join('')

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

const nums = [78, 59, 105, 32]
let randIndex = getRandomInt(nums.length)
console.log(nums[randIndex])