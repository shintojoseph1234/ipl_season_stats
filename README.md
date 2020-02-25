# ipl_season_stats



<!DOCTYPE html>
<html lang="en-us">
<head>
   
   <meta charset="utf-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0"/>
   <title>OneConsole</title>
   <link href="/static/images/icons/favicon.ico" rel="shortcut icon">
   
<link href="/static/material/fonts/material-design-icons/material-icons.css"  rel="stylesheet">
<link href="/static/material/fonts/roboto/style.css" rel="stylesheet">
<link href="/static/material/css/materialize.frontend.min.css" rel="stylesheet">
<link href="/static/material/css/materialize.frontend.print.min.css" rel="stylesheet" media="print">
<link href="/static/material/css/materialize.css" rel="stylesheet">
<link href="/static/material/css/materialize.forms.css" rel="stylesheet">
<link href="/static/material/css/materialize.frontend.css" rel="stylesheet">
<link href="/static/material/css/materialize.frontend.print.css" rel="stylesheet" media="print">
<link href="/static/material/css/jquery.datetimepicker.css" rel="stylesheet">
<link href="/static/material/css/responsive.dataTables.css" rel="stylesheet">
<link href="/static/material/css/fixedHeader.dataTables.css" rel="stylesheet">
<link href="/static/material/css/perfect-scrollbar.css" rel="stylesheet">

<link href="https://cdnjs.cloudflare.com/ajax/libs/material-design-lite/1.1.0/material.min.css" rel="stylesheet">
<link href="https://cdn.datatables.net/1.10.20/css/dataTables.material.min.css" rel="stylesheet">

   
<script src="/static/material/js/materialize.frontend.min.js"></script>
<script src="/static/material/js/custom-elements.min.js"></script>
<!-- <script src="/static/material/js/materialize.components.js"></script> -->
<script src="/static/material/js/turbolinks.js"></script>
<script src="/static/material/js/jquery.js"></script>
<script src="/static/material/js/jquery.dataTables.js"></script>
<script src="/static/material/js/jquery.activeNavigation.js"></script>
<script src="/static/material/js/jquery.datetimepicker.full.js"></script>
<script src="/static/material/js/jquery.formset.js"></script>
<script src="/static/material/js/perfect-scrollbar.jquery.js"></script>
<script src="/static/material/js/dataTables.fixedHeader.js"></script>
<script src="/static/material/js/dataTables.responsive.js"></script>
<script src="/static/material/js/materialize.js"></script>

<script src="https://cdn.datatables.net/1.10.20/js/dataTables.material.min.js"></script>

   
   
   <style>
      select {
      display: inline !important;
      }
      #logoutBtn{
      line-height: 50px !important;
      }
      td{
      padding : 0px 0px 0px 0px !important;
      font-size: 12px !important;
      }
      th{
      font-size: 12px !important;
      }
      /* Popup container - can be anything you want */
      .popup {
      position: relative;
      display: inline-block;
      cursor: pointer;
      -webkit-user-select: none;
      -moz-user-select: none;
      -ms-user-select: none;
      user-select: none;
      float: right;
      right: 290px;
      top: 15px;
      }
      /* The actual popup */
      .popuptext {
      visibility: hidden;
      width: 361px;
      background-color: #61d632;
      color: #fff;
      padding: 8px 8px;
      position: absolute;
      z-index: 1;
      bottom: 125%;
      left: 50%;
      margin-left: -80px;
      font-weight: bold;
      }
      /* Toggle this class - hide and show the popup */
      .popup .show {
      visibility: visible;
      -webkit-animation: fadeIn 1s;
      animation: fadeIn 1s;
      }
      .popup .hide {
      visibility: hidden;
      -webkit-animation: fadeIn 1s;
      animation: fadeIn 1s;
      }
      /* Add animation (fade in the popup) */
      @-webkit-keyframes fadeIn {
      from {opacity: 0;}
      to {opacity: 1;}
      }
      @keyframes fadeIn {
      from {opacity: 0;}
      to {opacity:1 ;}
      }
   </style>
   <script>
      $(document).ready(function(){
      $('.collapsible').collapsible();
      });
   </script>
