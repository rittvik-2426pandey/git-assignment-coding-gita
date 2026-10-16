# Assignment: Introduction to JavaScript
---

## Section A: Short Answer Questions (1 Mark each)

**Q1.** What is JavaScript?

Ans:-JavaScript is a high-level, dynamically typed, interpreated programming language used to create interactive websites and applications.

**Q2.** Who created JavaScript and in which year?<br>
Ans:-javascript was created by Brendan Eich at Netscape  in 1995.

**Q3.** What was the original name of JavaScript?<br>
Ans:- Originally named Mocha, then LiveScript, and finally JavaScript.

**Q4.** Is JavaScript the same as Java? Give one major difference.<BR>
Ans:-Java is mainly used for application/software development, while JavaScript is mainly used to make web pages interactive and dynamic.


**Q5.** What does it mean when we say JavaScript is a **high-level** programming language?<br>
Ans:-JavaScript is a **high-level** programming language means it can only understand by humans.

**Q6.** Is JavaScript a compiled language or an interpreted language? Explain briefly.<br>
Ans:- JavaScript is mainly considered an interpreted language. It is executed by the JavaScript engine, which reads and executes the code, often using Just-In-Time (JIT) compilation to improve performance.

**Q7.** Name the JavaScript engines used by the following browsers:
- Google Chrome===>> V8 
- Mozilla Firefox ===>> SpiderMonkey
- Apple Safari ===>> JavaScriptCore

**Q8.** What is **Dynamic Typing** in JavaScript?<Br>
Ans:-Dynamic typing means that in JavaScript, a variable's data type is determined automatically at runtime and can change during execution.

**Q9.** What is the main difference between a **static** website and a **dynamic** website?<br>
Ans:- A static website shows fixed content that usually does not change unless the code is manually updated. A dynamic website can generate or change content based on user actions, data, or other conditions.


**Q10.** Name the three pillars of Front-end Web Development and write one line about each.<br>
Ans:- The three pillars of Front-end Web Development are:

1. HTML (HyperText Markup Language): Provides the structure and content of a webpage.
2. CSS (Cascading Style Sheets): Controls the design, layout, colors, and appearance of a webpage.
3. JavaScript: Adds interactivity and dynamic behavior to a webpage.


**Q11.** What is the difference between Frontend and Backend?<br>
Ans:--Frontend is the part of a website that users see and interact with, using HTML, CSS, and JavaScript. Backend is the server-side part that handles data, databases, authentication, and application logic.


**Q12.** What is Node.js?<br>
Ans:-Node.js is a JavaScript runtime environment that allows JavaScript to run outside the web browser, mainly on the server side.


**Q13.** Explain **ECMAScript**. What is its relation with JavaScript?
Ans:-ECMAScript is the standard specification that defines how JavaScript should work. JavaScript is a programming language based on the ECMAScript standard, with additional features such as the DOM and Web APIs.

---

## Section B: True or False  
(Write True or False. If False, correct the statement)

1. JavaScript is a statically typed language. =====>>>>> False
2. JavaScript can only run inside the browser.=====>>>>> False
3. HTML is responsible for the behaviour of a webpage.=====>>>>> False
4. Node.js allows JavaScript to run outside the browser.=====>>>>> True
5. JavaScript is case-insensitive.=====>>>>> false
6. `let name` and `let Name` are the same variable. =====>>>>> False
7. ECMAScript is a programming language.=====>>>>> False
8. React, Angular, and Vue.js are used for Backend development.=====>>>>> False

---
## Section C: Fill in the Blanks

1. JavaScript was created by ____Brendan Eich__________ in the year ____1995__________.
2. The three technologies used in Front-end development are ___HTML_______, __CSS______, and _JAVASCRIPT_________.
3. JavaScript engines: Chrome uses ___V8_______, Firefox uses _SPIDERMONKEY_________.
4. In the restaurant analogy: Customer = ___user_______, Waiter = ___server______, Chef = ___DATABASE_______.
5. JavaScript file extension is _.JS_________.

## Section D: Conceptual Questions (2 Marks each)

**Q14.** Differentiate between a **static website** and a **dynamic website**. Give one real-world example of each.<BR>
aNS:-

| Static Website                                                  | Dynamic Website                                                    |
| --------------------------------------------------------------- | ------------------------------------------------------------------ |
| Shows fixed content that changes only when the code is updated. | Content can change automatically based on users, data, or actions. |
| Usually simpler and faster to develop.                          | Usually requires server-side logic and a database.                 |
| **Example:** A simple portfolio website.                        | **Example:** An online shopping website like Amazon.               |


**Q15.** Explain any two features of JavaScript that make it suitable for creating interactive web pages.<BR>
aNS:-**Q15.** Explain any two features of JavaScript that make it suitable for creating interactive web pages.

**Q16.** List any four areas (apart from web browsers) where JavaScript is used today. Mention one popular framework/library for each (if applicable).<BR>
ANS:-

1. Server-side Development — Node.js
2. Mobile App Development — React Native
3. Desktop App Development — Electron
4. Game Development— Phaser.js


**Q17.** What is the difference between writing JavaScript code:
- Inside an HTML file using `<script>` tag, and
- In an external `.js` file?  
Mention two advantages of using an external JavaScript file.<BR>
ANS:-

* Inside HTML using `<script>`: JavaScript code is written directly within the HTML file.
* External `.js` file: JavaScript code is written in a separate `.js` file and linked to the HTML using `<script src="script.js"></script>`.

**Two advantages of an external JavaScript file:**

1. **Reusability:** The same JavaScript file can be used on multiple HTML pages.
2. **Easy maintenance:** HTML and JavaScript are separated, making the code easier to read, update, and manage.


**Q18.** Explain the difference between Frontend and Backend using the **restaurant analogy** in your own words.<BR>
**Answer:**
Think of a website like a **restaurant**. The **Frontend** is like the dining area and waiter—the part customers see and interact with. The **Backend** is like the kitchen and chef—it works behind the scenes to process requests, prepare data, and send the result back to the customer.


**Q19.** Why should a beginner learn JavaScript? Write at least 4 points.<BR>
**Answer:**

A beginner should learn JavaScript because:

1. It makes websites **interactive and dynamic**.
2. It is an important language for **Frontend Web Development**.
3. It can also be used for **Backend Development** with Node.js.
4. It has many **frameworks and libraries** like React, Angular, and Vue.js.
5. It has a **large community** and many learning resources.

---

## Section E: Code-Based Questions (3 Marks each)

**Q20.** Predict the output of the following code and explain why:

```javascript
let value = 25;
console.log(typeof value);
value = "JavaScript";
console.log(typeof value);
value = false;
console.log(typeof value);
```
number
string
boolean
**Q20.**


Explanation: JavaScript is **dynamically typed**, so the same variable can store values of different data types. The `typeof` operator returns the data type of the current value stored in `value`.

**Q21.** Write a simple HTML + JavaScript program that displays an alert box with the message **"Welcome to JavaScript!"** when a button is clicked.<br>
ans:-<!DOCTYPE html>
<html>
<head>
    <title>JavaScript Alert</title>
</head>
<body>

    <button onclick="showMessage()">Click Me</button>

    <script>
        function showMessage() {
            alert("Welcome to JavaScript!");
        }
    </script>

</body>
</html>
**Q22.** Write JavaScript code to demonstrate **event-driven programming**.  <br>
<!DOCTYPE html>
<html>
<head>
    <title>Event-Driven Programming</title>
</head>
<body>

    <button id="btn">Click Me</button>
    <p id="message"></p>

    <script>
        document.getElementById("btn").addEventListener("click", function() {
            document.getElementById("message").innerHTML = "Button was clicked!";
        });
    </script>

</body>
</html>
When a user clicks a button with id `"myBtn"`, the text of a paragraph with id `"demo"` should change to `"Button was clicked!"`.

## Section F: Practical / Application Based (5 Marks)

**Q23.** Create a complete web page (HTML + JavaScript) that includes the following:

1. A heading: **"My First JavaScript Page"**
2. A button labeled **"Click Me"**
3. When the button is clicked:
   - Show an alert: `"Hello, B.Tech Student!"`
   - Change the background color of the page to light blue
4. Also print `"JavaScript is running successfully!"` in the browser console.

**Write the complete code** (you can use Inline or External JavaScript).

---
ANS-<!DOCTYPE html>
<html>
<head>
    <title>My First JavaScript Page</title>
</head>
<body>

    <h1>My First JavaScript Page</h1>

    <button onclick="changePage()">Click Me</button>

    <script>
        console.log("JavaScript is running successfully!");

        function changePage() {
            alert("Hello, B.Tech Student!");
            document.body.style.backgroundColor = "lightblue";
        }
    </script>

</body>
</html>

## Section G: Higher Order Thinking (Bonus - 3 Marks)

**Q24.** JavaScript was originally created only for browsers. Today it is used in frontend, backend, mobile apps, desktop apps, and even AI/ML.  
In your own words, explain why JavaScript became so popular and multipurpose. Mention the role of **Node.js** and **ECMAScript** updates in this growth.

---

**Q24.**

JavaScript became popular because it is **easy to learn, widely supported, and useful for many types of applications**. It started mainly for making web pages interactive, but today it is used in frontend, backend, mobile, desktop, and other areas.

