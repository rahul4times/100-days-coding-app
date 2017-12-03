$(document).ready(function(){
  // function User(usr_name,usr_bio){
  //   this.usr_name = usr_name;
  //   this.bio =  usr_bio;
  // }
  var req_url   = 'https://api.github.com/users/serrato1';

  $.ajax({
    url: req_url,
    dataType: "jsonp",
    success: function(json_data) {
      // alert(json_data.data.login);
      $("#user-img").attr("src",""+json_data.data.avatar_url);
    }
  });


  var list_people = [["repo 1","this is the brief overview for repo 1"],["repo 2","this is a description for repo 2"]];
  for (i = 0; i<= list_people.length -1 ; i++){
    var person  = list_people[i][0];
    var bio     = list_people[i][1];
    var block = "<h2>"+person+"</h2> <p>"+bio+"</p>";
    $(".main").append(block);
  }
  var git_person_1 = new User("Noel","this is my bio");
})


//
