# -*- coding: utf-8 -*-
"""
Purpose:
    this code is not examples, but helpers for other examples
    like all the example code it uses f strings a lot so
    make sure you have some understanding of f strings
    all code here are helpers, not examples, but you
    may need to understand this code to understand the
    examples.

Example use:

    import ex_helpers
    ex_helpers.info_about_obj( a_obj, msg = "for a_object:" )

Search:

    eval

"""

#import pandas as pd
#import numpy as np
#import sys
#import pprint
import time
import collections

import sys
from   pandas import Series, DataFrame

indent_0    = "   " # used for formatting

# ----------------------------------------
class CodeTimer():
    """
    Purpose:
        Time code, particularly for comparisons
        report ratios
    !! consider a calibrate for empty start stop
    !! what about time clock
    Example use:

        import ex_helpers
        a_code_timer = ex_helpers.CodeTimer()
        a_code_timer.start()
        # something
        a_code_timer.stop()

        # repeat

        a_code_timer.report()

    """
    def __init__( self, ):
        self.Timed      = collections.namedtuple( "Timed", "msg  timing" )

        self.reset()

    # ----------------------------------------
    def reset( self,  ):
        """
        Purpose:
            call to reset history and anything else needed
            for reuse of object
        Return:
            mutates self
        """
        self.records      = []

    # ----------------------------------------
    def start( self, msg = None ):
        """
        Purpose:
            call to start timing
        Return:
            mutates self
        """
        self.msg          = msg
        self.time_start   = time.time()
        self.perf_start   = time.perf_counter()
        self.time_end     = self.time_start
        self.perf_end     = self.perf_start

    # ----------------------------------------
    def stop( self, rpt = True ):
        """
        Purpose:
            call at end of timing
        Return:
            mutates self
        """
        self.time_end   = time.time()
        self.perf_end   = time.perf_counter()

        perf_elapsed    = self.perf_end - self.perf_start

        a_record        = self.Timed( msg = self.msg,  timing =  perf_elapsed )

        self.records.append( a_record )

        if rpt:
            self._report_stop( )

    # ----------------------------------------
    def _report_stop( self, ):
        """
        Purpose:
            call after end of timing -- on stop
            print a report of that timing
        Return:
            prints output
        """
        print( f"Stop: {self.msg}" )

        # msg   = ( f"    by time:         {self.time_end - self.time_start} seconds" )
        # print( msg )

        msg   = ( f"    by perf_counter: {self.perf_end - self.perf_start} seconds" )
        print( msg )

    # ----------------------------------------
    def report( self,   ):
        """
        Purpose:
            call after set of timings for relative timings
            prints a report
        Return:
            prints output
        """
        print( "\nTimings:")

        base_timing = None
        for a_record in self.records:
            a_msg       = a_record.msg
            a_timing    = a_record.timing
            if base_timing is None:
                # will happen on first timing
                base_timing = a_timing

            #timing_msg   =  f"{a_msg}  perf_time = {a_timing} relative time = {relative_timing}"
            relative_timing  = a_timing / base_timing
            # need better formatting
            timing_msg   =  f"{a_msg}\n    perf_time = {a_timing} relative time = {relative_timing}"
            print( timing_msg )

# ---------------
def begin_example( ex_name ):
    """
    Purpose:
        print a standardized heading for an example
        what it says, read
    Returns:
        prints output
    """
    return f"\n\n=========== {ex_name}(): =========== "

# ---------------
def end_example( ex_name ):
    """
    Purpose:
        print a uniform end to all examples
        what it says, read
    Returns:
        prints output
    Example:
        ex_helpers.end_example( ex_name )
    """
    print ( f"\n\n----- end of example {ex_name}() ----- \n\n" )

# # ---- example of example:
# # next use of begin end example
# # ----------------------------------------
# import ex_helpers
# def ex_template():
#     ex_name  = "ex_template"    
#         # not part of example, marks end
#     print( f"""{ex_helpers.begin_example( ex_name )}
#     template showing
#     use of begin_example, end-example  =
#     sys.path.append( "../"  )
#     """ )

#     print( "thats all folks" )

#     ex_helpers.end_example( ex_name )   

# #ex_template()

# ---------------
def get_data( a_key ):
    """
    Purpose:
        helper
        what it says, read
        this gets private data from a directory in this file system
        with data that should remain private

        Each user will need to implement this for themselves
        do not post private data to git !
    Returns:
        private data of any sort
    """
    # next poorly placed to make reimplementation for others easier
    sys.path.append( r"D:/Russ/0000/python00/python3/_projects/rsh"  )   # for sensitive data
        # this is only for running on russ's system to support next import
    import data
    rsh_data   = data.get_data( a_key )
    # print( f"{a_key} {rsh_data}" )
    return rsh_data