1. **Node.js** allowed JavaScript to run outside the browser, making it useful for **backend and server-side development**.
2. **ECMAScript updates** regularly added new features and improvements to JavaScript, making the language more powerful and easier to use.
3. A large number of **libraries and frameworks** such as React, Angular, and Vue.js helped developers build applications faster.
4. JavaScript has a **large developer community**, many learning resources, and support across different platforms.

Therefore, JavaScript grew from a browser scripting language into a **multipurpose programming language**.

### Submission Guidelines
- Write your answers in a notebook or type them in a document.
- For coding questions, test your code using browser console, VS Code Live Server, or online editors (CodePen / JSFiddle).
- Submit the answers on Github CodingGita Assignment Repo in JavaScript Folder before the given deadline.
// 1. Addition

// Question 1
// let collectionClass1 = 15000
// let collectionClass2 = 12500
// let totalCollection = collectionClass1 + collectionClass2
// console.log("Total Collection =", totalCollection);

// Question 2
// let pagesMorning = 18
// let pagesEvening = 25
// let totalPages = pagesMorning + pagesEvening
// console.log("Total Pages Read =", totalPages);

// Question 3
// let itemsSoldMonday = 125
// let itemsSoldTuesday = 178
// let totalItemsSold = itemsSoldMonday + itemsSoldTuesday
// console.log("Total Items Sold =", totalItemsSold);

// Question 4
// let a = "10";
// let b = 5;
// let result = a + b;
// console.log(result); // 105

// Question 5
// let x = 5;
// let y = "3";
// let result = x + y;
// console.log(result); // 53

// Question 6
// The output of 15 + 27 is 42
// console.log(15+27);

// Question 7
// let costBook = 350
// let costPen = 45
// let totalCost = costBook + costPen
// console.log("Total Price =", totalCost);

// Question 8
// Result of "25" + 10 is "2510" because of concatenation

// Question 9
// let balance = 2000
// let itemCost1 = 750
// let itemCost2 = 320
// let totalSpent = itemCost1 + itemCost2
// let remainingBalance = balance - totalSpent
// console.log("Total Spent =", totalSpent);
// console.log("Remaining Balance =", remainingBalance);

// Question 10
// console.log(5 + "5" + 5); // "555" due to concatenation
// console.log(5 + 5 + "5"); // "105" because the calculation will go from left to right therefore first 5+5 will become 10 and then 10 and "5" will be concatenated
// console.log("5" + 5 + 5); // "555" due to concatenation


// 2. Subtraction

// Question 1
// let totalSeats = 80
// let occupiedSeats = 53
// let emptySeats = totalSeats - occupiedSeats
// console.log("Number of Empty Seats =", emptySeats);

// Question 2
// let totalMarks = 500
// let lostMarks = 35
// let finalMarks = totalMarks - lostMarks
// console.log("Final Marks =", finalMarks);

// Question 3
// let totalBox = 2500
// let boxSent = 875
// let boxRemaining = totalBox - boxSent
// console.log("Remaining Boxes =", boxRemaining);

// Question 4
// let a = "10";
// let b = 3;
// let result = a - b;
// console.log(result); // 7

// Question 5
// let x = "20";
// let y = "5";
// let result = x - y;
// console.log(result); // 15

// Question 6
// The output of 100 - 37 is 63
// console.log(100 - 37);

// Question 7
// let totalWater = 500
// let waterUsed = 175
// let waterLeft = totalWater - waterUsed
// console.log("Water Left =", waterLeft);

// Question 8
// console.log("50" - 20); // 30 
// console.log("50" - "20"); // 30 
// In first expression, "50" is getting converted to number whereas in second expression both "50" and "20" are getting converted into number

// Question 9
// let totalApple = 240
// let appleSoldMorning = 95
// let appleSoldEvening = 67
// let totalAppleSold = appleSoldEvening + appleSoldMorning
// let appleLeft = totalApple - totalAppleSold
// console.log("Apples Left =", appleLeft);

// Question 10
// console.log("100" - 50); // 50 because "100" is converted into number and then getting subtracted from
// console.log("abc" - 10); // NaN because "abc" can't be converted into a number
// console.log(10 - "5" - "2"); // 3 because "5" and "2" is getting converted into number and then getting subtracted
// console.log("10" - "5" - "2"); // 3 because "10", "5" and "2" get converted into number and then gets subtracted


// 3. Multiplication

// Question 1
// let notebookCost = 45
// let notebookQty = 8
// let totalCost = notebookCost * notebookQty
// console.log("Total Cost =", totalCost);

// Question 2
// let productionPerHour = 120
// let productionTime = 6
// let bottlesProduced = productionPerHour * productionTime
// console.log("Bottles Produced =", bottlesProduced);

// Question 3
// let totalRows = 7
// let plantsPerRow = 15
// let totalPlants = totalRows * plantsPerRow
// console.log("Total Number of Plants =", totalPlants);

// Question 4
// let a = "5";
// let b = 4;
// let result = a * b;
// console.log(result); // 20

// Question 5
// let x = "10";
// let y = "2";
// let result = x * y;
// console.log(result); // 20

// Question 6
// The output of 12 * 8 is 96
// console.log(12 * 8);

// Question 7
// let pizzaCost = 299
// let totalPizza = 4
// let totalCost = pizzaCost * totalPizza
// console.log("Total Cost =", totalCost);

// Question 8
// The result of "7" * 6 is 42 and "7" * "6" is 42
// console.log("7" * 6);
// console.log("7" * "6");

// Question 9
// let productionPerHour = 45
// let productionTime = 8
// let totalUnitsProduced = productionPerHour * productionTime
// console.log("Units Produced =", totalUnitsProduced);

// Question 10
// console.log("5" * 3 * "2"); // 30 because "5" and "2" are getting converted to number and then getting calculated
// console.log("abc" * 4); // NaN because "abc" can't convert to number
// console.log(10 * "2.5"); // 25 because "2.5 "is getting converted to number and then getting calculated
// console.log("10" * "2.5" * "0"); // 0 because "10", "2.5" and "0" are getting converted to number and then getting calculated


// 4. Division

// Question 1
// let totalPencils = 144
// let totalStudents = 12
// let pencilsPerStudent = totalPencils / totalStudents
// console.log("Number of Pencils Each Student Receives =", pencilsPerStudent);

// Question 2
// let totalDistance = 360
// let totalTime = 6
// let averageDistance = totalDistance / totalTime
// console.log("Average Distance Travelled Per Hour =", averageDistance);

// Question 3
// let totalAmount = 72000
// let totalDepartments = 9
// let amountPerDepartment = totalAmount / totalDepartments
// console.log("Amount Received By Each Department =", amountPerDepartment);

// Question 4
// let a = "20";
// let b = 4;
// let result = a / b;
// console.log(result); // 5

// Question 5
// let x = "100";
// let y = "5";
// let result = x / y;
// console.log(result); // 20

// Question 6
// The output of 144 / 12 is 12
// console.log(144 / 12);

// Question 7
// let totalStudents = 360
// let totalClassrooms = 9
// let studentsPerClassroom = totalStudents / totalClassrooms
// console.log("Students Per Classroom =", studentsPerClassroom);

// Question 8
// The result of "100" / 4 is 25 and "100" / "4" is 25
// console.log("100" / 4);
// console.log("100" / "4");

// Question 9
// let totalBill = 2400
// let totalFriends = 6
// let equalShare = totalBill / totalFriends
// console.log("Each Person's Share =", equalShare);

// Question 10
// console.log(10 / 0); // Infinity
// console.log(-10 / 0); // -Infinity
// console.log(0 / 0); // NaN
// console.log("20" / "4" / 2); // 2.5
// console.log("abc" / 5); // NaN


// 5. Modulus

// Question 1
// let totalStudents = 53
// let studentPerGroup = 5
// let studentsLeft = totalStudents % studentPerGroup
// console.log("Number of Students Left Over =", studentsLeft);

// Question 2
// let totalCandies = 128
// let candiesPerBox = 10
// let candiesLeft = totalCandies % candiesPerBox
// console.log("Candies Left Unpacked =", candiesLeft);

// Question 3
// let totalToys = 237
// let toysPerBox = 6
// let toysLeft = totalToys % toysPerBox
// console.log("Toys Left =", toysLeft);

// Question 4
// let totalPeople = 185
// let busCapacity = 40
// let peopleLeft = totalPeople % busCapacity
// console.log("People Left =", peopleLeft);

// Question 5
// let a = 10;
// let b = 0;
// let result = a % b;
// console.log(result); // NaN

// Question 6
// The output of 29 % 5 is 4
// console.log(29 % 5);

// Question 7
// let totalChocolates = 23
// let chocolatesPerBox = 4
// let chocolatesLeft = totalChocolates % chocolatesPerBox
// console.log("Chocolates Left Over =", chocolatesLeft);

// Question 8
// console.log(0 % 7); // 0 because 0 % (any non-zero number) is 0
// console.log(15 % 0); // NaN because any number % 0 is NaN

// Question 9
// let totalPages = 47
// let pagesCapacity = 6
// let fullSheets = Math.floor(totalPages / pagesCapacity)
// let pagesLeft = totalPages % pagesCapacity
// console.log("Full Sheets Needed =", fullSheets);
// console.log("Pages Left Over =", pagesLeft);

