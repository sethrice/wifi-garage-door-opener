import socket
import machine
import webrepl
import time

webrepl.start()

#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head> <title>ESP8266 Garage Door  </title> </head>
<center><h2>Garage Door Opener</h2></center>
<form>
GD0:
<button name="Garage Toggle" value="OFF0" type="submit">Open Garage Door</button><br><br>
</form>
</html>
"""

#Setup PINS
GD0 = machine.Pin(5, machine.Pin.OUT)

#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
while True:
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)
    GDOFF0 = request.find('/?GD=OFF0')
    if GDOFF0 == 6:
        print('TURN GD0 OFF')
        GD0.value(not GD0.value()) # toggle
        time.sleep(1)
    response = html
    conn.send(response)
    conn.close()
