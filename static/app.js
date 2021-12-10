window.addEventListener('load', async (event) => {
  // Get all cupcakes from api 
  let cupcakeResponse = await axios.get('http://localhost:5000/api/cupcakes');
  
  // Select cupcake list 
  cupcakeList = document.getElementById("cupcake-list");
  
  // Iterate through cupcake Response data and append to list 
  for (cupcake in cupcakeResponse.data.cupcakes) {
    // Create a li 
    let tempListElement = document.createElement("li");
  
    // Get cupcake info from response data  
    let flavor = cupcakeResponse.data.cupcakes[cupcake].flavor;
    let image = cupcakeResponse.data.cupcakes[cupcake].image;
    let size = cupcakeResponse.data.cupcakes[cupcake].size;
    
    // flavor heading 
    let flavorHeading = document.createElement("h3");
    flavorHeading.innerText = flavor;
    
    // Size heading 
    let sizeHeading = document.createElement("p");
    sizeHeading.innerText = size;
    
    // Image element 
    let imageElement = document.createElement("img");
    imageElement.setAttribute('src', image);
    imageElement.setAttribute('height', 300);
    imageElement.setAttribute('width', 300);
    imageElement.classList.add("img-thumbnail");
    
    // Append all elements to li element 
    tempListElement.appendChild(flavorHeading);
    tempListElement.appendChild(sizeHeading);
    tempListElement.appendChild(imageElement);
    
    // Append li element to ul
    cupcakeList.appendChild(tempListElement);
  }
});

// Handle Form Submits 
let addForm = document.getElementById("cupcake-add-form");
addForm.addEventListener('submit', async (event) => {
  // Prevent the default page reload 
  event.preventDefault();
  
  // Serialize data & create object 
  let flavor = event.target.flavor.value;
  let size = event.target.size.value;
  let rating = event.target.rating.value;
  let image = event.target.image.value;
  
  let cupcake = {
    "flavor": flavor,
    "size": size,
    "rating": rating,
    "image": image
  };
  
  let response = await axios.post('http://localhost:5000/api/cupcakes', cupcake);
  console.log(response);
  
  
});

