// Question 10
// console.log(17 % 5); // 2
// console.log(-17 % 5); // -2
// console.log(17 % -5); // 2
// console.log(-17 % -5); // -2
// console.log(10 % 0); // NaN


// 6. Exponentiation

// Question 1
// let side = 6
// let volume = side ** 3
// console.log("Volume of Cube =", volume);

// Question 2
// let side = 9
// let totalCells = side ** 2
// console.log("Total Cells =", totalCells);

// Question 3
// console.log(5 ** 4);

// Question 4
// let pixelsEachSide = 1024
// let totalPixels = pixelsEachSide ** 2
// console.log("Total Pixels =", totalPixels);

// Question 5
// let base = 2;
// let power = -1;
// let result = base ** power;
// console.log(result); // 0.5

// Question 6
// The output of 3 ** 4 is 81
// console.log(3 ** 4);

// Question 7
// let side = 9
// let area = side ** 2
// console.log("Area of Square =", area);

// Question 8
// The result of 2 ** 5 is 32 and 5 ** 2 is 25
// They are not the sane
// console.log(2 ** 5);
// console.log(5 ** 2);

// Question 9
// console.log(2 ** 3 ** 2);  // 512        // right-associative
// console.log((2 ** 3) ** 2); // 64
// console.log(2 ** -3); // 0.125
// // console.log(-2 ** 2);  // Error          // Remember: Syntax error
// console.log((-2) ** 2); // 4
// console.log(4 ** 0.5); // 2

// Question 10
// let a = 10;
// let b = 0;
// let result = a ** b;
// console.log(result); // 1
**All the Best!**

---

### Deadline : 28th September, 2026

// // B] Assignment Operators
// // 1. Simple Assignment ---------------------------------------------------------
// 1
// let studentname="Priya";
// let marks=92
// console.log(studentname)
// console.log(marks)

// 2
// let score=0
// console.log(score)

// 3
// let a,b,c;
// a=b=c=50;
// console.log(a,b,c);

// 4
// 100

// 5
// 15,30


// 2. Add and Assign --------------------------------------------------
// A player’s score is 80. He scores 25 more points. Update the score using +=.
// A wallet has ₹1500. Cashback of ₹120 is added. Update the balance using +=.
// Predict the output:
// let count = 10;
// count += 5;
// console.log(count);
// Predict the output:
// let msg = "Good";
// msg += " Morning";
// console.log(msg);
// What is the final value after let n = 20; n += "5";? Explain.

// Answer:

// // 2. Add and Assign +=
// 1
// let score = 80;
// score += 25;
// console.log(score)

// 2
// let cashback = 1500;
// cashback += 120
// console.log(cashback)

// 3
// 15

// 4
// Good Morning

// 5
// 205
// because string concatination

// 3. Subtract and Assign --------------------------------------------
// Health is 100. Player takes 35 damage. Update health using -=.
// Stock of 300 items is reduced by 45 after a sale. Update using -=.
// Predict the output:
// let lives = 5;
// lives -= 2;
// console.log(lives);
// Predict the output:
// let num = "40";
// num -= 15;
// console.log(num);
// What is the result of let x = "abc"; x -= 5;? Explain.

// Answer:
// 1.
// let health = 100;
// health -= 35;
// console.log(health);

// 2.
// let stock=300;
// stock -= 45;
// console.log(stock);

// 3.
// 3

// 4.
// 25

// 5.
// NaN because abc cannot be converted into Number

// 4. Multiply and Assign ---------------------------------------------
// Price of an item is ₹500. Apply 18% GST using *= 1.18.
// A quantity of 8 is tripled. Update using *=.
// Predict the output:
// let amo = 200;
// amo *= 1.1;
// console.log(amo);
// Predict the output:
// let val = "7";
// val *= 3;
// console.log(val);
// What is the result of let y = "hello"; y *= 2;? Explain.

// Answer:
// 1.
// let pr = 500;
// price *= 1.18;
// console.log(pr);

// 2.
// let quantity=8;
// quantity *= 3;
// console.log(quantity);

// 3.
// 220.00

// 4.
// 21

// 5.
// NaN because hello cannot be converted into number 


// 5. Divide and Assign p----------------------------------------------------
// Total of 180 chocolates is shared among 6 children. Update using /=.
// Distance of 300 km is covered in 5 hours. Find average speed using /=.
// Predict the output:
// let total = 400;
// total /= 8;
// console.log(total);
// Predict the output:
// let num = "100";
// num /= 4;
// console.log(num);
// What is the result of let z = 50; z /= 0;? Explain.

// Answer:
// 1.
// let chocolate = 180;
// chocolate /= 6;
// console.log(chocolate)

// 2.
// let dist= 400;
// dist /= 5;
// console.log(dist)

// 3.
// 50

// 4.
// 25

// 5.
// Infinity, because it is devided by 0

// 6. Modulus and Assign ---------------------------------
// Number 47 is divided by 6. Store only the remainder using %=.
// Counter is at 23. Keep only the remainder when divided by 12 using %=.
// Predict the output:
// let num = 29;
// num %= 5;
// console.log(num);
// Predict the output:
// let x = "17";
// x %= 3;
// console.log(x);
// What is the result of let m = 15; m %= 0;? Explain.

// Answer:
// 1.
// let number = 47;
// number %= 6;
// console.log(number)

// 2.
// let count = 23;
// count %= 12;
// console.log(count)

// 3.
// 4

// 4.
// 2

// 5.
// remainder by 0 is undefined, JavaScript gives NaN.

// 7. Exponentiation and Assign -------------------------------------------------------
// Side of a cube is 5. Update it to get the volume using **= 3.
// Number 4 needs to be squared. Use **= 2.
// Predict the output:
// let base = 2;
// base **= 5;
// console.log(base);
// Predict the output:
// let n = 4;
// n **= 0.5;
// console.log(n);
// What is the result of let p = 2; p **= -1;? Explain.

// Answer:
// 1.
// let side=5;
// side **=3;
// console.log("Cube",side);
// 2.
// let num = 4;
// num **= 2;
// console.log(num);
--------------------------------------------------------------------------------------------------------------------------------------------
// D] Relational Operator

// 1. Greater Than

// Question 1
// let studentMarks = 78;
// let passingMarks = 40;
// let result = studentMarks>passingMarks
// console.log("Student has scored more?", result);

// Question 2
// let tempToday = 35;
// let tempYesterday = 28;
// let isHotter = tempToday>tempYesterday
// console.log("Is today hotter?", isHotter);

// Question 3
// console.log(15 > 10); // true
// console.log(10 > 15); // false
// console.log(10 > 10); // false

// Question 4
// console.log("20" > 15); // true
// console.log("5" > "10"); // true
// console.log("abc" > 10); // false

// Question 5
// console.log(null > 0); // false because null gets converted to 0 and 0 > 0 results in false
// console.log(undefined > 0); // false because undefined gets converted to NaN and NaN > 0 results in false 

// Question 6
// let itemsStock = 120
// let itemsRequired = 85
// let isSufficient = itemsStock > itemsRequired
// console.log("Is stock sufficient?", isSufficient);

// Question 7
// console.log(true > false); // true because true gets converted to 1 and false gets converted to 0 and then 1>0 results in true
// console.log("10" > "2"); // false because the each character of first string gets compared to the corresponding character of the second string
// console.log(NaN > 5); // false because any comparison with NaN results is false


// 2. Less Than

// Question 1
// let maxWeight = 50
// let currentWeight = 42
// let canAddItems = currentWeight < maxWeight
// console.log("Can more items still be added?", canAddItems);

// Question 2
// let minAge = 18
// let personAge = 16
// let isUnderage = personAge < minAge
// console.log("Is the person underage?", isUnderage);

// Question 3
// console.log(8 < 12); // true
// console.log(20 < 10); // false
// console.log(7 < 7); // false

// Question 4
// console.log("8" < 10); // true
// console.log("20" < "3"); // true
// console.log("hello" < 5); // false

// Question 5
// The result of null < 0 is false because null gets converted to 0 and 0 < 0 results in false and undefined < 0 is false because undefined gets converted to NaN and NaN < 0 results in false
// console.log(null < 0);
// console.log(undefined < 0);

// Question 6
// let tankCapacity = 500
// let waterLevel = 375
// let isNotFull = waterLevel < tankCapacity
// console.log("Is the tank not full?", isNotFull);

// Question 7
// console.log(false < true); // true because false gets converted to 0 and true gets converted to 1 and then 0 < 1 results in true
// console.log("5" < "15"); // false false because the each character of first string gets compared to the corresponding character of the second string
// console.log(NaN < 10); // false because any comparison with NaN results in false


// 3. Greater Than or Equal To

// Question 1
// let marksRequired = 75
// let marksScored = 75
// let getsDistinction = marksScored >= marksRequired
// console.log("Student gets distiction?", getsDistinction);

// Question 2
// let ticketPrice = 300
// let personBal = 300
// let canBuyTicket = personBal >= ticketPrice
// console.log("Can they buy the ticket?", canBuyTicket);

// Question 3
// console.log(25 >= 25); // true
// console.log(30 >= 25); // true
// console.log(20 >= 25); // false

// Question 4
// console.log("25" >= 25); // true
// console.log("10" >= "2"); // false
// console.log(null >= 0); // true

