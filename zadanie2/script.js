let deposit = 0
let dochod = 0
let podatek = (19 + 1.5)/100
let dochod_dzienny = 0;
function oblicz() 
{
  deposit = parseFloat(document.getElementById('x').value)
  dochod = deposit*(4.5/100)
  dochod_dzienny = dochod/365
  dochod_dzienny -= dochod_dzienny*podatek
  dochod -= dochod*podatek
  document.getElementById('y').innerHTML = 'Roczny dochód: ' + Math.round(dochod) + '&nbsp;Dzienny dochód: ' + Math.round(dochod_dzienny)
}