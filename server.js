'use strict';

const PORT = 3000;

// The variable stocks has the same value as the variable stocks in the file 'stocks.js'
const stocks = require('./stocks.js').stocks;

const express = require("express");
const app = express();


app.use(express.urlencoded({
    extended: true
}));

app.use(express.static('public'));
// Note: Don't add or change anything above this line.

// Add your code here

function findStockBySymbol(stockSymbol) {
    for (const stock in stocks){
        if(stocks[stock].symbol === stockSymbol){
            return (stocks[stock]);
        }    
    }
}

function findStockByPrice(lowestorHighest) {
    let value = stocks[0].price;
    let object = stocks[0]
    if(lowestorHighest === "lowest"){
        for (const stock in stocks){
            if(stocks[stock].price < value){
                value = stocks[stock].price
                object = stocks[stock]
            }
        }
        return object; 
    }
    else if (lowestorHighest === "highest") {
        for (const stock in stocks){
            if(stocks[stock].price > value){
                value = stocks[stock].price
                object = stocks[stock]
            }
        }
        return object;
    }
    
}

app.get("/stockorder", (req, res) => {
    const ans = (findStockBySymbol(req.query.stockdropdown))
    const amount = req.query.quantity
    const company = ans.company
    const price = ans.price
    const total = price * amount
    const stringAnswer = `You placed an order to buy ${amount} stocks of ${company}. The price of one stock is $${price} and the total price for this order is $${total}.`
    res.send(stringAnswer)
})

app.get("/stocksearch", (req, res) => {
    const choice = req.query.type
    const output = findStockByPrice(choice)
    res.send(output)
})

// Note: Don't add or change anything below this line.
app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}...`);
});