import socket
import datetime
import mysql.connector

IP = "192.168.1.250"
PORT = 9000
numero_mensaje = 1
latnew=0
longnew=0
minnew=0

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((IP,PORT))

while True:
    data,addr=sock.recvfrom(1024)
    Fecha_captura = datetime.datetime.now()


    
    if len(data) == 63:
        
        data = str(data)
    
        Anio = str(Fecha_captura.year)
        Mes = str(Fecha_captura.month)
        if len(Mes) < 2:
            Mes = "0%s" % Mes
        Dia = str(Fecha_captura.day)
        if len(Dia) < 2:
            Dia = "0%s" % Dia
        
        Hora = str(Fecha_captura.hour)
        if len(Hora) < 2:
            Hora = "0%s" % Hora
        Mins = str(Fecha_captura.minute)
        minutes=float(Fecha_captura.minute)
        if len(Mins) < 2:
            Mins = "0%s" % Mins
        Secs = str(Fecha_captura.second)
        if len(Secs) < 2:
            Secs = "0%s" % Secs

   #    lat = str(float(data[19:26])/100000)
   #    titud=float(data[20:26])/100000           
        titud=float(data[20:26])/1000
        lat=str(titud)
    #   long = str(float(data[28:35])/-100000) 
    #   gtitud=float(data[28:35])/-100000
        gtitud=float(data[28:35])/1000
        long=str(gtitud)

 

        fecha_db="%s/%s/%s" %(Anio,Mes,Dia)
        hora_db="%s:%s:%s" %(Hora, Mins, Secs)
        
        db = mysql.connector.connect(user='root',password='1234',database='disenouninorte')
        cursor = db.cursor()
        if abs(titud-latnew)>0 or abs(gtitud-longnew)>0 or abs(minutes-minnew)>0 :
              cursor.execute("INSERT INTO coordenadas (Fecha,Hora,Latitud,Longitud) VALUES('%s','%s','%s','%s')" % (fecha_db,hora_db,lat,long))
              latnew=titud
              longnew=gtitud
              minnew=minutes
        db.commit()
        cursor.close()
        db.close()
        

