# pi4-cooling
<br>simple python script to aid in cooling the new pi4.
<br>Much of the script has been borrowed from other users online to help me cobble this together.

<br>To power the 5v fan from the raspberry pi and use the GPIO to switch it on and off connect as below (lots more examples online).
<br>Im using a 40mm 2 wire 5v fan (cheapest one on ebay).
<br>I have a 2N2222A NPN Transistor connected between the 5v pin out, ground and GPIO 18 (changeable in the script).
<br>Pin (1) collector to PI GND.
<br>Pin (2) base to GPIO 18.
<br>Pin (3) Emitter to Fan ground.
<br>Fan live to GPIO live.

<img src="https://github.com/jasharrar/pi4-cooling/blob/master/fan.jpg" alt="fan" style="width:500px;height:600px;">
