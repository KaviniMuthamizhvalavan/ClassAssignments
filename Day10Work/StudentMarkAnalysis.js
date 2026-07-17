/* 
Student Marks Analysis
10 students marks in an array
analyse marks using loop and if statements

for loop to iterate thriugh all marks 
use an if statement to check whether each student has passed or failed
pass 50 or above
fail below 50

*/

let marks=[85,42,76,91,38,67,55,29,80,49];
let pass = [];
let fail = [];
let high = 0;
let low = 100;

for (var i=0; i < marks.length; i++){
    if(marks[i]>=50){
        console.log("Student ", i,": ",marks[i], "- Pass");
        pass++;
        if (marks[i] > high){
            high = marks[i]
        }
    }
    else{
        console.log("Student ", i,": ",marks[i], "- Fail");
        fail++;
        if (marks[i]<low){
            low = marks[i]
        }
    }
}
console.log("Total Passed: "+pass)
console.log("Total Failed: "+fail)
console.log(`Highest Mark: ${high}`)
console.log(`Lowest Mark: ${low}`)
