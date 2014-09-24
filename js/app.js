var app = angular.module( 'myApp', ['MainController','photoService','autoCompletedir'] );

app.config(function($httpProvider){
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
});
