# -*- coding: utf-8 -*-
"""
not examples, but helper for other examples
need to import anything that might be evaluated


import ex_helpers
ex_helpers.info_about_obj( a_obj, msg = "for a_object:" )


"""
from   pandas import Series, DataFrame
#import pandas as pd
#import numpy as np
#import sys
import pprint
import time
import collections

import sys
sys.path.append( r"D:/Russ/0000/python00/python3/_projects/rsh"  )   # for sensitive data
import data

"""
import sys
sys.path.append( r"D:/Russ/0000/python00/python3/_examples"  )
import ex_helpers
info_about_obj( a_obj, msg = "for a_object:" )


"""

indent_0    = "   "

# ----------------------------------------
class PrintStr(  ):
    """
    yes a purpose would be nice
    print_str = PrintStr( )
    print_str.str
    print_str.print( )
    """
    #----------- init -----------
    def __init__(self,  ):
        """
        Usual init see class doc string
        """
        self.str   = ""

    def print(self, a_str ):

        if  self.str == "":
            self.str = a_str
        else:
            self.str = f"{self.str}\n{a_str}"

        return self.str

# --------------- helper function -----------------------
def begin_example( ex_name ):
    """
    what it says, read
    get a uniform end to all examples

    end_example( ex_name )
    """
    return f"\n\n=========== {ex_name}(): =========== "

# --------------- helper function -----------------------
def get_data( a_key ):
    """
    what it says, read
    this gets private data from a directory others should not have
    """
    rsh_data   = data.get_data( a_key )
    # print( f"{a_key} {rsh_data}" )
    return rsh_data

# --------------- helper function -----------------------
def end_example( ex_name ):
    """
    what it says, read
    get a uniform end to all examples

    end_example( ex_name )
    """
    print ( f"\n\n----- end of example {ex_name}() ----- \n\n" )

# ----------------------------------------
def ex_template():
    ex_name  = "ex_template"   # end with >>    ex_helpers.end_example( ex_name )  # not part of example, marks end
    print( f"""{ex_helpers.begin_example( ex_name )}
    template showing
    use of begin_example, end-example  =
    sys.path.append( "../"  )
    """ )

    print( "thats all folks" )

    ex_helpers.end_example( ex_name )  # not part of example, marks end

#ex_template()


# ----------------------------------------
class CodeTimer():
    """
    !! consider then store and do ratios
    !! consider a calibrate for empty start stop
    !! what about time clock
    import ex_helpers
    a_code_timer = ex_helpers.CodeTimer()
    a_code_timer.start()
    # something
    a_code_timer.stop()
    a_code_timer.report( ver = ""  )
    # repeat

    a_code_timer.report_all()

    """
    def __init__( self, ):
        self.Timed      = collections.namedtuple( "Timed", "msg  timing" )

        self.reset()

    # ----------------------------------------
    def reset( self,  ):
        """
        call to reset history sart timing
        mutates self
        """
        self.records      = []
        #self.start()

    # ----------------------------------------
    def start( self, msg = None ):
        """
        call to sart timing
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
        call at end of timing
        mutates self

        """
        self.time_end   = time.time()
        self.perf_end   = time.perf_counter()

        perf_elapsed    = self.perf_end - self.perf_start

        a_record        = self.Timed( msg = self.msg,  timing =  perf_elapsed )

        self.records.append( a_record )

        if rpt:
            self.report( )

    # ----------------------------------------
    def report( self, ver = ""  ):
        """
        call after end of timing
        ver  just an idea about version  time or perf_counter
        mutates self

        """
        print( self.msg )

        # msg   = ( f"    by time:         {self.time_end - self.time_start} seconds" )
        # print( msg )

        msg   = ( f"    by perf_counter: {self.perf_end - self.perf_start} seconds" )
        print( msg )

    # ----------------------------------------
    def report_all( self,   ):
        """
        call after set of timings for a final report


        """
        print( "\nSummary of timings:")

        base_timing = None
        for a_record in self.records:
            a_msg       = a_record.msg
            a_timing    = a_record.timing
            if base_timing is None:
                base_timing = a_timing

            relative_timing  = a_timing / base_timing
            # need better formatting
            timing_msg   =  f"{a_msg}  perf_time = {a_timing} relative time = {relative_timing}"
            print( timing_msg )