# ----------------------------------------
def print_double_bar_sep( ):
    """
    Purpose:
        prints a "double bar" across output
        read it
    """
    print( "\n" + 50 * "=" + "\n")


# ---- Info functions -- print a nice set of info about an object
# ----------------------------------------
def  info_about_obj( a_obj, msg = "for a_object:" ):
    """
    Purpose:
        prints information about objects
        sort of a pretty print +
        has some isinstance branching to get the right  display
        this branches to right function for ease of calling
        may want to add more cases for different types
    args:
        a_obj    an object to examine
        msg      msg to be printed along with the other info
    Returns:
        prints output
    Example Call:
        ex_helpers.info_about_obj( a_obj, msg = "info_about_obj:" )
    """
    if  isinstance( a_obj, list ):
        info_about_list( a_obj, msg )

    elif  isinstance( a_obj, Series ):
        info_about_series( a_obj, msg )

    elif isinstance( a_obj, DataFrame ):
        info_about_dataframe( a_obj, msg )

    elif isinstance( a_obj, dict ):
        info_about_dict( a_obj, msg )

    elif isinstance( a_obj, DataFrame ):
        info_about_dataframe( a_obj, msg )

    elif isinstance( a_obj, DataFrame ):
        info_about_dataframe( a_obj, msg )

    else:
        print(  "\n!!!! info_about_obj ---- did not identify object type" )
        print( f"\nfor msg = {msg} object is of Type {type(a_obj)}" )
        print( f">{a_obj}<")
        print( f"type is = { str( type(a_obj) ) } \n     "
               f"str     = {str( a_obj )} \n     repr    = {repr(a_obj )}" )

        print( "------\n")

# ----------------------------------------
def  info_about_series( a_series, msg = "for a_series:" ):
    """
    Purpose:
        prints information about series
        see inof_about_obj
    args:
        a_obj    an object to examine -- best an instance of series
        msg      msg to be printed along with the other info
    Returns:
        prints output
    Example Call:
        ex_helpers.info_about_series( a_obj, msg = "info_about_series:" )
    """
    if  isinstance( a_series, Series ):
        print( f"\nmsg {msg}" )
        print( f"     series: >{a_series}<" )
        print( f"     a_series.values: >{a_series.values}<" )
        print( f"     a_series.index: >{a_series.index}<" )
    else:
        print( f"\nfor msg = {msg} object is not an instance of Seriesbut is {type(a_series)}" )
    print( "------\n")

# ----------------------------------------
def  info_about_dataframe( a_obj, msg = "for a DataFrame:" ):
    """
    Purpose:
        another info about function -- see related functions, inof_about_....
        read
    """
    if  isinstance( a_obj, DataFrame ):
        print( f"\nmsg {msg}" )
        print( f"     DataFrame: >{a_obj}<" )

        print( f"     dataframe.values: >{a_obj.values}<" )
    else:
        print( f"\nfor msg = {msg} object is not an instance of DataFramebut is {type(a_obj)}" )
    print( "------\n")

# ----------------------------------------
def  info_about_dict( a_obj, msg = "for a dict:" ):
    """
    Purpose:
        another info about function -- see related functions, inof_about_....
        read
    Args:
        a_obj  a_dict
        msg    a message to be printed has default

    Returns:
        prints output 
    Example Call:
        ex_helpers.info_about_dict( a_obj, msg = "info_about_dict:" )

    """
    if  isinstance( a_obj, dict ):

        print( f"\nmsg {msg}" )
        #print( f"     Dict: >{a_obj}<" )
        print( "dict list --------->" )
        for  key, value in a_obj.items():
            print( f"{key}: {value}" )

        #print( f"     dataframe.values: >{a_obj.values}<" )
        # print( f"     a_series.index: >{a_series.index}<" )
    else:
        print( f"\nfor msg = {msg} object is not an instance "
                         f"of Dict but is {type(a_obj)}" )
    print( "------\n")

# ----------------------------------------
def info_about_list( a_obj, msg = "for a list:" ):
    """
    Purpose:
        another info about function -- see related functions, inof_about_....
        read
    """
    if  isinstance( a_obj, list ):
        print( f"\nmsg: {msg}" )
        #print( f"     Dict: >{a_obj}<" )
        print( f"length of list is: {len( a_obj )}")
        print( "list --------->" )
        ix = 0
        for i_list in a_obj:
            print( f"** {ix} {i_list}" )
            ix += 1
            #print( ix )
            if ix > 20:
                print( "and more items.... " )
                break

    else:
        print( f"\nfor msg = {msg} object is not an instance of list but is a {type(a_obj)}" )
    print( "------\n")