// Question 5
// The result of undefined >= 0 is false because undefined gets converted to NaN and any comparison with NaN results in false
// console.log(undefined >= 0);

// Question 6
// A lift can carry maximum 8 people. Currently 8 people are inside. Write a condition using >= to check if the lift is full or overloaded.
// let liftCapacity = 8
// let peopleInside = 8
// let isFull = peopleInside >= liftCapacity
// console.log("Is lift full?", isFull);

// Question 7
// console.log(true >= 1); // true because true gets converted to 1 and then 1>=1 results in true
// console.log("" >= 0); // true because "" gets converted to 0 and then 0 >= 0 results in true
// console.log(NaN >= NaN); // false because any comparison with NaN results in false


// 4. Less Than or Equal To

// Question 1
// let maxSpeedLimit = 60
// let vehicleSpeed = 60
// let isWithinLimit = vehicleSpeed <= maxSpeedLimit
// console.log("Is vehicle within speed limit?", isWithinLimit);

// Question 2
// let marksPassing = 40
// let marksStudent = 39
// let isFailed = marksStudent <= (marksPassing-1)
// console.log("Has student failed?", isFailed);

// Question 3
// console.log(15 <= 20); // true
// console.log(20 <= 15); // false
// console.log(15 <= 15); // true

// Question 4
// console.log("15" <= 20); // true
// console.log("30" <= "5"); // true
// console.log(null <= 0); // true

// Question 5
// The result of undefined <= 0 is false because undefined gets converted to NaN and any comparison with NaN results in false
// console.log(undefined <= 0);

// Question 6
// let bagCapacity = 10
// let booksCurrentlyInBag = 10
// let canAddBooks = booksCurrentlyInBag <= (bagCapacity-1)
// console.log("Can more books be added?", canAddBooks);

// Question 7
// console.log(false <= 0); // true because false get converted to 0 and then 0 <= 0 results in true
// console.log("" <= 0); // true because "" get converted to 0 and then 0 <= 0 results in true
// console.log(NaN <= 5); // false because any comparison with NaN results in false


// C] Comparison Operators

// 1. Loose Equality

// Question 1
// console.log("25" == 25); // true

// Question 2
// console.log(0==false); // true


// Question 3
// console.log(10 == "10"); // true
// console.log(null == undefined); // true

// Question 4
// console.log("" == 0); // true
// console.log([] == false); // true

// Question 5
// NaN == NaN returns false


// 2. Loose Inequality

// Question 1
// console.log("18" != 18); // false

// Question 2
// let password = "1234"
// let enterPass = 1234
// console.log(password != enterPass); // false

// Question 3
// console.log(5 != "5"); // false
// console.log(0 != false); // false

// Question 4
// console.log(null != undefined); // false
// console.log("" != 0); // false

// Question 5
// NaN != NaN returns true


// 3. Strict Equality

// Question 1
// console.log("25" === 25); // false because value is equal but data type is different

// Question 2
// console.log(0 === false); // false
// console.log(null === undefined); // false

// Question 3
// console.log(10 === "10"); // false
// console.log(true === 1); // false

// Question 4
// console.log("" === 0); // false
// console.log([] === false); // false

// Question 5
// === is prefered because it checks both value and datatype


// 4. Strict Inequality

// Question 1
// console.log("18" !== 18); // true

// Question 2
// console.log(0 !== false); // true
// console.log(null !== undefined); // true

// Question 3
// console.log(5 !== "5"); // true
// console.log(true !== 1); // true

// Question 4
// console.log("" !== 0); // true
// console.log(NaN !== NaN); // true

// Question 5
// let input = ""
// console.log(input !== "0"); // true


// Mixed Practice

// Question 1

// Whether age 18 is greater than or equal to voting age 18.
// let votingAge = 18
// let age = 18
// let result = age >= votingAge
// console.log(result);

// Whether temperature 32 is less than 35.
// let temperature1 = 35
// let temperature2 = 32
// let result = temperature2 < temperature1
// console.log(result);

// Whether score 90 is greater than 85.
// let score1 = 85
// let score2 = 90
// let result = score2 > score1
// console.log(result);

// Question 2
// console.log(10 > 5 && 5 < 10); // true
// console.log("10" >= 10); // true
// console.log(null <= undefined); // false
// console.log("5" < "10" && 5 > 2); // false

// Question 3
// let productCost = 499
// let customerBal = 500
// let canBuy = customerBal >= productCost  
// let isChangeLeft = productCost < customerBal
// console.log("Can customer buy the product?", canBuy);
// console.log("Will any change be left?", isChangeLeft);

// Question 4
// "10" > "2" is false but 10 > 2 is true because when two strings are compared then each character of the first string is compared to the corresponding character of the second string and when both the operands are numbers then they are compared on their numerical value


---------------------------------------------------------------------------============================================-===========================================================================

PART E: QUESTIONS AND ANSWERS;;;;;;;;;;;;
{/* question1 */}
{/* let counter = 5;
counter++;
console.log(counter);  */}

{/* question2 */}
{/* let lives = 3;
lives--;
console.log(lives); */}

{/* question3 */}
{/* let score = 10;
score++;
console.log(score); */}

{/* question4 */}
{/* let items = 8;
items--;
console.log(items); */}

{/* question5 */}
{/* let count = 0;
count++;
count++;
console.log(count); */}

{/* question6 */}
{/* let x=5;
let y=x++;
console.log("x =", x); 
console.log("y =", y); */}
{/* In postfix (x++), JavaScript gives the current value of x (which is 5) to y first, and then increases x by 1. That is why y is 5 and x becomes 6. */}

{/* question7 */}
{/* let a = 5;
let b = ++a;
console.log("a =", a); // Output: 6
console.log("b =", b); */}
{/* In prefix (++a), JavaScript increases a by 1 first (making it 6), and then gives that new value to b. That is why both a and b are 6. */}

{/* question8 */}
{/* let lives = 3;
let previousLives = lives--;
console.log("lives =", lives);               
console.log("previousLives =", previousLives) */}

{/* question9 */}
{/* let attempts = 0;
let currentAttempts = ++attempts;
console.log("attempts =", attempts)
console.log("currentAttempts =", currentAttempts) */}

{/* question10:
let points = 100;
points++; 
points--; 
console.log(points); */}

{/* PREDICTING OUTPUTS___________________________ */}

{/* question11 */}
{/* 12, 10, 12 */}


{/* question12
5, 10 */}


{/* question13
7, 12 */}


{/* question14
5, 13 */}


{/* question15
2 */}
=================================================================================================================
// F] Logical Operators

// 1. Logical AND

// Question 1
// let storedUsername = "admin"
// let storedPassword = 1234
// let enteredUsername = "sdf"
// let enteredPassword = 1234
// let isUsernameValid = storedUsername == enteredUsername
// let isPasswordValid = storedPassword == enteredPassword
// let areBothValid = isPasswordValid && isUsernameValid
// console.log("Are both valid?", areBothValid);

// Question 2
// let isLoggedIn = true
// let hasPermission = true
// let canAccess = isLoggedIn && hasPermission
// console.log("Can the user access the page?", canAccess);

// Question 3
// let inStock = true
// let price = 800
// let isWithinBudget = price <= 1000
// let canBuy = inStock && isWithinBudget
// console.log("Can it be bought?", canBuy);

// Question 4
// let marks = 75
// let attendance = 80
// let hasPassed = (marks > 65) && (attendance > 70)
// console.log("Has student passed?", hasPassed);

// Question 5
// let isWeekend = true
// let isHoliday = false
// let willPartyHappen = isWeekend && isHoliday
// console.log("Will party happen?", willPartyHappen);

// Question 6
// let a = 0;
// let b = 10;
// let result = a && b;
// console.log(result); // 0

// Question 7
// let x = 5;
// let y = 10;
// let result = (x > 3 && y) || 0;
// console.log(result); // 10

// Question 8
// let p = "Hello";
// let q = "";
// let r = "World";
// let result = p && q && r;
// console.log(result); // ""

// Question 9
// let val = 5;
// let condition = val && (val = 0);
// console.log(condition); // 0
// console.log(val); // 0

// Question 10
// let x = 10;
// let y = 20;
// let result = (x && y) && (x > y);
// console.log(result); // false


// 2. Logical OR

// Question 1
// let passwordCorrect = true
// let otpValid = false
// let loginAllowed = passwordCorrect || otpValid
// console.log("Is login allowed?", loginAllowed);

// Question 2
// let isMember = false
// let hasCoupon = true
// let isDiscountApplied = isMember || hasCoupon
// console.log("Is the discount applied?", isDiscountApplied);

// Question 3
// let age = 16
// let height = 155
// let entryAllowed = (age > 18) || (height > 150)
// console.log("Is entry allowed?", entryAllowed);

// Question 4
// let emailGiven = true
// let phoneGiven = false
// let isFormValid = emailGiven || phoneGiven
// console.log("Is form valid?", isFormValid);

// Question 5
// let score = 900
// let timeBonus = true
// let gameLevelOpens = (score > 1000) || timeBonus
// console.log("Is game level open?", gameLevelOpens);

// Question 6
// let a = 0;
// let b = false;
// let c = "";
// let d = null;
// let e = 42;
// let result = a || b || c || d || e;
// console.log(result); // 42

