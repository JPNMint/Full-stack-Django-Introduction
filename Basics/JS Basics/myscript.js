first_name = prompt("Your first name?")
last_name = prompt("Your last name?")

age = prompt("Your age?")
height = prompt("Your body height?")
pet = prompt("Your pet's name?")


if (first_name[0]==last_name[0] && (age>20 && age<30) && height>169 && pet.slice(-1)=='y'){
    alert("You are a spy!")
}