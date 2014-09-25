angular.module('photoService',[])

.factory('photoService', function($http) {

   return {
        getPhoto: function(title,year) {
             //return the promise directly.
             console.log(title + " " + year)
             return $http.get('http://www.omdbapi.com/?t='+title+'&y='+year)     
        },
        getAllFiles: function(){
             return $http.get('movies.json')
           },
        getMovies: function(){
             return $http.get('/api/get_movie')
           }
      };
    })