// Question 7
// let x = "Hello" || 0;
// let y = 0 || "Hi";
// console.log(x, y); // Hello Hi

// Question 8
// let a = 10;
// let b = 20;
// let result = (a < 5) || (b > 15);
// console.log(result); // true

// Question 9
// let val = 5;
// let condition = val || (val = 0);
// console.log(condition); // 5
// console.log(val); // 5

// Question 10
// let x = "" || 0 || false || null || undefined || "OK";
// console.log(x); // OK


// 1. Logical NOT

// Question 1
// let isBanned = false
// let canLogin =!isBanned
// console.log("Can the user login?", canLogin);

// Question 2
// let isCompleted = false
// let isPending = !isCompleted
// console.log("Is the task still pending?", isPending);

// Question 3
// let isOn = true
// let isOff = !isOn
// console.log("Is the light off?", isOff);

// Question 4
// let isActive = false
// let cannotAccess = !isActive
// console.log("Can the user not access premium content?", cannotAccess);

// Question 5
// let isReadOnly = false
// let canEdit = !isReadOnly
// console.log("Can the file be edited?", canEdit);

// Question 6
// let a = 0;
// let b = 1;
// console.log(!a, !b); // true false

// Question 7
// let x = "Hello";
// let y = "";
// console.log(!x, !y); // false true

// Question 8
// let val = 5;
// let result = !val;
// console.log(result); // false

// Question 9
// let a = 10;
// let b = 20;
// let result = !(a && b);
// console.log(result); // false

// Question 10
// let x = 0;
// let y = 1;
// let result = !(x || y);
// console.log(result); // false



// G] typeof Operator

// Question 1
// let name = "Rahul"
// console.log(typeof name);

// Question 2
// let age = 25
// console.log(typeof age);

// Question 3
// let isStudent = true
// console.log(typeof isStudent);

// Question 4
// let city
// console.log(typeof city);

// Question 5
// console.log(typeof null);

// Question 6
// console.log(typeof 42); // number
// console.log(typeof "Hello"); // string
// console.log(typeof true); // boolean
// console.log(typeof undefined); // undefined

// Question 7
// console.log(typeof null); // object
// console.log(typeof {}); // object
// console.log(typeof []); // object

// Question 8
// console.log(typeof NaN); // number
// console.log(typeof Infinity); // number
// console.log(typeof function(){}); // function

// Question 9
// let price = 99.99
// let message = "Welcome"
// let isActive = false
// console.log("The type of", price, "is", typeof price);
// console.log("The type of", message, "is", typeof message);
// console.log("The type of", isActive, "is", typeof isActive);

// Question 10
// let value = null;
// console.log(typeof value); // object
// console.log(typeof value === "object"); // true

// Question 11
// console.log(typeof typeof 100); // string
// console.log(typeof typeof "Hi"); // string
// console.log(typeof typeof true); // string

// Question 12
// let a = 10;
// let b = "10";
// console.log(typeof a === typeof b); // false
// console.log(typeof a == typeof b); // false

// Question 13
// console.log(typeof null === "object"); // true
// console.log(typeof [] === "object"); // true
// console.log(typeof {} === "object"); // true

// Question 14
// let x;
// console.log(typeof x); // undefined
// x = null;
// console.log(typeof x); // object
// x = 0;
// console.log(typeof x); // number

// Question 15
// console.log(typeof NaN === "number"); // true
// console.log(typeof Infinity === "number"); // true
// console.log(typeof (1 / 0)); // number



// H] Type Coercion

// Question 1
// let string = "25"
// string = Number(string)
// string += 10
// console.log(string);

// Question 2
// let number = 100
// number = number(number)
// number += " rupees"
// console.log(number);

// Question 3
// let value = 0
// value = Boolean(value)
// console.log(value);

// Question 4
// let value = "Hello"
// value = Boolean(value)
// console.log(value);

// Question 5
// let string = "50"
// string = +string
// string *= 2
// console.log(string);

// Question 6
// console.log("10" - 5); // 5
// console.log("10" + 5); // 105
// console.log("10" * 2); // 20
// console.log("10" / 2); // 5

// Question 7
// console.log("5" - "2"); // 3
// console.log("5" + "2"); // 52
// console.log("5" * "2"); // 10
// console.log("5" / "2"); // 2.5

// Question 8
// console.log(Number("123")); // 123
// console.log(Number("123abc")); // NaN
// console.log(Number(true)); // 1
// console.log(Number(false)); // 0
// console.log(Number(null)); // 0
// console.log(Number(undefined)); // NaN

// Question 9
// console.log(Boolean(0)); // false
// console.log(Boolean("")); // false
// console.log(Boolean("0")); // true
// console.log(Boolean([])); // true
// console.log(Boolean({})); // true
// console.log(Boolean(null)); // false

// Question 10
// console.log(String(100)); // "100"
// console.log(String(true)); // "true"
// console.log(String(null)); // "null"
// console.log(String(undefined)); // "undefined"
// console.log(100 + ""); // "100"

// Question 11
// console.log("5" + 3 + 2); // "532"
// console.log(5 + 3 + "2"); // "82"
// console.log("5" - 3 + 2); // 4
// console.log(5 - "3" + "2"); // "22"

// Question 12
// console.log(true + true); // 2
// console.log(true + false); // 1
// console.log(true + "false"); // "truefalse"
// console.log(false + "true"); // "falsetrue"

// Question 13
// console.log(null + 5); // 5
// console.log(undefined + 5); // NaN
// console.log(null + "5"); // "null5"
// console.log(undefined + "5"); // "undefined5"

// Question 14
// console.log([] + []); // 
// console.log([] + {}); // [object object]
// console.log({} + []); //  [object object]
// console.log({} + {}); //  [object object][object object]

// Question 15
// let a = "10";
// let b = 5;
// let c = a + b;
// let d = a - b;
// let e = +a + b;
// console.log(c, typeof c); // "105" "string"
// console.log(d, typeof d); // 5 "number"
// console.log(e, typeof e); // 15 "number"

// Question 16
// console.log(!!"Hello"); // true
// console.log(!!""); // false
// console.log(!!0); // false
// console.log(!!1); // true
// console.log(!!null); // false
// console.log(!!undefined); // false

// Question 17
// console.log(Number("")); // 0
// console.log(Number(" ")); // 0
// console.log(Number("0")); // 0
// console.log(Number("  25  ")); // 25
// console.log(Number("25px")); // NaN

// Question 18
// let val1 = "5";
// let val2 = 2;
// console.log(val1 + val2); // "52"
// console.log(+val1 + val2); // 7
// console.log(val1 - val2); // 3
// console.log(val1 * val2); // 10
// console.log(val1 / val2); // 2.5

// Question 19
// let count = 5;
// console.log(typeof count++); // number
// console.log(count); // 6
// console.log(typeof ++count); // number
// console.log(count); // 7

// Question 20
// let x = "10";
// let y = ++x;
// console.log(x, y, typeof x, typeof y); // 11 11 number number

// Question 21
// let a = "5";
// let b = a++;
// console.log(a, b, typeof a, typeof b); // 6 5 number number

// Question 22
// console.log(typeof (1 + "2")); // string
// console.log(typeof (1 - "2")); // number
// console.log(typeof (1 * "2")); // number
// console.log(typeof (1 / "2")); // number

// Question 23
// let val = null;
// console.log(typeof val); // object
// console.log(val + 1); // 1
// console.log(val - 1); // -1
// console.log(val * 1); // 0
// console.log(Boolean(val)); // false
=====================================================================================================================================================================
`if` Statement 

1. Write a program to check if a number is divisible by 5. If yes, print “Divisible by 5”.

2. Check if a person’s age is greater than or equal to 60. If true, print “Senior Citizen”.

3. Write a program that checks if a given number is greater than 100. If yes, print “Big Number”.

4. Check if the temperature is less than 10. If true, print “Very Cold”.

5. Write a program to check if a student scored full marks (100). If yes, print “Perfect Score”.

6. Check if a number is negative. If it is, print “Negative Number”.

7. Write a program that checks if a user has entered an empty string. If the string is empty, print “No input provided”.

8. Check if a given year is divisible by 100. If yes, print “Century Year”.

9. Write a program to check if a number is both positive and even using a single `if` condition. If true, print “Positive Even Number”.

10. Check if the value of a variable `marks` is greater than or equal to 35 **and** less than or equal to 100. If true, print “Valid Marks”.

---
// ============================================================================================================
q1.
  let num=5;
let isDivisible=num%5==0;
if (isDivisible == true){
  console.log("is divisible by 5")
}

q2.
  let age=65;
  if (age >= 60) {
    console.log("Senior Citizen");
}
q3.
  let number = 150;
if (number > 100) {
    console.log("Big Number");
}
q4.
  let temperature = 5;
if (temperature < 10) {
    console.log("Very Cold");
}

q5.
  let score = 100;
if (score == 100) {
    console.log("Perfect Score");
}

q6.
  let n = -8;
if (n < 0) {
    console.log("Negative Number");
}
q7.
  let str = "";
if (str == "") {
    console.log("No input provided");
}
q8.
  let year = 2000;
if (year % 100 == 0) {
    console.log("Century Year");
}

q9.
  let value = 8;
if (value > 0 && value % 2 == 0) {
    console.log("Positive Even Number");
}
Q10.
  let marks= 55;;
