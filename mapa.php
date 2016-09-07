<?php 
  
  if(!($iden = mysql_connect("localhost", "root", ""))) 
    die("Error: No se pudo conectar");
  
  
  if(!mysql_sele_db("disenouninorte", $iden)) 
    die("Error: No existe la base de datos");
 
  $sentencia = "SELECT * FROM prueba"; 
  
  $resultado = mysql_query($sentencia, $iden); 
  if(!$resultado) 
    die("Error: no se pudo realizar la consulta");
  
  $rawdata=array();
  $i=0; 
  while($fila = mysql_fetch_assoc($resultado)) 
  { 
  $rawdata($i)=$fila;
  $i++;

  } 
    
 mysql_free_result($resultado);
 mysql_close($iden); 
 echo json_encode($rawdata)
?> 