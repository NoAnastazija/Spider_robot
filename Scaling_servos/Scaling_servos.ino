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

#include <Servo.h>   

Servo servo[4][3];

//define servos' ports
const int servo_pin[4][3] = { {2, 3, 4}, {5, 6, 7}, {8, 9, 10}, {11, 12, 13} };

void setup()
{
  //initialize all servos
  for (int i = 0; i < 4; i++)
  {
    for (int j = 0; j < 3; j++)
    {
      servo[i][j].attach(servo_pin[i][j]);
      delay(20);
    }
  }
}

void loop(void)
{
  for (int i = 0; i < 4; i++)
  {
    for (int j = 0; j < 3; j++)
    {
      servo[i][j].write(90);
      delay(20);
    }
  }
}