if (marks>=35 && marks<=100){
  console.log("valid score")
}
// ==========================================================================================================

 B] `if...else` Statement 

1. Write a program to check whether a number is even or odd.

2. Check if a person is eligible to vote (age ≥ 18). Print “Eligible” or “Not Eligible”.

3. Write a program that checks whether a number is positive or negative.

4. Check if a student has passed or failed based on marks (pass mark = 35).

5. Write a program to check whether a given character is an uppercase letter or not.  
   (Hint: Use character comparison)

6. Check if a number is divisible by 3 or not. Print appropriate messages.

7. Write a program that takes a password as input. If the password is “admin123”, print “Login Successful”, otherwise print “Incorrect Password”.

8. Check whether a given year is a leap year or not using the basic rule (divisible by 4).

9. Write a program to find the greater of two numbers using `if...else`.

10. Check if a number is positive, negative, or zero using only `if...else` (you may use nested or multiple conditions carefully).

  // ==========================================================================================================

  q1.
  let num = 8;
if (num % 2 == 0) {
    console.log("Even");
} else {
    console.log("Odd");
}

q2.
  let age = 20;
if (age >= 18) {
    console.log("Eligible");
} else {
    console.log("Not Eligible");
}

  Q3.
    let number = -5;
if (number >= 0) {
    console.log("Positive");
} else {
    console.log("Negative");
}
q4.
  let marks = 40;
if (marks >= 35) {
    console.log("Passed");
} else {
    console.log("Failed");
}
q5.
  let ch = "A";
if (ch >= "A" && ch <= "Z") {
    console.log("Uppercase Letter");
} else {
    console.log("Not an Uppercase Letter");
}
                                                                                               
q6.
      let n = 12;
if (n % 3 == 0) {
    console.log("Divisible by 3");
} else {
    console.log("Not Divisible by 3");
}

q7.
  let password = "admin123";
if (password == "admin123") {
    console.log("Login Successful");
} else {
    console.log("Incorrect Password");
}

q8.
  let year = 2024;
if (year % 4 == 0) {
    console.log("Leap Year");
} else {
    console.log("Not a Leap Year");
}
q9.
  let a = 25;
let b = 15;
if (a > b) {
    console.log(a + " is greater");
} else {
    console.log(b + " is greater or equal");
}
q10.
  let value = 0;
if (value > 0) {
    console.log("Positive");
} else {
    if (value < 0) {
        console.log("Negative");
    } else {
        console.log("Zero");
    }
}

C] if...else if...else Statement
1. Print the season based on month
let month = 4;
if (month == 12 || month == 1 || month == 2) {
    console.log("Winter");
} else if (month >= 3 && month <= 5) {
    console.log("Summer");
} else if (month >= 6 && month <= 8) {
    console.log("Monsoon");
} else if (month >= 9 && month <= 11) {
    console.log("Autumn");
} else {
    console.log("Invalid Month");
}


2. Simple tax calculator
let income = 500000;
let tax;
if (income < 300000) {
    tax = 0;
} else if (income <= 700000) {
    tax = income * 0.05;
} else if (income <= 1000000) {
    tax = income * 0.10;
} else {
    tax = income * 0.15;
}

console.log("Tax:", tax);


3. Student score
let marks = 85;
if (marks >= 90) {
    console.log("Outstanding");
} else if (marks >= 70) {
    console.log("Good");
} else if (marks >= 40) {
    console.log("Average");
} else {
    console.log("Needs Improvement");
}


4. Vehicle speed
let speed = 60;
if (speed < 40) {
    console.log("Slow");
} else if (speed <= 80) {
    console.log("Normal");
} else {
    console.log("Fast");
}


5. Person's height
let height = 165;
if (height < 150) {
    console.log("Short");
} else if (height <= 170) {
    console.log("Average");
} else {
    console.log("Tall");
}


6. Weekday or weekend
let day = 6;
if (day >= 1 && day <= 5) {
    console.log("Weekday");
} else if (day == 6 || day == 7) {
    console.log("Weekend");
} else {
    console.log("Invalid Day");
}


7. Electricity bill
The question gives a rate for each unit range, so this solution applies the rate to all units consumed.
let units = 120;
let bill;

if (units <= 50) {
    bill = units * 2;
} else if (units <= 150) {
    bill = units * 4;
} else {
    bill = units * 6;
}

console.log("Bill: ₹" + bill);


8. Attendance percentage
let attendance = 85;
if (attendance >= 90) {
    console.log("Excellent");
} else if (attendance >= 75) {
    console.log("Good");
} else if (attendance >= 50) {
    console.log("Satisfactory");
} else {
    console.log("Poor");
}


9. Find the highest of three marks
let a = 75;
let b = 90;
let c = 80;
if (a >= b && a >= c) {
    console.log(a);
} else if (b >= a && b >= c) {
    console.log(b);
} else {
    console.log(c);
}


10. Positive/negative and even/odd
let n = -7;
if (n == 0) {
    console.log("Zero");
} else if (n > 0 && n % 2 == 0) {
    console.log("Positive Even");
} else if (n > 0) {
    console.log("Positive Odd");
} else if (n % 2 == 0) {
    console.log("Negative Even");
} else {
    console.log("Negative Odd");
}



D] Nested if Statement
1. Greater than 10 and divisible by 3
let n = 15;
if (n > 10) {
    if (n % 3 == 0) {
        console.log("Greater than 10 and divisible by 3");
    } else {
        console.log("Greater than 10 but not divisible by 3");
    }
} else {
    console.log("Not greater than 10");
}


2. Voting eligibility
let age = 20;
let voterID = true;
if (age >= 18) {
    if (voterID == true) {
        console.log("Can Vote");
    } else {
        console.log("Voter ID required");
    }
} else {
    console.log("Not eligible");
}


3. Pass and distinction
let marks = 85;
if (marks >= 40) {
    console.log("Passed");
    if (marks >= 80) {
        console.log("Passed with Distinction");
    }
} else {
    console.log("Failed");
}


4. ATM system
let pin = 1234;
let balance = 5000;
let amount = 2000;
let correctPin = 1234;

if (pin == correctPin) {
    if (balance >= amount) {
        console.log("Withdrawal Successful");
    } else {
        console.log("Insufficient Balance");
    }
} else {
    console.log("Incorrect PIN");
}


5. Leap year
let year = 2024;
if (year % 4 == 0) {
    if (year % 100 == 0) {
        if (year % 400 == 0) {
            console.log("Leap Year");
        } else {
            console.log("Not a Leap Year");
        }
    } else {
        console.log("Leap Year");
    }
} else {
    console.log("Not a Leap Year");
}


6. Email validation
let email = "student@gmail.com";
if (email.includes("@")) {
    if (email.endsWith(".com")) {
        if (email.length > 10) {
            console.log("Valid Email");
        } else {
            console.log("Email is too short");
        }
    } else {
        console.log("Email must end with .com");
    }
} else {
    console.log("Email must contain @");
}


7. Online shopping discount
let total = 2000;
let premium = true;
let discount = 0;
if (total >= 1000) {
    if (premium == true) {
        discount = total * 0.20;
    } else {
        discount = total * 0.10;
    }
}

let finalAmount = total - discount;
console.log("Final Amount:", finalAmount);


8. Positive, even and divisible by 4
let n = 16;
if (n > 0) {
    if (n % 2 == 0) {
        if (n % 4 == 0) {
            console.log("Positive Even and Divisible by 4");
        } else {
            console.log("Positive Even");
        }
    } else {
        console.log("Positive Odd");
    }
} else {
    console.log("Not Positive");
}


9. Job eligibility
let age = 25;
let degree = true;
let experience = 3;
if (age >= 21 && age <= 30) {
    if (degree == true) {
        if (experience >= 2) {
            console.log("Eligible for Interview");
        } else {
            console.log("Insufficient Experience");
        }
    } else {
        console.log("Degree Required");
    }
} else {
    console.log("Age Not Eligible");
}


10. Exam eligibility
let present = true;
let internal = 35;
let external = 40;
if (present == true) {
    if (internal >= 30) {
        if (external >= 35) {
            console.log("Eligible for Final Exam");
        } else {
            console.log("External Marks Insufficient");
        }
    } else {
        console.log("Internal Marks Insufficient");
    }
} else {
    console.log("Student is Absent");
}



E] switch Statement
1. Number of days in a month
let month = 2;
switch (month) {
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
        console.log("31 days");
        break;

    case 4:
    case 6:
    case 9:
    case 11:
        console.log("30 days");
        break;

    case 2:
        console.log("28 days");
        break;

    default:
        console.log("Invalid Month");
}


2. Vowel or consonant
let ch = "a";
switch (ch.toLowerCase()) {
    case "a":
    case "e":
    case "i":
    case "o":
    case "u":
        console.log("Vowel");
        break;

    default:
        console.log("Consonant");
}


3. Season using multiple cases
let n = 3;
switch (n) {
    case 1:
    case 2:
        console.log("Winter");
        break;

    case 3:
    case 4:
        console.log("Summer");
        break;

    default:
        console.log("Invalid Number");
}


4. Class based on marks using switch(true)
let marks = 80;
switch (true) {
    case marks >= 75:
        console.log("Distinction");
        break;

    case marks >= 60:
        console.log("1st Class");
        break;

    case marks >= 50:
        console.log("2nd Class");
        break;

    case marks >= 35:
        console.log("3rd Class");
        break;

    default:
        console.log("Failed");
}


