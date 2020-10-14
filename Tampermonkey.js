// ==UserScript==
// @name         Patatas
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       YO
// @match        file:///C:/Users/franc/OneDrive/Escritorio/a.html
// @grant        none
// @require      https://www.npmjs.com/package/blowfishx
// ==/UserScript==


(function() {
    'use strict';
   var key = "patata";
   var a = document.getElementsByClassName("Blowfish")[0].getAttribute("id");
   var bf = new Blowfish();
   var iv = "mensajee";
   var password="pata";
   var enc = blowfish.decrypt(a, password, { outputType: 3, cipherMode: 1 });
   document.getElementsByClassName("Blowfish")[0].innerText = enc;

})();
