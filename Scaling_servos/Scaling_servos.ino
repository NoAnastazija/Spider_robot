/************************************************************************************************************************************************************************                                              
 * - Author               : BELKHIR Mohamed                        *                                               
 * - Profession           : (Electrical Ingineer) MEGA DAS owner   *                                                                                              
 * - Main purpose         : Industrial Application                 *                                                                                 
 * - Copyright (c) holder : All rights reserved                    *
 * - License              : BSD 2-Clause License                   * 
 * - Date                 : 20/04/2017                             *
 * ***********************************************************************************************************************************************************************/
 
 /*********************************** NOTE **************************************/
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:

// * Redistributions of source code must retain the above copyright notice, this
//  list of conditions and the following disclaimer.

// * Redistributions in binary form must reproduce the above copyright notice,
//  this list of conditions and the following disclaimer in the documentation
//  and/or other materials provided with the distribution.

// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED

/*

                                                         ─▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄
                                                         █░░░█░░░░░░░░░░▄▄░██░█
                                                         █░▀▀█▀▀░▄▀░▄▀░░▀▀░▄▄░█
                                                         █░░░▀░░░▄▄▄▄▄░░██░▀▀░█
                                                         ─▀▄▄▄▄▄▀─────▀▄▄▄▄▄▄▀

*/

#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
#define SERVOMIN  102// This is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  492 // This is the 'maximum' pulse length count (out of 4096)
#define SERVO_FREQ 50 // Analog servos run at ~50 Hz updates


//define servos' ports
//                            Leg 0 (FR)    Leg 1 (RR)    Leg 2 (FL)    Leg 3 (RL)
//                             F   C   T     F   C   T     F   C   T     F   C   T
const int servo_pin[4][3] = {{ 1,  3,  0}, { 9, 11,  8}, { 5,  7,  4}, {13, 15, 12}};

void setup()
{
  pwm.begin();
  pwm.setOscillatorFrequency(27000000);
  pwm.setPWMFreq(SERVO_FREQ);
  delay(10);
}

void loop(void)
{
  for (int i = 0; i < 4; i++)
  {
    for (int j = 0; j < 3; j++)
    {
      pwm.setPWM(servo_pin[i][j], 0, map(90, 0, 180, SERVOMIN, SERVOMAX));
      delay(20);
    }
  }
}
