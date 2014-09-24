angular.module('MainController',[])

.controller('MainCtrl', function($scope,photoService) {

	//get the things from the services

/*
$scope.mainLoading = true

    photoService.getAllFiles()
        .success(function(data)
        {
            console.log(typeof(data))



            $scope.mainLoading = false

        });

*/
    //vars
    
	$scope.genres = ['Short','Drama','Comedy','Documentary','Adult','Action','Romance','Thriller','Animation','Family','Crime','Horror','Music','Adventure','Fantasy','Sci-Fi','Mystery','Sport','Musical','Western','War','Reality-TV','News','Talk-Show','Game-Show','Film-Noir','Lifestyle','Experimental','Erotica','Commercial']
    $scope.tempMovies = {'Stolen (2012)': {'genre': ['Action', 'Crime', 'Drama', 'Thriller'], 'rating': ['5.5'], 'votes': ['30275']}, 'Tremors (1990)': {'genre': ['Comedy', 'Horror', 'Sci-Fi'], 'rating': ['7.2'], 'votes': ['72190']}, 'Prick Up Your Ears (1987)': {'genre': ['Drama'], 'rating': ['7.3'], 'votes': ['3723']}, 'Celebrity Deathmatch (1998)': {'genre': ['Action', 'Animation', 'Comedy', 'Sport'], 'rating': ['6.9'], 'votes': ['5034']}, 'Northfork (2003)': {'genre': ['Drama', 'Fantasy'], 'rating': ['6.4'], 'votes': ['4711']}, 'Stripes (1981)': {'genre': ['Comedy', 'War'], 'rating': ['6.9'], 'votes': ['38010']}, 'The Amityville Horror (2005)': {'genre': ['Horror'], 'rating': ['6.0'], 'votes': ['66441']}, 'The Thin Man (1934)': {'genre': ['Comedy', 'Crime', 'Mystery'], 'rating': ['8.2'], 'votes': ['17948']}, 'Kokuriko-zaka kara (2011)': {'genre': ['Animation', 'Drama', 'Family', 'Romance'], 'rating': ['7.4'], 'votes': ['11724']}, 'The Pirates! In an Adventure with Scientists! (2012)': {'genre': ['Adventure', 'Adventure'], 'rating': ['6.7'], 'votes': ['32298']}, 'The Visitor (2007/I)': {'genre': ['Crime', 'Drama', 'Music', 'Romance'], 'rating': ['7.7'], 'votes': ['33683']}, 'Gwai wik (2006)': {'genre': ['Fantasy', 'Horror', 'Mystery', 'Thriller'], 'rating': ['6.2'], 'votes': ['3882']}, 'This Is England (2006)': {'genre': ['Crime', 'Drama'], 'rating': ['7.7'], 'votes': ['87173']}, 'The Eagle Has Landed (1976)': {'genre': ['Adventure', 'Drama', 'Thriller', 'War'], 'rating': ['6.9'], 'votes': ['11875']}, 'Drake & Josh (2004)': {'genre': ['Comedy', 'Family'], 'rating': ['7.5'], 'votes': ['20407']}, 'Malcolm in the Middle (2000)': {'genre': ['Comedy'], 'rating': ['8.0'], 'votes': ['73696']}, 'Police Academy (1984)': {'genre': ['Comedy', 'Crime'], 'rating': ['6.6'], 'votes': ['72642']}, 'Jack Ryan: Shadow Recruit (2014)': {'genre': ['Action', 'Mystery', 'Thriller'], 'rating': ['6.2'], 'votes': ['62315']}, 'A Single Shot (2013)': {'genre': ['Crime', 'Drama', 'Thriller'], 'rating': ['5.8'], 'votes': ['5358']}, 'Live! (2007)': {'genre': ['Drama'], 'rating': ['5.8'], 'votes': ['4053']}, 'The Inbetweeners 2 (2014)': {'genre': ['Comedy'], 'rating': ['6.9'], 'votes': ['12673']}, 'The January Man (1989)': {'genre': ['Action', 'Crime', 'Mystery', 'Thriller'], 'rating': ['5.5'], 'votes': ['4574']}, 'All in the Family (1971)': {'genre': ['Family'], 'rating': ['8.5'], 'votes': ['6660']}, 'The In-Laws (1979)': {'genre': ['Action', 'Adventure', 'Comedy', 'Crime', 'Thriller'], 'rating': ['7.4'], 'votes': ['4766']}, 'Helix (2014)': {'genre': ['Sci-Fi', 'Thriller'], 'rating': ['7.0'], 'votes': ['12840']}, 'Naruto (2002)': {'genre': ['Action', 'Adventure', 'Animation', 'Comedy', 'Fantasy', 'Thriller'], 'rating': ['7.9'], 'votes': ['28200']}, 'The Rainmaker (1997)': {'genre': ['Crime', 'Drama', 'Thriller'], 'rating': ['7.1'], 'votes': ['38391']}, 'Deadly Friend (1986)': {'genre': ['Drama', 'Horror', 'Mystery', 'Sci-Fi'], 'rating': ['5.4'], 'votes': ['4110']}, 'Foxfire (1996)': {'genre': ['Drama'], 'rating': ['6.1'], 'votes': ['6116']}, 'Jjakpae (2006)': {'genre': ['Action', 'Crime', 'Drama'], 'rating': ['6.8'], 'votes': ['3184']}, 'The Words (2012)': {'genre': ['Drama', 'Mystery', 'Romance'], 'rating': ['7.1'], 'votes': ['47678']}}
    $scope.currentGenre = ""
    $scope.movieTitle = ""
    
    //loaders
    $scope.mainLoading = false
    $scope.Photoloading = false;
    $scope.clicked = false
    
    $scope.moviePhoto = ""
    var dataList = []
    var yearTitleList = []

    $scope.findMovie = function(){

        //Get the movies
        //TODO MAKE A API CALL
        //var obj = JSON.parse(data);

         dataList = fetch_random($scope.tempMovies)
         yearTitleList = getYearTitle(dataList[0])
         $scope.movieTitle = yearTitleList[0]
         $scope.Photoloading = true;
         $scope.clicked = true
        
        photoService.getPhoto(yearTitleList[0],yearTitleList[1]).success(function(data){

        $scope.moviePhoto=data.Poster
        $scope.Photoloading = false;
        });
    }

    //Length of a object
    function lengthObj(obj) {
        var size = 0, key;
        for (key in obj) {
            if (obj.hasOwnProperty(key)) size++;
        }
        return size;
    };

    //Get the year and the title from the movie
    //sjitmix
    function getYearTitle(movie){
        var title = ""
        var year = ""
         for (var i=0;i< dataList[0].length;i++){

            if (dataList[0][i] == '('){
                if (!isNaN(dataList[0][i+1]) && !isNaN(dataList[0][i+2]) && !isNaN(dataList[0][i+3]) && !isNaN(dataList[0][i+4])) {

                title = dataList[0].substring(0,i-1)
                year = dataList[0].substring(i+1,i+5)
                return [title,year]
                }
            }
                
         }

    }

    //fetch a random key from a object
    //return the object and the key
    function fetch_random(obj) {
        var temp_key, keys = [];
        for(temp_key in obj) {
           if(obj.hasOwnProperty(temp_key)) {
               keys.push(temp_key);
           }
        }
        var randomMovie = keys[Math.floor(Math.random() * keys.length)];

        return [randomMovie,obj[randomMovie]];
}


});