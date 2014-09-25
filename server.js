//SET UPP

var express = require ('express');
var app  = express();
var port = process.env.Port || 8080;
var mongoose = require('mongoose'); 					// mongoose for mongodb

app.set('title', 'WTFTOWATCH');


mongoose.connect('mongodb://gummi:gummi@ds039850.mongolab.com:39850/movies'); 	// connect to mongoDB database TODO CREATE A OWN DB FROM THE OWN SERVER

app.configure(function() {
	app.use(express.static(__dirname + '/public')); 		// set the static files location /public/img will be /img for users
	app.use(express.logger('dev')); 						// log every request to the console
	app.use(express.bodyParser()); 							// pull information from html in POST
	app.use(express.methodOverride()); 						// simulate DELETE and PUT
});

// routes ======================================================================
require('./app/routes.js')(app);


// listen (start app with node server.js) ======================================
app.listen(port);
console.log("App listening on port " + port);