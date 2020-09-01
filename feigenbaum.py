import numpy as np

def format( value_float_, precision_int_=5 ):

    precision_aux =  "%."+str(precision_int_)+"f"

    return precision_aux %value_float_

def logistic_map( x_float_, r_float_ ):

    return 1.0*r_float_*x_float_*( 1.0 - x_float_ )

def exponential_map( x_float_, r_float_ ):

    return 1.0*x_float_*np.exp(r_float_*(1-x_float_))

def cobweb_diagram( r_float_, init_cond_float_, N_steps_int_ ):

    x_pos_ary = np.empty(N_steps_int_+1)
    y_pos_ary = np.empty(N_steps_int_+1)

    x_pos_ary[0] = init_cond_float_
    y_pos_ary[0] = 0

    for i_int in np.arange(1,N_steps_int_+1,2):

        x_pos_ary[ i_int ] = x_pos_ary[ i_int-1 ]
        y_pos_ary[ i_int ] = logistic_map( x_pos_ary[ i_int-1 ], r_float_ )

        x_pos_ary[ i_int+1 ] = y_pos_ary[ i_int ]
        y_pos_ary[ i_int+1 ] = y_pos_ary[ i_int ]

    return x_pos_ary, y_pos_ary

def feigenbaum_diagram( r_float_, init_cond_float_, N_steps_int_, L_tail_int_ ):

    x_ary = np.zeros( N_steps_int_, dtype=float )
    x_ary[0] = init_cond_float_

    for i_int in np.arange( 1, N_steps_int_ ):

        x_ary[ i_int ] = exponential_map( x_ary[i_int-1], r_float_ )
        # x_ary[ i_int ] = logistic_map( x_ary[i_int-1], r_float_ )

    return x_ary[-L_tail_int_:-1]

def main():

    init_cond_float = 0.5
    N_steps_int = 1000
    L_tail_int = 500
    step_size_float = 0.01

    x_cob_web_ary = np.zeros( N_steps_int )
    y_cob_web_ary = np.zeros( N_steps_int )

    r_value_ary = np.arange( 0, 4, step_size_float )

    cob_web_file = open( "cobweb_diagram.txt", "w" )

    for r_value_float in r_value_ary:

        x_cob_web_ary, y_cob_web_ary = cobweb_diagram( r_value_float, init_cond_float, N_steps_int )

        for i_int in np.arange( len( x_cob_web_ary ) ):

            cob_web_file.write( str( x_cob_web_ary[ i_int ] )+"\t\t"+ str( y_cob_web_ary[ i_int ] )+"\n" )
        
        cob_web_file.write( "\n\n" )

    cob_web_file.close()

    feigenbaum_diagram_file = open( "feigenbaum_diagram.txt" , "w" )

    for r_value_float in r_value_ary:

        orbit_ary = feigenbaum_diagram( r_value_float, init_cond_float, N_steps_int, L_tail_int )

        for value_float in orbit_ary:

            feigenbaum_diagram_file.write( str( format(r_value_float, 4) )+"\t\t"+str(format( value_float, 4 ))+"\n"  )

    feigenbaum_diagram_file.close()

if __name__ == '__main__':
    main()