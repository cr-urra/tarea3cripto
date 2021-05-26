// ==UserScript==
// @name         T3 Script Cripto
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Descifrador de TripleDES OFB
// @author       Cristóbal Urra B.
// @match        http://localhost/*
// @icon         https://www.google.com/s2/favicons?domain=reddit.com
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/crypto-js.min.js
// @grant        none
// ==/UserScript==

(function decryptTripleDES() {
    'use strict'
    var html = document.getElementsByClassName("3DES");
    var html2 = document.getElementsByClassName("iv");
    var html3 = document.getElementsByClassName("key");
    var ciphertext = html[0].id;
    var key = html3[0].id;
    var iv = html2[0].id;
    var hexK = CryptoJS.enc.Hex.parse(key);
    var hexI = CryptoJS.enc.Hex.parse(iv);
    var cipher = CryptoJS.lib.CipherParams.create({
            ciphertext: CryptoJS.enc.Base64.parse(ciphertext)
        });
    var decrypted = CryptoJS.TripleDES.decrypt(cipher, hexK, {
      iv: hexI,
      mode: CryptoJS.mode.OFB,
      padding: CryptoJS.pad.ZeroPadding
    });
    alert(decrypted.toString(CryptoJS.enc.Utf8))
})();