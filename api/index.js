var express = require('express');
var bodyParser = require("body-parser");
var cors = require('cors');
var process = require('process');
var fs = require('fs');

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
    'bell': true,
};

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(cors());

app.get('/action', function (req, res) {
    console.log("Hande GET on route: " + req.path)
    res.send(action);
});

app.get('/ui/actions', function (req, res) {
    res.writeHeader(200, {"Content-Type": "text/html"});
    res.write(fs.readFileSync(__dirname + '/../web/actions.html'));
    res.end();
});

app.get('/ui/colors', function (req, res) {
    res.writeHeader(200, {"Content-Type": "text/html"});
    res.write(fs.readFileSync(__dirname + '/../web/colors.html'));
    res.end();
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
