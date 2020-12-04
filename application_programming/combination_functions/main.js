/Задача 89.1/

function getSum(arr) {
	let sum = 0;
	
	for (let elem of arr) {
		sum += Number(elem);
	}
	
	return sum;
}

function getDigits(num) {
	return String(num).split('');
}

/Ответ/
console.log(getSum( getDigits(12345)));

/Задача 89.2/

function getDivisors(num) {
let result = [];

for (let i = 2; i < num; i++) {
if (num % i == 0) {
result.push(i);
}
}
return result;
}
function getAvg(arr) {
let sum = 0;

for (let elem of arr) {
sum += elem;
}

return sum / arr.length;
}
console.log(getAvg(getDivisors(20)));