import numpy as np

'''
    0 d1 0 0
 [cos(0)   -sin(0)*cos(0)  sin(0)*sin(0)     0*cos(0)  ]
 [sin(0)   cos(0)*cos(0)   -cos(0)*sin(0)    0*sin(0)  ]
 [0        sin(0)          cos(0)                   d1                ]
 [0        0               0                               1                   ]
'''

'''
 [cos(theta[k])   -sin(theta[k])*cos(alpha[k])  sin(theta[k])*sin(alpha[k])     a[k]*cos(theta[k])  ]
 [sin(theta[k])   cos(theta[k])*cos(alpha[k])   -cos(theta[k])*sin(alpha[k])    a[k]*sin(theta[k])  ]
 [0               np.sin(alpha[k])              cos(alpha[k])                   d[k]                ]
 [0               0                             0                               1                   ]
'''

'''
 [cos(theta[k])   -sin(theta[k])*cos(alpha[k])  sin(theta[k])*sin(alpha[k])     a[k]*cos(theta[k])  ]
 [sin(theta[k])   cos(theta[k])*cos(alpha[k])   -cos(theta[k])*sin(alpha[k])    a[k]*sin(theta[k])  ]
 [0               np.sin(alpha[k])              cos(alpha[k])                   d[k]                ]
 [0               0                             0                               1                   ]
'''
def trans_k(k, theta, d, a, alpha):
    return  np.matrix(   [[np.cos(theta[k]),   -np.sin(theta[k])*np.cos(alpha[k]),  np.sin(theta[k])*np.sin(alpha[k]),   a[k]*np.cos(theta[k])  ],
                            [np.sin(theta[k]),   np.cos(theta[k])*np.cos(alpha[k]),   -np.cos(theta[k])*np.sin(alpha[k]),  a[k]*np.sin(theta[k])  ],
                            [0,                  np.sin(alpha[k]),                    np.cos(alpha[k]),                    d[k]                   ],
                            [0,                  0,                                   0,                                   1                      ]])

def poly_interp_2(t):
    t0 = 0.0
    t1 = 4.0
    a1 = 42* (np.pi/180.0)
    a2 = 76* (np.pi/180.0)
    a_change = a2 - a1
    v_ends = 0.0
    tau = t/(t1-t0)
    f = a1 + a_change*(-2*tau*tau*tau + 3*tau*tau)
    return f

def adc_math():
    minvolts = 0.0
    maxvolts = 5.0
    minbitvalue = 0
    maxbitvalue = 1023
    voltage_range = maxvolts - minvolts
    number_bit_values = (maxbitvalue - minbitvalue) + 1
    resolution_in_volts_per_ADC_bit = voltage_range/number_bit_values

    '''
    The minimum clock speed requirement results from charge "bleed" off of the sample capacitor.
    The sampling capacitor itself stores the electrical charge that's actually measured by the ADC.
    When the clock is too slow, the charge in the capacitor will start to dissapate. For this device,
    a frequency of ~10KHz should be maintained.
    '''

    '''
    Distance = Time x Speed of Sound/2
    d = 341/m/s in air * time * (1/2)
    100 ms = 10Hz sampling freq, Nyquist says we can sample up to 5Hz signals w/o aliasing
    200 ms = 5HZ
    d = 431 * 0.2 * (1/2) = 43.1 meters
    '''

    '''
    A jacobian has 6 rows because each velocity parameter exists in 3 dimensional space.
    That means that there are 3 orthagonal linear velocities and 3 orthagonal angular velocities
    that must be stored for each joint in 3D space.
    The number of columns is determined by the number of joints in the system.
    '''

    '''
    A singular or degenerate Jacobian would have a determinant with value 0.
    For it to generally be invertible, the Jacobian would have to be a square matrix satisying the
    above condition.
    '''

def part6():
        t_0_6 = np.matrix( [    [ -0.988,   -0.152, 0,  -6.5 ],
                                [0.152,    -0.988, 0,  7 ],
                                [0.0,       0.0,    1,  5 ],
                                [0,         0,      0,  1 ]] )

        inv_t_0_6 = np.linalg.inv(t_0_6)
        d0 = np.matrix([[0],[0],[0],[1]])
        db = np.matrix([[-6],[7],[5],[1]])
        print(inv_t_0_6*d0)


def main():
    t2 = 12.5*np.pi/180.0
    t3 = 18.0*np.pi/180.0
    d1 = 5.0
    a2 = 3.5
    a3 = 2.5
    alph2 = np.pi/2
    # first 0 for 1 indexing
    theta =     [0, 0, t2, t3]
    d =         [0, d1, 0, 0]
    alpha =     [0, 0, alph2, 0]
    a =         [0, 0, a2, a3]
    #part6()
    #print(poly_interp_2(2.5)*180/np.pi)
    print(a2*np.cos( t1 ) + a3*np.cos( t1+t2) )
    print(a2*np.sin( t1 ) + a3*np.sin( t1+t2) )

    print( trans_k(1, theta, d, a, alpha)* trans_k(2, theta, d, a, alpha) * trans_k(3, theta, d, a, alpha))
    #print()
    #print()


if __name__ == '__main__':
    main()
