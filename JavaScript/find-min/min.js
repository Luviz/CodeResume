const findMin = (numbers) => {
  let min = numbers[0];

  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] < min) {
      min = numbers[i];
    }
  }

  return min;
};

console.log(findMin([3, 4, 5, 1, 2]), `correct: 1`);
console.log(findMin([4, 5, 6, 7, 0, 1, 2]), `correct: 0`);
console.log(findMin([11, 13, 15, 17]), `correct: 11`);
console.log(
  findMin([1, 2, 3, 4, 5, 6, 7, 8, 0, 9, 10, 11, 12, 13]),
  `correct: 0`
);