# ----------------------------------------
def  info_about_obj( a_obj, msg = "for a_object:" ):
    """
    prints information about objects
    has some isinstance branching to get the right  display
    this branchches to right function for ease of calling
    args:
        a_obj    an object to examine
        msg      msg to be printed along with the other info
    Example Call:
        ex_helpers.info_about_dict( a_obj, msg = "info_about_dict:" )
    sort of a pretty print +
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
        info_about_obj
        print( f"\n!!!! info_about_obj ---- did not identify object" )
        print( f"\nfor msg = {msg} object is of Type {type(a_obj)}" )
        print( f">{a_obj}<")
        print( f"type is = { str( type(a_obj) ) } \n     str     = {str( a_obj )} \n     repr    = {repr(a_obj )}" )

        print( "------\n")

# ----------------------------------------
def  info_about_series( a_series, msg = "for a_series:" ):
    """
    another info about function
    read
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
    another info about function
    read
    """
    if  isinstance( a_obj, DataFrame ):
        print( f"\nmsg {msg}" )
        print( f"     DataFrame: >{a_obj}<" )

        print( f"     dataframe.values: >{a_obj.values}<" )
        # print( f"     a_series.index: >{a_series.index}<" )
    else:
        print( f"\nfor msg = {msg} object is not an instance of DataFramebut is {type(a_obj)}" )
    print( "------\n")


# ----------------------------------------
def str_about_dict( a_obj, msg = "for a dict:", starting_indent = "" ):
    """
    Args:
        a_obj (TYPE): DESCRIPTION.
        msg (TYPE, optional): DESCRIPTION. Defaults to "for a dict:".

    Returns:
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
        ret_str   =  f"\n{starting_indent}for msg = {msg} object is not an instance of Dict but is {type(a_obj)}"
        ret_str( "{ret_str}\n{starting_indent}------\n")

    return ret_str

# ---- helper function
def print_double_bar_sep( ):
    """
    helpers should have some minimal doc string

    prints a "double bar" across output
    read it
    """
    print( "\n" + 50 * "=" + "\n")



# ----------------------------------------
def  info_about_dict( a_obj, msg = "for a dict:" ):
    """
    Args:
        a_obj  a_dict
        msg (TYPE, optional): DESCRIPTION. Defaults to "for a dict:".

    Returns:
        debug string for dict
    Example Call:
        ex_helpers.info_about_dict( a_obj, msg = "info_about_dict:" )

    """
    print_str = PrintStr( )

    if  isinstance( a_obj, dict ):

        print_str.print( f"\nmsg {msg}" )
        #print( f"     Dict: >{a_obj}<" )
        print_str.print( "dict list --------->" )
        for  key, value in a_obj.items():
            print_str.print( f"{key}: {value}" )

        #print( f"     dataframe.values: >{a_obj.values}<" )
        # print( f"     a_series.index: >{a_series.index}<" )
    else:
        print_str.print( f"\nfor msg = {msg} object is not an instance of Dict but is {type(a_obj)}" )
    print_str.print( "------\n")
    ret = print_str.str
    print( ret )
    return ret

# ----------------------------------------
def info_about_list( a_obj, msg = "for a list:" ):
    """
    another info about function
    read
    consider pretty print
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
                break
        else:
            print( "and more items.... " )


    else:
        print( f"\nfor msg = {msg} object is not an instance of list but is a {type(a_obj)}" )
    print( "------\n")


# ----------------------------------------
def info_about_unicode( a_obj, msg = None ):
    """
    another info about function
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
    another info about function
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

        # for  i_list in a_obj:
        #      print( f"** {i_list}" )

    else:
        print( f"\nfor msg = {msg} object is not an instance of str but is a {type(a_obj)}" )
    print( "------\n")

# ----------------------------------------
def info_about_bytes( a_obj, msg = "for a unicode for a bytes:" ):
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


# --------------------- helper -------------------------
def show_timedelta( delta ):

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


