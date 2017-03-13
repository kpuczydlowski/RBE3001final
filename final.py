'''
Kacper Puczydlowski Final Exam
This document should contain all code necessary to obtain the test script results at the bottom
Answers to written questions are provided with the text
Marked-up pdf is attached

'''

import numpy as np
''' Part 1'''
'''-----------------------------------------------------------------------------------'''
'''
    Part 1 A
'''

'''-------------------------------'''
'''          DH Table             '''
'''-------------------------------'''
'''LinkN: theta   | d |  alpha  | a '''
'''-------------------------------'''
'''Link1:  0      | d1 | alpha1 | 0'''
'''Link2: theta2  | 0  | 0      | a2'''
'''Link3: theta3  | 0  | 0      | a3'''
'''-------------------------------'''
''' Joint Variables are d1, theta2, theta3 '''


'''
    Part 1 B
'''
'''
    HTM 0_1
 [cos(0)   -sin(0)*cos(alpha1)  sin(0)*sin(alpha1)     0*cos(0)  ]
 [sin(0)   cos(0)*cos(alpha1)   -cos(0)*sin(alpha1)    0*sin(0)  ]
 [0        sin(alpha1)          cos(alpha1)            d1        ]
 [0        0                    0                      1         ]
'''

'''
    HTM 1_2
 [cos(theta2)   -sin(theta2)*cos(0)  sin(theta2)*sin(0)     a2*cos(theta2)  ]
 [sin(theta2)   cos(theta2)*cos(0)   -cos(theta2)*sin(0)    a2*sin(theta2)  ]
 [0             sin(0)               cos(0)                 0               ]
 [0             0                         0                           1               ]
'''

'''
    HTM 2_3
 [cos(theta3)   -sin(theta3)*cos(0)  sin(theta3)*sin(0)     a3*cos(theta3)  ]
 [sin(theta3)   cos(theta3)*cos(0)   -cos(theta3)*sin(0)    a3*sin(theta3)  ]
 [0             sin(0)               cos(0)                 0               ]
 [0             0                    0                      1               ]
'''

def trans_k(k, theta, d, a, alpha):
    return  np.matrix(   [[np.cos(theta[k]),   -np.sin(theta[k])*np.cos(alpha[k]),  np.sin(theta[k])*np.sin(alpha[k]),   a[k]*np.cos(theta[k])  ],
                            [np.sin(theta[k]),   np.cos(theta[k])*np.cos(alpha[k]),   -np.cos(theta[k])*np.sin(alpha[k]),  a[k]*np.sin(theta[k])  ],
                            [0,                  np.sin(alpha[k]),                    np.cos(alpha[k]),                    d[k]                   ],
                            [0,                  0,                                   0,                                   1                      ]])

def part1c():
    t2 = 12.5*np.pi/180.0
    t3 = 18.0*np.pi/180.0
    d1 = 5.0
    a2 = 3.5
    a3 = 2.5
    alph1 = np.pi/2
    # first 0 for 1 indexing
    theta =     [0, 0, t2, t3]
    d =         [0, d1, 0, 0]
    alpha =     [0, alph1, 0, 0]
    a =         [0, 0, a2, a3]

    r = trans_k(1, theta, d, a, alpha)* trans_k(2, theta, d, a, alpha) * trans_k(3, theta, d, a, alpha)
    print
    print('Part1 C\n')
    print('HTM 0_3:')
    print(r)
    print
    print('Check using inv. kin')
    print('x: '+ str(a2*np.cos( t2 ) + a3*np.cos( t2+t3)) )
    print('z:'+ str( a2*np.sin( t2 )  + a3*np.sin( t2+t3) +5 ))
    print
    p = np.matrix([ [r[0,3]],[r[2,3]] ])
    print('p_vector:')
    print(p)
    print

''' Part 2'''

'''-----------------------------------------------------------------------------------'''

