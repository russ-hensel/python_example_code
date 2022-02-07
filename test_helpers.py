# -*- coding: utf-8 -*-
#>>>>>python example timing of different code for speed differences or just timing







"""
 

Search for:
    ex_timings.py
    ex_run_fast.py

    perf_counter
    time
    time.perf_counter



"""

import datetime
import time
import sys
sys.path.append( r"D:\Russ\0000\python00\python3\_examples"  )
import ex_helpers

# ----------------------------------------
def ex_template():
    ex_name  = "ex_template"    # >> end with ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )} template showing use of begin_example, end-example  ===============
    """ )

    print( "thats all folks" )

    ex_helpers.end_example( ex_name )

#ex_template()



# ----------------------------------------
def test_time_some_code():
    ex_name  = "test_time_some_code"   # end with >> ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )}  bunch of conversions from web  good: keep   ===============
    """ )

    
    timestamp       = 1226527167.595983
    loop_max        = int( 1e5 )
     

    # again with time_util
    code_timer    = ex_helpers.CodeTimer()
    msg           = f"\nfor {loop_max} itterations code took - using CodeTimer"
    code_timer.start( msg )

    for ix in range( 1, loop_max  ):

          time_tuple = time.gmtime( timestamp )

    code_timer.stop()
    
    loop_max        = int( 1e4 )
     
    # ---- second test 
    msg           = f"\nfor {loop_max} itterations code took - using CodeTimer"
    code_timer.start( msg )
    for ix in range( 1, loop_max  ):

          time_tuple = time.gmtime( timestamp )

    code_timer.stop()
    code_timer.report_all()
    
    
    ex_helpers.end_example( ex_name )

# 

# test_time_some_code()

# ----------------------------------------
def xxx():
    ex_name  = "xxx"    # >> end with ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )}  
           and so on 
    """ )

    print( "thats all folks" )

    ex_helpers.end_example( ex_name )
    
#test_eval_and_print() 


# ----------------------------------------
def test_eval_with_args():
    ex_name  = "test_eval_with_args"     # end with >>  ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )}
          eval_and_print( msg = None, values = None, eval_string= "nothing to eval", print_flag = True ):
    """)

    locals   = { "test_1":   ">23456789<",   # a string to test with len 10
                 "test_2":   12.45,         # number to test with len 5
                 "test_3":   ">33333333<",   # a string to test with
                 "test_bar": "12345678901234567890123456789012345678901234567890123456789",
                 }
    
    #msg      =  eval( 'f"{test_1:>15}{test_2:>10}{test_3:>5}"', None, None  )         # error on test_1
    #msg      =  eval( 'f"{test_1:>15}{test_2:>10}{test_3:>5}"', globals = None,    )  # keyword not allowed
    
    eval_string  =  'f"{test_1:>15}{test_2:>10}{test_3:>5}"' 
    ret  = ex_helpers.eval_and_print( msg = "from test_eval_with_args", values = locals,  eval_string = eval_string, print_flag = True )
    print( f"ret  = >>{ret}<<")

test_eval_with_args()


  


 



# ========================= eof =========================











