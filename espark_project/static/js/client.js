$(document).ready(function(){
  var options = {  
    success: function(responseData) { 
      if(responseData.notCsv) {
        alert("Please make sure your file is a CSV")
      } else {
        $('#tablecontainer').html(responseData.myhtml)
      }
    },
    beforeSubmit: function(arr, $form, options){ 
      if($('.domainorder').val() === "" || $('.studenttests').val() === ""){
        alert("You need coffee. Please upload your CSV.")
        return false;
      }
    },
    dataType: 'json'
  }; 

  $('.form').ajaxForm(options);

})
