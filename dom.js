// DOM

// document object model
// use it to manipulate content, style, structure
// is one of the most unique and useful tools of javascript

// methods of selecting elements


/*

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>master dom</title>
  </head>
  <body>
    <div class="container">
      <h1 id="main-heading">Favorite movie franchise</h1>
      <ul>
        <li class="list-item">The matrix</li>
        <li class="list-item">Star Wars</li>
        <li class="list-item">Harry Potter</li>
        <li class="list-item">Lord of Ring</li>
        <li class="list-item">Marvel</li>
      </ul>
    </div>
    <script src="./index.js"></script>
  </body>
</html>

 */


// GetElementById

const title = document.getElementById("main-heading");
console.log(title);


// GetElementByClassName

const listItem =  document.GetElementsByClassName('list-item');
console.log(listItem);


// GetElementByTagName
// here li stands for list tag 

const listItemTag =  document.GetElementsByTagName('li');
console.log(listItemTag);


// querySelector

const container = document.querySelector('div');
console.log(container);


// querySelectorAll

const containerAll = document.querySelectorAll('div');
console.log(containerAll);


