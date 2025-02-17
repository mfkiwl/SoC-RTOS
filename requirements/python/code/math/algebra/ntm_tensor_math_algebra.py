###################################################################################
##                                            __ _      _     _                  ##
##                                           / _(_)    | |   | |                 ##
##                __ _ _   _  ___  ___ _ __ | |_ _  ___| | __| |                 ##
##               / _` | | | |/ _ \/ _ \ '_ \|  _| |/ _ \ |/ _` |                 ##
##              | (_| | |_| |  __/  __/ | | | | | |  __/ | (_| |                 ##
##               \__, |\__,_|\___|\___|_| |_|_| |_|\___|_|\__,_|                 ##
##                  | |                                                          ##
##                  |_|                                                          ##
##                                                                               ##
##                                                                               ##
##              Peripheral-NTM for MPSoC                                         ##
##              Neural Turing Machine for MPSoC                                  ##
##                                                                               ##
###################################################################################

###################################################################################
##                                                                               ##
## Copyright (c) 2022-2023 by the author(s)                                      ##
##                                                                               ##
## Permission is hereby granted, free of charge, to any person obtaining a copy  ##
## of this software and associated documentation files (the "Software"), to deal ##
## in the Software without restriction, including without limitation the rights  ##
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell     ##
## copies of the Software, and to permit persons to whom the Software is         ##
## furnished to do so, subject to the following conditions:                      ##
##                                                                               ##
## The above copyright notice and this permission notice shall be included in    ##
## all copies or substantial portions of the Software.                           ##
##                                                                               ##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR    ##
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,      ##
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE   ##
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER        ##
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, ##
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN     ##
## THE SOFTWARE.                                                                 ##
##                                                                               ##
## ============================================================================= ##
## Author(s):                                                                    ##
##   Paco Reina Campo <pacoreinacampo@queenfield.tech>                           ##
##                                                                               ##
###################################################################################

import numpy as np 

class TensorArithmetic:
  def __init__(self, data_a_in, data_b_in):
    self.data_a_in = data_a_in
    self.data_b_in = data_b_in

  def ntm_tensor_adder(self):
    a_in = np.array(self.data_a_in)
    b_in = np.array(self.data_b_in)

    data_out = []

    # calculating addition
    for i in range(len(data_a_in)):
      data_out.append([])
      for j in range(len(data_a_in[i])):
        data_out[i].append([])
        for k in range(len(data_a_in[i][j])):
          data_out[i][j].append(a_in[i][j][k] + b_in[i][j][k])

    return data_out

  def ntm_tensor_multiplier(self):
    a_in = np.array(self.data_a_in)
    b_in = np.array(self.data_b_in)

    data_out = []

    # calculating multiplication
    for i in range(len(data_a_in)):
      data_out.append([])
      for j in range(len(data_a_in[i])):
        data_out[i].append([])
        for k in range(len(data_a_in[i][j])):
          data_out[i][j].append(a_in[i][j][k] * b_in[i][j][k])

    return data_out

  def ntm_tensor_divider(self):
    a_in = np.array(self.data_a_in)
    b_in = np.array(self.data_b_in)

    data_out = []

    # calculating division
    for i in range(len(data_a_in)):
      data_out.append([])
      for j in range(len(data_a_in[i])):
        data_out[i].append([])
        for k in range(len(data_a_in[i][j])):
          data_out[i][j].append(a_in[i][j][k] / b_in[i][j][k])

    return data_out


data_a_in = np.random.rand(3,3,3)
data_b_in = np.random.rand(3,3,3)


arithmetic = TensorArithmetic(data_a_in, data_b_in)


np.testing.assert_array_equal(arithmetic.ntm_tensor_adder(), data_a_in + data_b_in)

np.testing.assert_array_equal(arithmetic.ntm_tensor_multiplier(), data_a_in * data_b_in)

np.testing.assert_array_equal(arithmetic.ntm_tensor_divider(), data_a_in / data_b_in)