5. Nested switch for admin and user
let role = "admin";
let action = "edit";
switch (role) {
    case "admin":
        switch (action) {
            case "create":
                console.log("Create Item");
                break;

            case "edit":
                console.log("Edit Item");
                break;

            case "delete":
                console.log("Delete Item");
                break;

            default:
                console.log("Invalid Action");
        }
        break;

    case "user":
        console.log("Limited Access");
        break;

    default:
        console.log("Invalid Role");
}


6. Predict and correct the output
Original output:
Mango is yellow
Banana is yellow
Unknown fruit


This happens because there is no break after the "mango" case, so JavaScript continues to the next cases. This is called fall-through.
Correct code:
let fruit = "mango";

switch (fruit) {
    case "apple":
        console.log("Apple is red");
        break;

    case "mango":
        console.log("Mango is yellow");
        break;

    case "banana":
        console.log("Banana is yellow");
        break;

    default:
        console.log("Unknown fruit");
}
7. Identify different values using switch
let value = "0";
switch (value) {
    case 0:
        console.log("Number Zero");
        break;

    case "0":
        console.log("String Zero");
        break;

    case false:
        console.log("Boolean False");
        break;

    case null:
        console.log("Null Value");
        break;

    case undefined:
        console.log("Undefined Value");
        break;

    default:
        console.log("Other Value");
}


Explanation: JavaScript switch uses strict comparison (===). Therefore, 0, "0", and false are different values.
8. Calculator using switch
let a = 10;
let b = 3;
let op = "**";
switch (op) {
    case "+":
        console.log(a + b);
        break;

    case "-":
        console.log(a - b);
        break;

    case "*":
        console.log(a * b);
        break;
    case "/":
        if (b == 0) {
            console.log("Cannot divide by zero");
        } else {
            console.log(a / b);
        }
        break;

    case "%":
        console.log(a % b);
        break;

    case "**":
        console.log(a ** b);
        break;

    default:
        console.log("Invalid Operator");
}


9. Beginning, middle or end of the month
let day = 15;
switch (true) {
    case day >= 1 && day <= 10:
        console.log("Beginning of the month");
        break;
    case day >= 11 && day <= 20:
        console.log("Middle of the month");
        break;
    case day >= 21 && day <= 31:
        console.log("End of the month");
        break;
    default:
        console.log("Invalid Day");
}


10. Online food ordering system
let category = "veg";
let item = "pizza";
let size = "full";
let price = 0;

switch (category) {
    case "veg":
        switch (item) {
            case "pizza":
                price = 200;
                break;

            case "burger":
                price = 100;
                break;

            default:
                console.log("Invalid Veg Item");
        }
        break;

    case "nonveg":
        switch (item) {
            case "pizza":
                price = 300;
                break;

            case "burger":
                price = 150;
                break;

            default:
                console.log("Invalid Nonveg Item");
        }
        break;

    default:
        console.log("Invalid Category");
}

if (price > 0) {
    switch (size) {
        case "half":
            price = price / 2;
            break;

        case "full":
            break;

        default:
            price = 0;
            console.log("Invalid Size");
    }
    if (price > 0) {
        console.log("Category:", category);
        console.log("Item:", item);
        console.log("Size:", size);
        console.log("Price: ₹" + price);
    }
}



F] Ternary Operator Questions
The basic format is:
condition ? valueIfTrue : valueIfFalse
1. Divisible by 7
let n = 21;

let result = n % 7 == 0
    ? "Divisible by 7"
    : "Not Divisible by 7";

console.log(result);


2. Temperature
let temperature = 32;
let result = temperature >= 30 ? "Hot Day" : "Pleasant Day";

console.log(result);


3. Check empty string
let str = "";
let result = str == "" ? "Empty String" : "String has content";

console.log(result);
4. Age classification using nested ternary
let age = 16;
let result = age < 13
    ? "Child"
    : age <= 19
    ? "Teenager"
    : "Adult";
console.log(result);


5. Greatest of three numbers
let a = 10, b = 25, c = 15;
let result = a >= b && a >= c
    ? a
    : b >= c
    ? b
    : c;
console.log(result);


6. Student marks classification
let marks = 65;
let result = marks >= 75
    ? "Distinction"
    : marks >= 60
    ? "First Class"
    : marks >= 50
    ? "Second Class"
    : marks >= 35
    ? "Pass"
    : "Fail";
console.log(result);


7. Positive/negative and even/odd
let n = -7;
let result = n == 0
    ? "Zero"
    : n > 0
    ? n % 2 == 0 ? "Positive Even" : "Positive Odd"
    : n % 2 == 0 ? "Negative Even" : "Negative Odd";

console.log(result);


8. Leap year using nested ternary
let year = 2024;
let result = year % 4 == 0
    ? year % 100 == 0
        ? year % 400 == 0 ? "Leap Year" : "Not a Leap Year"
        : "Leap Year"
    : "Not a Leap Year";

console.log(result);


9. Role and action using one nested ternary
let role = "admin";
let action = "delete";
let result = role == "admin"
    ? action == "delete"
        ? "Admin Delete"
        : action == "edit"
        ? "Admin Edit"
        : "Admin Other"
    : role == "user"
        ? action == "view"
            ? "User View"
            : "User Restricted"
        : "Invalid Role";

console.log(result);


10. Discount and final amount using one expression
let cart = 3000;
let result = {
    discount: cart >= 5000 ? 20
        : cart >= 2000 ? 10
        : cart >= 1000 ? 5
        : 0,
    payable: cart - cart * (
        cart >= 5000 ? 0.20
        : cart >= 2000 ? 0.10
        : cart >= 1000 ? 0.05
        : 0
    )
};

console.log(result);
For a cart total of ₹3,000, the result is:
discount: 10%
payable: ₹2700C] if...else if...else Statement
1. Print the season based on month
let month = 4;
if (month == 12 || month == 1 || month == 2) {
    console.log("Winter");
} else if (month >= 3 && month <= 5) {
    console.log("Summer");
} else if (month >= 6 && month <= 8) {
    console.log("Monsoon");
} else if (month >= 9 && month <= 11) {
    console.log("Autumn");
} else {
    console.log("Invalid Month");
}


2. Simple tax calculator
let income = 500000;
let tax;
if (income < 300000) {
    tax = 0;
} else if (income <= 700000) {
    tax = income * 0.05;
} else if (income <= 1000000) {
    tax = income * 0.10;
} else {
    tax = income * 0.15;
}

console.log("Tax:", tax);


3. Student score
let marks = 85;
if (marks >= 90) {
    console.log("Outstanding");
} else if (marks >= 70) {
    console.log("Good");
} else if (marks >= 40) {
    console.log("Average");
} else {
    console.log("Needs Improvement");
}


4. Vehicle speed
let speed = 60;
if (speed < 40) {
    console.log("Slow");
} else if (speed <= 80) {
    console.log("Normal");
} else {
    console.log("Fast");
}


5. Person's height
let height = 165;
if (height < 150) {
    console.log("Short");
} else if (height <= 170) {
    console.log("Average");
} else {
    console.log("Tall");
}


6. Weekday or weekend
let day = 6;
if (day >= 1 && day <= 5) {
    console.log("Weekday");
} else if (day == 6 || day == 7) {
    console.log("Weekend");
} else {
    console.log("Invalid Day");
}


7. Electricity bill
The question gives a rate for each unit range, so this solution applies the rate to all units consumed.
let units = 120;
let bill;

if (units <= 50) {
    bill = units * 2;
} else if (units <= 150) {
    bill = units * 4;
} else {
    bill = units * 6;
}

console.log("Bill: ₹" + bill);


8. Attendance percentage
let attendance = 85;
if (attendance >= 90) {
    console.log("Excellent");
} else if (attendance >= 75) {
    console.log("Good");
} else if (attendance >= 50) {
    console.log("Satisfactory");
} else {
    console.log("Poor");
}


9. Find the highest of three marks
let a = 75;
let b = 90;
let c = 80;
if (a >= b && a >= c) {
    console.log(a);
} else if (b >= a && b >= c) {
    console.log(b);
} else {
    console.log(c);
}


10. Positive/negative and even/odd
let n = -7;
if (n == 0) {
    console.log("Zero");
} else if (n > 0 && n % 2 == 0) {
    console.log("Positive Even");
} else if (n > 0) {
    console.log("Positive Odd");
} else if (n % 2 == 0) {
    console.log("Negative Even");
} else {
    console.log("Negative Odd");
}



D] Nested if Statement
1. Greater than 10 and divisible by 3
let n = 15;
if (n > 10) {
    if (n % 3 == 0) {
        console.log("Greater than 10 and divisible by 3");
    } else {
        console.log("Greater than 10 but not divisible by 3");
    }
} else {
    console.log("Not greater than 10");
}


2. Voting eligibility
let age = 20;
let voterID = true;
if (age >= 18) {
    if (voterID == true) {
        console.log("Can Vote");
    } else {
        console.log("Voter ID required");
    }
} else {
    console.log("Not eligible");
}


3. Pass and distinction
let marks = 85;
if (marks >= 40) {
    console.log("Passed");
    if (marks >= 80) {
        console.log("Passed with Distinction");
    }
} else {
    console.log("Failed");
}


