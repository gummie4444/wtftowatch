//SCHEMA for the drugs document


var mongoose = require('mongoose');


var movieSchema = new mongoose.Schema({
	movieName:String,
	genre: Array,
	rating: Number,
	votes: Number
})


movieSchema.statics.random = function(callback) {
		  this.count(function(err, count) {
		    if (err) {
		      return callback(err);
		    }
		    var rand = Math.floor(Math.random() * count);
		    this.findOne().skip(rand).exec(callback);
		  }.bind(this));
		};

module.exports = mongoose.model("Data",movieSchema);