# ----------------------------------------
def info_about_unicode( a_obj, msg = None ):
    """
    Purpose:
        another info about function -- see related functions, inof_about_....
        read
    """
    if msg is None:
        msg = f"info about a {type( a_obj)}"

    if  isinstance( a_obj, str ):
        info_about_unicode_str( a_obj, msg   )
    elif isinstance( a_obj, bytes ):
        info_about_bytes( a_obj, msg   )

    else:
        print( f"\nfor msg = {msg} object is not unicode but is a {type(a_obj)}" )
    print( "------\n")

# ----------------------------------------
def info_about_unicode_str( a_obj, msg = "for a unicode for a str:" ):
    """
    Purpose:
        another info about function -- see related functions, info_about_....
        read
    """
    if  isinstance( a_obj, str ):
        print( f"\nmsg: {msg}" )
        #print( f"     Dict: >{a_obj}<" )
        print( f"object isinstance of str of type {type(a_obj)}")
        print( f"as a string it is >{a_obj}<")

        msg     =  f"   repr is >{a_obj.__repr__()}<"
        print( msg )

        print( f"length of str is: {len( a_obj )}")
        if a_obj.isascii():
            msg = f"a_obj is ASCII = >{a_obj}<"
        else:
            msg = f"a_obj NOT ASCII >{a_obj}<"
        print( msg )
        msg     =  f"   repr is >{a_obj.__repr__()}<"
        print( msg )

    else:
        print( f"\nfor msg = {msg} object is not an instance of str but is a {type(a_obj)}" )
    print( "------\n")

# ----------------------------------------
def info_about_bytes( a_obj, msg = "for a unicode for a bytes:" ):
    """
    Purpose:
        another info about function -- see related functions, inof_about_....
        read
    """
    if  isinstance( a_obj,  bytes ):
        print( f"\nmsg: {msg}" )
        #print( f"     Dict: >{a_obj}<" )
        print( f"length of bytes is: {len( a_obj )}")
        # if a_obj.isascii():
        #     msg = f"a_obj is ASCII {a_obj}"
        # else:
        #     msg = f"a_obj NOT ASCII {a_obj}"
        # print( msg )
        msg     =  f"   repr>>{a_obj.__repr__()}"
        print( msg )

        # for  i_list in a_obj:
        #      print( f"** {i_list}" )

    else:
        print( f"\nfor msg = {msg} object is not an instance of bytes but is  a {type(a_obj)}" )
    print( "------\n")

# ----------------------------------------
def str_about_dict( a_obj, msg = "for a dict:", starting_indent = "" ):
    """
    Purpose:
        may be a leftover or not
    Args:
        a_obj object to be examined 
        msg    message to print 

    Returns:
        print output 
        str

    """
    ret_str   = f"{starting_indent}{msg}"

    if  isinstance( a_obj, dict ):

        #ret_str   =  f"\nmsg {msg}" )
        #print( f"     Dict: >{a_obj}<" )
        ret_str   =  f"{ret_str}\n{starting_indent}dict list --------->"
        for key, value in a_obj.items():
            ret_str   =  f"{ret_str}\n{starting_indent}{indent_0} {key}: {value}"

        #print( f"     dataframe.values: >{a_obj.values}<" )
        # print( f"     a_series.index: >{a_series.index}<" )
    else:
        ret_str   = ( f"\n{starting_indent}for msg = {msg} object "
                     f"is not an instance of Dict but is {type(a_obj)}" )
        ret_str   = ( "{ret_str}\n{starting_indent}------\n")

    return ret_str

# --------------------- helper -------------------------
def show_timedelta( delta ):
    """
    Purpose:
        prints info about a time delta, perhaps shoudl be an info_about_... function
        what it says, read
    Returns:
        prints output

    """
    print(  2*"\n" +f"delta.               {delta}" )
    print(  f"delta.min (minimum)  {delta.min }"  )
    print( "these are the only attributes related to instance, compute others")
    print(  f"delta.days           {delta.days}"  )
    print(  f"delta.seconds        {delta.seconds }"  )
    print(  f"delta.microseconds   {delta.microseconds }"  )

    print( "compute minutes/sec possibley on 2 different days" )
    minutes_delta   =  int( ( ( delta.days * 60 * 60 * 24 ) + delta.seconds ) / 60 )
    print(  f"minutes_delta   {minutes_delta}"  )

    print( "compute minutes possibley on 2 different days" )
    seconds_delta   =  int( ( ( delta.days  * 60 * 24 ) + delta.seconds )   )
    print(  f"seconds_delta   {seconds_delta}"  )

    print(  f"60 * 60 * 24   {60 * 60 * 24}"  )

 
