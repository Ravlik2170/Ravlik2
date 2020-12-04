let arr1 = [1, 2, 3, 4, 5];
console.log(arr1);
let result1 = arr1.map(function(elem) {
	return Math.sqrt(elem);
});
console.log(result1);

let arr2 = ['dsfds', 'dsfdsf', 'sdfd'];
console.log(arr2);
let result2 = arr2.map(function(elem){
	return elem + '!';
});
console.log(result2);

let arr3 = ['dsfdsdfsa', 'dgffdsfdsf', 'sfdsdfd']
console.log(arr3);
let result3 = arr3.map(function(elem){
	return elem.split('').reverse().join('');
});
console.log(result3);

let arr4 = ['123', '456', '789'];
console.log(arr4);
let result4 = arr4.map(function(elem){
	return elem.split('');
});
console.log(result4);

let arr5 = [1, 2, 3, 4, 5];
console.log(arr5);
let result5 = arr5.map(function(elem,index){
	return elem*index;
});
console.log(result5);

