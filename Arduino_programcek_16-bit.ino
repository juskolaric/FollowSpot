#include <DmxSimple.h>
uint8_t dimmer, pan, panFine, tilt, tiltFine, RGB;

/*LED par 9x10W:
 * 1 - dimmer
 * 2 - Red
 * 3 - white
 * 4 - blue
 *
 *Spot 70W:
 * 1 - Pan (16-bit)
 * 2 - tilt (16-bit)
 * 3 - XY Rotating speed
 * 4 - dimmer
 */

void setup() {
  Serial.begin(115200);

  DmxSimple.usePin(2);

  DmxSimple.maxChannel(20);

  /* Set channel 1 on the light (total dimmer) to max (255)
  ** so that values for channels R (2), G (3) and B (4) are visible.*/
  DmxSimple.write(4, 11);
  DmxSimple.write(8, 0); // pika je 0, 47 je za fino nastavlanje
  DmxSimple.write(10, 96); // za fokus


}

void loop() {

  if (Serial.available()) { //ali je kaj v bufferju od serial1
    String input = Serial.readStringUntil('!');
    dimmer = input.substring(0, 3).toInt();
    pan = input.substring(3, 6).toInt();
    panFine = input.substring(6, 9).toInt();
    tilt = input.substring(9, 12).toInt();
    tiltFine = input.substring(12, 15).toInt();
    RGB = input.substring(15, 18).toInt();//dodal
  }
  DmxSimple.write(4, dimmer);
  DmxSimple.write(1, pan); // normal
  DmxSimple.write(2, tilt);
  DmxSimple.write(12, panFine); //fine
  DmxSimple.write(13, tiltFine);
  DmxSimple.write(6, RGB); //dodal
  
  /*Serial.print(dimmer);
  Serial.print(" ");
  Serial.print(pan);
  Serial.print(" ");
  Serial.print(tilt);
  Serial.println(" ");

  DmxSimple.write(1, 255);
    DmxSimple.write(2, 255);
    delay(1000);
    DmxSimple.write(2, 0);
    DmxSimple.write(3, 255);
    delay(1000);
    DmxSimple.write(3, 0);
    DmxSimple.write(4, 255);
    delay(1000);
    DmxSimple.write(4, 0);
  */
}