# ---- eval which is best ?? newest at top see test_helpers
# nextcurrently best, perhaps become only
# ----------------------------------------
def exec_and_print( msg          = None,
                    code         = "'nothing to eval'",
                    as_locals    = None,   # locals() # normally locals()
                    as_globals   = None,
                    print_flag   = True ):

    """
    Purpose:
        show a string and execute the code in it, code may include assignments
        the exec function itself returns no value, eval does.
        info may be returned in the locals or globals ?
        related to compile function
    Returns:
        a string of some meaning, will print if print_flag is true
        prints output

    Args:
        msg             = message to be printed
        as_globals      = globals to use may be globals()
        as_values       = a dict: lists symbolic value to be used by eval as locals  locals()
        code            = string of code to be executed, may be multilined
        print_flag      = True to print msg and ...

    Returns:
        result of this function as string
        may print results

    Example:

       ex_helpers.exec_and_print(   msg          ="from index to end",
                                    code         = "a_string[ 1: ]",
                                    as_locals    = locals(),   # normally locals for the evel
                                    as_globals   = None,
                                    print_flag   = True )

       if an exception occurs this will swallow it and report ??
       use as shown in:
            examples in test_helpers.py

    """
    exec_to  = None  # exec always return none
    indent   = "    "
    a_str    = "\n"
    if msg is not None:
        a_str     = f"{a_str}{msg}:\n{indent}{code} ==>"
    else:
        a_str     = f'{code} ==>'

    try:
        exec_to  = exec( code, as_globals, as_locals ) # return will be None

    except Exception as an_exception:
        a_str        = f'{a_str}\n{indent}exec caused exception {an_exception}'

    else:  # no exception
        a_str        = f'{a_str}\n{indent}{indent}>>executed without an exception<<'
    # if msg is None:
    #     #msg  = f"Eval the string >{code}<"
    #     msg  = "Eval a string"
    # else:
    #     #msg  = f"Eval the string {msg} >{code}<"
    #     msg  = f"Eval a string: {msg}"

    if print_flag:
        print( a_str )
        # print( msg )
        # print( f"{code} =>" )
        # print( f">>{ret}<<" )

        # # work on this next more look at string instead of print
        # print( ">>", )
        # pprint.pprint( ret, )
        # print( "<<")

    return ( exec_to, a_str )

# ----------------------------------------
def eval_and_print( msg          = None,
                    code         = "'nothing to eval'",
                    as_locals    = None,   # locals() # normally locals()
                    as_globals   = None,
                    print_flag   = True ):

    """
    Purpose:
        show a string and print and retrun what it evals to.
    Returns:
        prints output

    Args:
        msg             = message to be printed
        code            = string of code to be run/evaluated
        as_locals       = a dict: lists symbolic value to be used by eval as locals  locals()
        as_globals      = globals to use may be globals()
        print_flag      = True to print msg and the evaluation

    Returns:
        result of evaluation and string of from this function
        may print results -- normal use

    Example:

       ex_helpers.eval_and_print(   msg          ="from index to end",
                                    code         = "a_string[ 1: ]",
                                    as_locals    = locals(),   # normally locals for the evel
                                    as_globals   = None,
                                    print_flag   = True )

       if an exception occurs this will swallow it and report
       use as shown in:
            examples in test_helpers.py

    """
    indent   = "    "
    a_str    = "\n"
    eval_to  = None  # for exceptions
    if msg is not None:
        a_str     = f"{a_str}{msg}:\n{indent}{code} ==>"
    else:
        a_str     = f'{code} ==>'

    try:
        eval_to    = eval( code, as_globals, as_locals )
    except Exception as an_exception:
        #ret        = f"eval caused exception {an_exception}"
        a_str        = f'{a_str}\n{indent}eval caused exception {an_exception}'
    else:  # no exception
        a_str        = f'{a_str}\n{indent}{indent}>>{eval_to}<<'
    # if msg is None:
    #     #msg  = f"Eval the string >{code}<"
    #     msg  = "Eval a string"
    # else:
    #     #msg  = f"Eval the string {msg} >{code}<"
    #     msg  = f"Eval a string: {msg}"

    if print_flag:
        print( a_str )
        # print( msg )
        # print( f"{code} =>" )
        # print( f">>{ret}<<" )

        # # work on this next more look at string instead of print
        # print( ">>", )
        # pprint.pprint( ret, )
        # print( "<<")

    return ( eval_to, a_str )


# ----------------------------------------
def print_eval( eval_string, msg = "Next eval the string", gl = None, lo = None  ):
    """
    Purpose:
        deprecated soon to be gone 
        show string and show its eval
        probably should not be used, favor function above
        what it says, read
    Returns:
        prints output

    """
    print( f"\n{ msg }: >>{eval_string}<<" )
    ret   = f"     >>{eval( eval_string, gl, lo )}<<end eval\n"
    #ret   = f"     >>{eval( eval_string, globals(), locals() )}<<end eval\n"
    #ret   = f"     >>{eval( eval_string, locals(), globals() )}<<end eval\n"

    print( ret  )


# #--------------------------------
# if __name__ == "__main__":

    # pass










