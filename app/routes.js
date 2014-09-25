//ROUTES
//load the schema
var Data = require('./models/movie_model');

module.exports = function(app){
	
	
	//API for collecting movies
	//Maby return somthing more than just the movie name
	app.get('/api/get_movie',function(req,res){

		Data.random(function(err,movie){
			if (err)
				res.send(err);
			return res.send({"movie": movie.movieName})
		});

		
	});

	// application -------------------------------------------------------------
	app.get('*', function(req, res) {
		res.sendfile('./public/index.html'); // load the single view file (angular will handle the page changes on the front-end)
	});



	
}