def part2():
    print('Part 2')
    print('cubic(2.5) = ' +str(poly_interp(2.5)*180/np.pi))
    print

def poly_interp(t):
    t0 = 0.0
    t1 = 4.0
    a1 = 42 * (np.pi/180.0)
    a2 = 76 * (np.pi/180.0)
    a_change = a2 - a1
    v_ends = 0.0
    tau = t/(t1-t0)
    f = a1 + a_change*(-2*tau*tau*tau + 3*tau*tau)
    return f

''' Part 3'''
'''-----------------------------------------------------------------------------------'''
def part3a():
    minvolts = 0.0
    maxvolts = 5.0
    minbitvalue = 0
    maxbitvalue = 4095
    voltage_range = maxvolts - minvolts
    number_bit_values = (maxbitvalue - minbitvalue) + 1
    resolution_in_volts_per_ADC_bit = voltage_range/number_bit_values
    print('Part 3 A')
    a = "{0:.3g}".format(resolution_in_volts_per_ADC_bit)
    print('Resolution in volts/bit: ' +a)
    print

    '''
    Part 3 B
    The minimum clock speed requirement results from charge "bleed" off of the sample capacitor.
    The sampling capacitor itself stores the electrical charge that's actually measured by the ADC.
    When the clock is too slow, the charge in the capacitor will start to dissapate. For this device,
    a frequency of ~10KHz should be maintained.
    '''

    '''
    Part 3 C
    Distance = Time x Speed of Sound/2
    -speed of sound in air is 341 m/s
    d = 341/m/s in air * time * (1/2)
    100 ms = 10Hz sampling freq, Nyquist says we can sample up to 5Hz signals w/o aliasing
    200 ms = 5HZ
    d = 431 * 0.2 * (1/2) = 43.1 meters
    '''
'''-----------------------------------------------------------------------------------'''
    '''
    Part 4
    Each column in the Jacobian represents the end-effector velocity generated by the corresponding
    joint moving at a (unit) velocity, given all other joints are immobilized and static.
    So, the number of columns is determined by the number of joints in the system.
    '''

'''-----------------------------------------------------------------------------------'''
    '''
    Part 5
    A singular or degenerate Jacobian would have a determinant with value 0.
    For it to generally be invertible, the Jacobian would have to be a square matrix satisying the
    above condition.
    '''

'''Part 6'''
'''-----------------------------------------------------------------------------------'''
def part6():
        t_0_6 = np.matrix( [    [ -0.988,   -0.152, 0,  -6.5 ],
                                [0.152,    -0.988, 0,  7 ],
                                [0.0,       0.0,    1,  5 ],
                                [0,         0,      0,  1 ]] )

        inv_t_0_6 = np.linalg.inv(t_0_6)

        p = np.matrix([ [inv_t_0_6[0,3]],[inv_t_0_6[1,3]],[inv_t_0_6[2,3]] ])
        print('Part 6')
        print('p_vector: ')
        print(p)
        print

def main():
    part1c()
    part2()
    part3a()
    part6()

if __name__ == '__main__':
    main()


'''
test script results:

        Part1 C

        HTM 0_3:
        [[  8.61629160e-01  -5.07538363e-01   0.00000000e+00   5.57110893e+00]
         [  3.10777616e-17   5.27595697e-17  -1.00000000e+00   1.24080268e-16]
         [  5.07538363e-01   8.61629160e-01   6.12323400e-17   7.02638456e+00]
         [  0.00000000e+00   0.00000000e+00   0.00000000e+00   1.00000000e+00]]

        Check using inv. kin
        x: 5.57110892602
        z:7.02638455619

        p_vector:
        [[ 5.57110893]
         [ 7.02638456]]

        Part 2
        cubic(2.5) = 65.2421875

        Part 3 A
        Resolution in volts/bit: 0.00122

        Part 6
        p_vector:
        [[-7.49163371]
         [ 5.93246121]
         [-5.        ]]

 '''
