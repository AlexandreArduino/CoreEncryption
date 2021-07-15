#include "328p.h"
#include "Arduino.h"

void _serial_init(void)
{
    Serial.begin(BAUDRATE);
}