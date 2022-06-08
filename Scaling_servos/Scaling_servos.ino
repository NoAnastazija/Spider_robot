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
#define SERVOMIN  150 // This is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  600 // This is the 'maximum' pulse length count (out of 4096)
#define USMIN  600 // This is the rounded 'minimum' microsecond length based on the minimum pulse of 150
#define USMAX  2400 // This is the rounded 'maximum' microsecond length based on the maximum pulse of 600
#define SERVO_FREQ 50 // Analog servos run at ~50 Hz updates


//define servos' ports
const int servo_pin[4][3] = { {0, 1, 3}, {8, 9, 11}, {4, 5, 7}, {12, 13, 15} };

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
