$(document).ready(function(){

  // var req_url   = 'https://api.github.com/users/serrato1';
  //
  // $.ajax({
  //   url: req_url,
  //   dataType: "jsonp",
  //   success: function(json_data) {
  //     // alert(json_data.data.login);
  //     console.log('json data from api: ', json_data.data);
  //     $("#user-img").attr("src",""+json_data.data.avatar_url);
  //     $("#name").append(json_data.data.name);
  //     $("#url").append(json_data.data.html_url);
  //     $("#location").append(json_data.data.location);
  //     $("#graph").attr("src","images/commit-01.png");
  //     console.log(json_data);
  //   }
  // });


  var list_people = [["Noel Serrato","https://api.github.com/users/serrato1","images/commit-01.png"],["David","https://api.github.com/users/wratchetwrench","images/commit-02.png"],["Rahul","https://api.github.com/users/rahul4times","images/commit-02.png"],["Noel Serrato","https://api.github.com/users/chrisb01","images/commit-01.png"]];
  for (i = 0; i<= list_people.length -1 ; i++){
    var person  = list_people[i][0];
    var url = list_people[i][1]
    var graph     = list_people[i][2];
    var block = "<h2 id=\"name\">"+person+"</h2> <a id='user-url' href=\""+url+"\""+">"+url+"</a><img id=\"graph\" src=\""+graph+"\"/>";
    $(".main").append(block);
  }
  // var git_person_1 = new User("Noel","this is my bio");

  var tags = ["100daysofcode", "python", "java", "LA", "pycon2018", "dockercon2018"] ;

  for (i = 0; i <= tags.length - 1 ; i++){
    var block=    '<div class="menuitem"><a href="#">'+tags[i]+'</a></div>';
    $(".menu").append(block);
  }
})


//
