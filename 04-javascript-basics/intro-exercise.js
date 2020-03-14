var pounds = prompt("Metric Converter\n\nEnter a figure in pounds:")
var kilos = pounds * 0.454
kilos = kilos.toFixed(1)
alert(pounds + " pounds converts to " + kilos + " kilos.")
console.log("Conversion completed.")