console.log("working");
if (localStorage.getItem('cart')== null) {
  var cart={}
}
else{
  cart = JSON.parse(localStorage.getItem('cart'))    // load the cart
  document.getElementById('cart').innerHTML=Object.keys(cart).length
  updateCart(cart)
}
$('.cart').click(function(){
console.log('clicked');
var idstr=this.id.toString()
console.log(idstr);
if (cart[idstr] !=undefined){
cart[idstr] = cart[idstr] + 1;
}
else
{
cart[idstr] = 1;
}
updateCart(cart)
console.log(cart);
});

function updateCart(cart) {
    for (var item in cart) {
        document.getElementById('div' + item).innerHTML = "<button id='minus" + item + "' class='btn btn-primary minus'>-</button> <span id='val" + item + "''>" + cart[item] + "</span> <button id='plus" + item + "' class='btn btn-primary plus'> + </button>";
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cart').innerHTML = Object.keys(cart).length;
    console.log(cart);
}
function updatepopcart(cart) {
  var popStr=""
  var i=1
  popStr=popStr+"<h5>Cart</h5>"
  for(var item in cart){
    popStr=popStr+"<b>"+i+"</b>"
    popStr=popStr+document.getElementById('name'+item) +"Qty:"+cart[item]+"<br>"
    i=i+1
  }

}

// If plus or minus button is clicked, change the cart as well as the display value
$('.divpr').on("click", "button.minus", function() {
    a = this.id.slice(7, );
    cart['pr' + a] = cart['pr' + a] - 1;
    cart['pr' + a] = Math.max(0, cart['pr' + a]);
    document.getElementById('valpr' + a).innerHTML = cart['pr' + a];
    updateCart(cart);
});
$('.divpr').on("click", "button.plus", function() {
    a = this.id.slice(6, );
    cart['pr' + a] = cart['pr' + a] + 1;
    document.getElementById('valpr' + a).innerHTML = cart['pr' + a];
    updateCart(cart);
});
