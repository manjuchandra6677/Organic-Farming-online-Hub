function validpassword(){
      var password=document.password.pass1.value;
      var cpassword=document.password.pass2.value;

           if(password.length<8){
           alert("please enter atleast 5  characters");
           return false;
           }
                if(password==cpassword){
                return true;}
                else{
				alert("password & confirm password must be same");
                return false;
                }


}