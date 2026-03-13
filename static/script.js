async function sendMessage(){

let input=document.getElementById("userInput");

let message=input.value;

if(message==="") return;

let chatbox=document.getElementById("chatbox");

chatbox.innerHTML+=`<div class="user">${message}</div>`;

let response=await fetch("/chat",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({message:message})

});

let data=await response.json();

chatbox.innerHTML+=`<div class="bot">${data.reply}</div>`;

input.value="";

chatbox.scrollTop=chatbox.scrollHeight;

}