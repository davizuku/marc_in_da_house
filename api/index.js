var express = require('express');
var bodyParser = require("body-parser");
var cors = require('cors');
var process = require('process');

if (process.argv.length < 3) {
    console.log('Usage: node index.js <port>');
    process.exit()
}

var port = process.argv[2]

var app = express();

var action = 'none';

var VALID_ACTIONS = {
    'none': true,
    'forward': true,
    'backward': true,
    'right': true,
    'left': true,
};

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(cors());

app.get('/action', function (req, res) {
    console.log("Hande GET on route: " + req.path)
    res.send(action);
});

app.post('/action', function (req, res) {
    console.log("Hande POST on route: " + req.path)
    if (req.body.action in VALID_ACTIONS) {
        action = req.body.action;
    } else {
        console.log('Invalid action: ', req.body);
    }
    res.send();
});

app.listen(port, function () {
    console.log('node-http Server listening on port ' + port);
});