# ----------------------------------------
def eval_and_print( msg          = None,
                    code         = "'nothing to eval'",
                    as_locals    = None,   # locals() # normally locals()
                    as_globals   = None,
                    print_flag   = True ):

    """
    currently best, perhaps become only
    briefly: show a string and print and retrun what it evals to.
       for more info see arguments
       ex_helpers.eval_and_print(   msg          ="from index to end",
                                    code         = "a_string[ 1: ]",
                                    as_locals    = locals(),   # normally locals for the evel
                                    as_globals   = None,
                                    print_flag   = True )

       if an exception occurs this will swallow it and report
    use as shown in:
        examples in test_helpers.py
    Args:
        msg             = message to be printed
        as_globals      = globals to use may be globals()
        as_values       = a dict: lists symbolic value to be used by eval as locals  locals()
        code            = string of code to be run/evaluated
        print_flag      = True to print msg and the evaluation

    Returns:
        result of evaluation

    """
    indent   = "    "
    str      = "\n"
    if msg is not None:
        str = f"{str}{msg}:\n{code}"
    else:
        str     = f'{code} ==>'

    try:
        eval_to    = eval( code, as_globals, as_locals )
    except Exception as an_exception:
        #ret        = f"eval caused exception {an_exception}"
        str        = f'{str}\n{indent}eval caused exception {an_exception}'
    else:  # no exception
        str        = f'{str}\n{indent}>>{eval_to}<<'
    # if msg is None:
    #     #msg  = f"Eval the string >{code}<"
    #     msg  = "Eval a string"
    # else:
    #     #msg  = f"Eval the string {msg} >{code}<"
    #     msg  = f"Eval a string: {msg}"

    if print_flag:
        print( str )
        # print( msg )
        # print( f"{code} =>" )
        # print( f">>{ret}<<" )

        # # work on this next more look at string instead of print
        # print( ">>", )
        # pprint.pprint( ret, )
        # print( "<<")

    # eval( eval_string )
    # next is not really useful, eval returns None ( at least in some cases )
    # this next does run the code again in eval_string
    #print(( eval_string, " ==> ", str( eval( eval_string )) ))
    # print( f"eval_string  ====>  {eval( eval_string)}" )

    return( str )


# ----------------------------------------
def print_eval( eval_string, msg = "Next eval the string", gl = None, lo = None  ):
    """
    show string and show its eval
    note may need to make objects in string global from caller
    """
    print( f"\n{ msg }: >>{eval_string}<<" )
    ret   = f"     >>{eval( eval_string, gl, lo )}<<end eval\n"
    #ret   = f"     >>{eval( eval_string, globals(), locals() )}<<end eval\n"
    #ret   = f"     >>{eval( eval_string, locals(), globals() )}<<end eval\n"

    print( ret  )


# ----------------------------------------
def eval_it( eval_string, msg = None ):
    """
    show a string and print what it evals to.
    ex_helpers.eval_it( something_to_eval, msg_defaults_to_None )
    use like this
    ex_helpers.print_eval( a_string, gl = globals(), lo = locals() )
    Args:
        eval_string (TYPE): DESCRIPTION.
        msg (TYPE, optional): DESCRIPTION. Defaults to None.

    Returns:
        None.

    """
    if msg is None:
        #msg  = f"Eval the string >{eval_string}<"
        msg  = "Eval the string"
    else:
        #msg  = f"Eval the string {msg} >{eval_string}<"
        msg  = f"Eval the string: {msg}"
    print( msg  )
    # eval( eval_string )
    # next is not really useful, eval returns None ( at least in some cases )
    # this next does run the code again in eval_string
    #print(( eval_string, " ==> ", str( eval( eval_string )) ))
    print( f"eval_string  ====>  {eval( eval_string)}" )

# ---------------------------------------- what
def ex_eval():
    print( """\n
    ================ ex_eval(): evaluation of a string as py code ===============
    """ )
    a_string = "print('hi there')"
    a_string = " 2 + 3"


    # # a_num seems to be out of scope
    a_num    = 2
    a_string = "a_num + 3"
    the_eval   = eval( a_string,   )
    #the_eval   = eval( a_string, {"a_num": a_num}, {"a_num": a_num} )
    print( the_eval )
    print_eval( a_string, msg = "custom", gl = globals(), lo = locals() )

    # x = 100  # A global variable
    # eval("x + 100", {"x": x})


    #eval_it( a_string )
    #print_eval( a_string )

#ex_eval()


# #--------------------------------
# if __name__ == "__main__":

#     a_obj = { "a": 1,"b": 2}
#     info_about_dict( a_obj, msg = "test for a dict:" )


#     #ex_helpers.info_about_obj( "a string" )
#     #print( a_dict )

#     # a_dict = {}     # empty dict
#     # ex_helpers.info_about_obj( a_dict )











