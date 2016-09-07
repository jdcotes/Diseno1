			
var intevalo1;
var entro=0;
 var map2;
   var Tabla_MySql;
 //intevalo1 = setInterval('mapa1()',11000);
 intevalo1 = setInterval(function(){mapa1()},5000);
        // mapa1();
var markerArray =[],total=0;
var routes2=[];
 function mapa1(){
     
     $.post("server/vivo.php",function(respuesta) {
     	/*bueno para que accedan a cada una de las filas de las tablas es así:*/
Tabla_MySql = JSON.parse(respuesta);


     	// console.log(Tabla_MySql[0].Fecha);
     	// console.log(Tabla_MySql[0].Hora);
     	// console.log(Tabla_MySql[0].Latitud);
     	// console.log(Tabla_MySql[0].Longitud);

         var prueba1 = JSON.parse(respuesta);
         var lat, lon;
          for (var j in prueba1) {
              var myLatLng = {lat: parseFloat(prueba1[j].Latitud), lng: parseFloat(prueba1[j].Longitud)};
              lat=parseFloat(prueba1[j].Latitud);
              lon= parseFloat(prueba1[j].Longitud);
             }
           if(entro==0)
           {
            map2 = new google.maps.Map(document.getElementById('map'), {
           zoom: 15,
           center: myLatLng
            });
            entro=1;
          
           }
           routes2[total] =  new google.maps.LatLng(lat,lon);
           total=total+1;
           var polyline = new google.maps.Polyline({
            path: routes2
            , map: map2
            , strokeColor: '#ff0000'
            , strokeWeight: 5
            , strokeOpacity: 0.3
            , clickable: false
          });
            var marker = new google.maps.Marker({
            position: myLatLng,
            map: map2,
            title: 'You are here'
          });
           
           for (var i = 0; i < markerArray.length; i++) {
             markerArray[i].setMap(null);
           };
          markerArray= [];
          markerArray.push(marker );
      
       });
  }