</head>
<body class="with-sidebar">
   <dmc-turbolinks/>
   
   <header>
      
      <dmc-sidenav>
         <ul id="slide-out" class="sidenav sidenav-fixed">
            
            <li>
               <div class="user-view">
                  <div class="background" >
                     <img src="/static/material/imgs/sidenav.svg">
                  </div>
                  
                  
                  <a href="#"><img class="circle" src="/static/material/imgs/user.png"></a>
                  
                  
                  <a href="#"><span class="white-text name">Mallikarjunappa</span></a>
                  <a href="#"><span class="white-text email">vikas-patel.mallikarjunappa@socgen.com</span></a>
               </div>
            </li>
            
            
            <ul class="collapsible">
               <li>
                  <div class="collapsible-header"><i class="material-icons">people</i>MANAGEMENT</div>
                  <div class="collapsible-body">
                     <ul>
                        <li><a href="/management/active_sessions">Active Users</a></li>
                        <li><a href="/management/mail_logs">Mail Logs</a></li>
                     </ul>
                  </div>
               </li>
            </ul>
            <!-- back to home -->
            <li>
              <a href="/" class="collapsible-header" data-turbolinks="false">Back to home
                <i class="material-icons">home</i>
              </a>
            </li>
            
         </ul>
      </dmc-sidenav>
      
   </header>
   <main>
      
      
      <nav class="topbar">
         <div class="nav-wrapper">
            <dmc-sidenav-trigger><a href="#" data-target="slide-out" class="sidenav-trigger"><i class="material-icons">menu</i></a></dmc-sidenav-trigger>
            <div class="brand-logo">
               Management
            </div>
            <ul id="nav-mobile" class="right hide-on-med-and-down">
               
               
               <li><a id="logoutBtn" href="/logout" data-turbolinks="false"><i class="material-icons right">exit_to_app</i>Log out</a></li>
               
               
            </ul>
         </div>
      </nav>
      
      
      <nav class="breadcrumbs">
         <div class="nav-wrapper">
            
<a href="/">Home</a>
<a href="/apps/all">Applications</a>
<a href="" class="active">Management</a>

         </div>
      </nav>
      
      
      <div class="popup" >
         <span class="popuptext" id="myPopup">A Simple Popup!</span>
      </div>
      <div class="content">
         
<div class="left-panel wide">
   <div class="card">
      <div class="card-content" >
        <div class="card-title">Mail Logs</div>
          <div style="overflow:auto;width:100%;height:100%;" class="container">
             
        </div>
    </div>
   </div>
</div>
<script type="text/javascript">

   $(document).ready(function() {

     setTimeout(function(){
       var popup = document.getElementById("myPopup");
      popup.innerHTML = "";
        popup.innerHTML = "Loaded successfully";
        popup.classList.toggle("show");
      setTimeout(function(){
        document.getElementById("myPopup").classList.toggle("hide");
      },5000);

      },1000);


       $('#table').DataTable({
         pageLength: 20,
         
         // fixedHeader: true,
         // scrollX: true,
         columnDefs: [
               {
                   destroy:true,
                   targets: [ 0, 1, 2 ],
                   className: 'mdl-data-table__cell--non-numeric'
               }
           ]
       });
   });
</script>

<div class="fixed-action-btn">
   <a class="btn-floating btn-large waves-effect waves-light red z-depth-2" onClick="javascript:history.go(-1);">
      <i class="large material-icons">keyboard_backspace</i>
   </a>
</div>


      </div>
      
      
   </main>
   <footer>
      
   </footer>
   
   
   <dmc-snackbar>
      
   </dmc-snackbar>
   
</body>
</html>