4. ATM system
let pin = 1234;
let balance = 5000;
let amount = 2000;
let correctPin = 1234;

if (pin == correctPin) {
    if (balance >= amount) {
        console.log("Withdrawal Successful");
    } else {
        console.log("Insufficient Balance");
    }
} else {
    console.log("Incorrect PIN");
}


5. Leap year
let year = 2024;
if (year % 4 == 0) {
    if (year % 100 == 0) {
        if (year % 400 == 0) {
            console.log("Leap Year");
        } else {
            console.log("Not a Leap Year");
        }
    } else {
        console.log("Leap Year");
    }
} else {
    console.log("Not a Leap Year");
}


6. Email validation
let email = "student@gmail.com";
if (email.includes("@")) {
    if (email.endsWith(".com")) {
        if (email.length > 10) {
            console.log("Valid Email");
        } else {
            console.log("Email is too short");
        }
    } else {
        console.log("Email must end with .com");
    }
} else {
    console.log("Email must contain @");
}


7. Online shopping discount
let total = 2000;
let premium = true;
let discount = 0;
if (total >= 1000) {
    if (premium == true) {
        discount = total * 0.20;
    } else {
        discount = total * 0.10;
    }
}

let finalAmount = total - discount;
console.log("Final Amount:", finalAmount);


8. Positive, even and divisible by 4
let n = 16;
if (n > 0) {
    if (n % 2 == 0) {
        if (n % 4 == 0) {
            console.log("Positive Even and Divisible by 4");
        } else {
            console.log("Positive Even");
        }
    } else {
        console.log("Positive Odd");
    }
} else {
    console.log("Not Positive");
}


9. Job eligibility
let age = 25;
let degree = true;
let experience = 3;
if (age >= 21 && age <= 30) {
    if (degree == true) {
        if (experience >= 2) {
            console.log("Eligible for Interview");
        } else {
            console.log("Insufficient Experience");
        }
    } else {
        console.log("Degree Required");
    }
} else {
    console.log("Age Not Eligible");
}


10. Exam eligibility
let present = true;
let internal = 35;
let external = 40;
if (present == true) {
    if (internal >= 30) {
        if (external >= 35) {
            console.log("Eligible for Final Exam");
        } else {
            console.log("External Marks Insufficient");
        }
    } else {
        console.log("Internal Marks Insufficient");
    }
} else {
    console.log("Student is Absent");
}



E] switch Statement
1. Number of days in a month
let month = 2;
switch (month) {
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
        console.log("31 days");
        break;

    case 4:
    case 6:
    case 9:
    case 11:
        console.log("30 days");
        break;

    case 2:
        console.log("28 days");
        break;

    default:
        console.log("Invalid Month");
}


2. Vowel or consonant
let ch = "a";
switch (ch.toLowerCase()) {
    case "a":
    case "e":
    case "i":
    case "o":
    case "u":
        console.log("Vowel");
        break;

    default:
        console.log("Consonant");
}


3. Season using multiple cases
let n = 3;
switch (n) {
    case 1:
    case 2:
        console.log("Winter");
        break;

    case 3:
    case 4:
        console.log("Summer");
        break;

    default:
        console.log("Invalid Number");
}


4. Class based on marks using switch(true)
let marks = 80;
switch (true) {
    case marks >= 75:
        console.log("Distinction");
        break;

    case marks >= 60:
        console.log("1st Class");
        break;

    case marks >= 50:
        console.log("2nd Class");
        break;

    case marks >= 35:
        console.log("3rd Class");
        break;

    default:
        console.log("Failed");
}


5. Nested switch for admin and user
let role = "admin";
let action = "edit";
switch (role) {
    case "admin":
        switch (action) {
            case "create":
                console.log("Create Item");
                break;

            case "edit":
                console.log("Edit Item");
                break;

            case "delete":
                console.log("Delete Item");
                break;

            default:
                console.log("Invalid Action");
        }
        break;

    case "user":
        console.log("Limited Access");
        break;

    default:
        console.log("Invalid Role");
}


6. Predict and correct the output
Original output:
Mango is yellow
Banana is yellow
Unknown fruit


This happens because there is no break after the "mango" case, so JavaScript continues to the next cases. This is called fall-through.
Correct code:
let fruit = "mango";

switch (fruit) {
    case "apple":
        console.log("Apple is red");
        break;

    case "mango":
        console.log("Mango is yellow");
        break;

    case "banana":
        console.log("Banana is yellow");
        break;

    default:
        console.log("Unknown fruit");
}
7. Identify different values using switch
let value = "0";
switch (value) {
    case 0:
        console.log("Number Zero");
        break;

    case "0":
        console.log("String Zero");
        break;

    case false:
        console.log("Boolean False");
        break;

    case null:
        console.log("Null Value");
        break;

    case undefined:
        console.log("Undefined Value");
        break;

    default:
        console.log("Other Value");
}


Explanation: JavaScript switch uses strict comparison (===). Therefore, 0, "0", and false are different values.
8. Calculator using switch
let a = 10;
let b = 3;
let op = "**";
switch (op) {
    case "+":
        console.log(a + b);
        break;

    case "-":
        console.log(a - b);
        break;

    case "*":
        console.log(a * b);
        break;
    case "/":
        if (b == 0) {
            console.log("Cannot divide by zero");
        } else {
            console.log(a / b);
        }
        break;

    case "%":
        console.log(a % b);
        break;

    case "**":
        console.log(a ** b);
        break;

    default:
        console.log("Invalid Operator");
}


9. Beginning, middle or end of the month
let day = 15;
switch (true) {
    case day >= 1 && day <= 10:
        console.log("Beginning of the month");
        break;
    case day >= 11 && day <= 20:
        console.log("Middle of the month");
        break;
    case day >= 21 && day <= 31:
        console.log("End of the month");
        break;
    default:
        console.log("Invalid Day");
}


10. Online food ordering system
let category = "veg";
let item = "pizza";
let size = "full";
let price = 0;

switch (category) {
    case "veg":
        switch (item) {
            case "pizza":
                price = 200;
                break;

            case "burger":
                price = 100;
                break;

            default:
                console.log("Invalid Veg Item");
        }
        break;

    case "nonveg":
        switch (item) {
            case "pizza":
                price = 300;
                break;

            case "burger":
                price = 150;
                break;

            default:
                console.log("Invalid Nonveg Item");
        }
        break;

    default:
        console.log("Invalid Category");
}

if (price > 0) {
    switch (size) {
        case "half":
            price = price / 2;
            break;

        case "full":
            break;

        default:
            price = 0;
            console.log("Invalid Size");
    }
    if (price > 0) {
        console.log("Category:", category);
        console.log("Item:", item);
        console.log("Size:", size);
        console.log("Price: ₹" + price);
    }
}



F] Ternary Operator Questions
The basic format is:
condition ? valueIfTrue : valueIfFalse
1. Divisible by 7
let n = 21;

let result = n % 7 == 0
    ? "Divisible by 7"
    : "Not Divisible by 7";

console.log(result);


2. Temperature
let temperature = 32;
let result = temperature >= 30 ? "Hot Day" : "Pleasant Day";

console.log(result);


3. Check empty string
let str = "";
let result = str == "" ? "Empty String" : "String has content";

console.log(result);
4. Age classification using nested ternary
let age = 16;
let result = age < 13
    ? "Child"
    : age <= 19
    ? "Teenager"
    : "Adult";
console.log(result);


5. Greatest of three numbers
let a = 10, b = 25, c = 15;
let result = a >= b && a >= c
    ? a
    : b >= c
    ? b
    : c;
console.log(result);


6. Student marks classification
let marks = 65;
let result = marks >= 75
    ? "Distinction"
    : marks >= 60
    ? "First Class"
    : marks >= 50
    ? "Second Class"
    : marks >= 35
    ? "Pass"
    : "Fail";
console.log(result);


7. Positive/negative and even/odd
let n = -7;
let result = n == 0
    ? "Zero"
    : n > 0
    ? n % 2 == 0 ? "Positive Even" : "Positive Odd"
    : n % 2 == 0 ? "Negative Even" : "Negative Odd";

console.log(result);


8. Leap year using nested ternary
let year = 2024;
let result = year % 4 == 0
    ? year % 100 == 0
        ? year % 400 == 0 ? "Leap Year" : "Not a Leap Year"
        : "Leap Year"
    : "Not a Leap Year";

console.log(result);


9. Role and action using one nested ternary
let role = "admin";
let action = "delete";
let result = role == "admin"
    ? action == "delete"
        ? "Admin Delete"
        : action == "edit"
        ? "Admin Edit"
        : "Admin Other"
    : role == "user"
        ? action == "view"
            ? "User View"
            : "User Restricted"
        : "Invalid Role";

console.log(result);


10. Discount and final amount using one expression
let cart = 3000;
let result = {
    discount: cart >= 5000 ? 20
        : cart >= 2000 ? 10
        : cart >= 1000 ? 5
        : 0,
    payable: cart - cart * (
        cart >= 5000 ? 0.20
        : cart >= 2000 ? 0.10
        : cart >= 1000 ? 0.05
        : 0
    )
};

console.log(result);
For a cart total of ₹3,000, the result is:
discount: 10%
payable: ₹2700


