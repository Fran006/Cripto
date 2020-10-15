// ==UserScript==
// @name         Tarea3
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        file:///C:/Users/franc/OneDrive/Escritorio/a.html
// @grant        none
// @require      http://sladex.org/blowfish.js/ext/blowfish.js
// ==/UserScript==

(function() {
    'use strict';

        var a = document.getElementsByClassName("blowfish")[0].getAttribute("id");
        var b = document.getElementsByClassName("iv")[0].getAttribute("id");
        var c = document.getElementsByClassName("llave")[0].getAttribute("id");
        var objeto= [1,3];
        var des = blowfish.decrypt(a, c, objeto);
        //var des2 = des.encode(8);
        document.getElementsByClassName("Blowfish")[0].innerText = des;

})();
