# -*- coding: utf-8 -*-


"""
Purpose:

    Examples of defining function and calling them
    Status: useful, but imcomplete
            ex_call_foo_positional is about the only example up to
            my current standards



Search for:

    def ex_     begins all examples

    *
    **
    call
    def
    dict
    positional
    partial
    return
    require     # require named arguments
    unpack

Links:

    (25) Brett Slatkin - How to Be More Effective with Functions - PyCon 2015 - YouTube
    *>url  https://www.youtube.com/watch?v=WjJUPxKB164&list=WL&index=88&t=220s

    Partial functions - Learn Python - Free Interactive Python Tutorial
        *>url  https://www.learnpython.org/en/Partial_functions

    Partial Functions in Python - GeeksforGeeks
        *>url  https://www.geeksforgeeks.org/partial-functions-python/

    Partial Functions in Python?
        *>url  https://www.tutorialspoint.com/partial-functions-in-python

    Python Partial Function Fun With Functools [ Updated ]
        *>url  https://mindmajix.com/python-partial-function

    Partial Application in Python. Deriving new functions with functools | by Martin McBride | The Startup | Medium
        *>url  https://medium.com/swlh/partial-application-in-python-7e9cbbbc959a

    functools — Higher-order functions and operations on callable objects — Python 3.9.6 documentation
        *>url  https://docs.python.org/3/library/functools.html

"""

import functools
from functools import partial

import ex_helpers



# ---- helpers
def foo_positional( argument_1, argument_2, argument_3 ):
    """
    retuns a string showing function ame and argument used in call

    *, makes following argument be required specify by name ( can use **dict )
    but can be called by position
    ie argumen_3 can be called by name

    """
    a_str      = ""
    a_str      = ( f"{a_str}foo was called with {argument_1}, {argument_2}, {argument_3}" )

    return a_str





def foo( argument_1, argument_2, *, argument_3 ):
    """
    retuns a string showing function ame and argument used in call

    *, makes following argument be required specify by name ( can use **dict )
    but can be called by position
    ie argumen_3 can be called by name

    """
    a_str      = ""
    a_str      = ( f"{a_str}foo was called with {argument_1}, {argument_2}, {argument_3}" )

    return a_str


def foo_required( argument_1, argument_2, *, argument_3 ):
    """
    retuns a string showing function ame and argument used in call

    *, makes following argument be required specify by name ( can use **dict )

    """
    a_str      = ""
    a_str      = ( f"{a_str}foo called with {argument_1}, {argument_2}, {argument_3}" )

    return a_str

# ----------------------------------------
def foo_named( argument_1 = 7,  argument_2 = 11 ):
    """
    documentation about the function here:

    Another version of foo, but named arguments and defaults for the arguments
    must be called with arguments by name, but arguments may be ommited.


    """
    print( f"foo_named called arguments are {argument_1}, {argument_2}" )
    print(  "foo_named will return 1")

    return 1

# ----------------------------------------
def foo_named( argument_1 = 7, argument_2 = 11 ):
    """
    documentation about the function here:

    Another version of foo, but named arguments and defaults for the arguments
    must be called with arguments by name, but arguments may be ommited.


    """
    print( f"foo_named called arguments are {argument_1}, {argument_2}" )
    print(  "foo_named will return 1")

    return 1


# ----------------------------------------
def fun_1( a, b, c = 0 ):
    """

    """
    print(( a, b, c ))

# ----------------------------------------
def fun_2( a, b, c = 0 ):
   a = a^2
   b = b^2
   c = 2
   return

# -------------------------helper/example

def fun_with_star( a, b, *values, joe = "joe"):
    """
    bring in variable number of values as a tuple
    joe named var with default must be after *values
    """
    print(( "from fun_with_star()", a, b, values, joe ))


# -------------------------helper/example
def fun_with_list( a, b1, b2, b3, joe = "joe"):
    """
    call this with * in caller to show unpacking
    """
    print(( "from fun_with_list()", a, b1, b2, b3, joe ))


# ----------------------------------------
def function_with_starstar( positional_arg, **kwargs ):
    """
    example function defined with **kwargs
    kwargs is a dictionay
    **kwargs may come after other args or not
    place_arg is an argument defined by it place in the arguments
    """
    print( "in function function_with_starstar")
    print( f"     positional_arg = {positional_arg}" )
    #print( argument_1 )  will be error
    print( "    ", kwargs )
    print( f"     kwargs are of type = {type( kwargs )}" )
    for key, val in kwargs.items():
            print( "    ", key, '->', val)


#---------- helper
def function_three_args( arg1, arg2, arg3 ):
    """
    an example fuction to make partial

    """
    print ( """
    -------------- function_three_args()    ---------------------
    """ )

    print( f"function_three_args args =  >>{arg1}<<, >>{arg2}<<  >>{arg3}<<)")


#function_three_args( "arg1aaa",  "arg2bbb", "arg3ccc", )

# -------------------------helper/example

def fun_with_keywords_required( *, a = 1, b = 1,  ):
    """
    call
    """
    print(( "fun_with_keywords_required()", a, b ))


# ----------------- helper
def value_from_digits( hundreds, tens, units ):
    """
    Purpose:
        a function to make partial
        read
    """
    return (100 * hundreds ) + ( 10 * tens ) + units



# ----------------------------------------
def ex_call_foo_positional():
    ex_name  = "ex_call_foo_positional"
    print( f"""{ex_helpers.begin_example( ex_name )}
            a very simple function with positional arguments
            all arguments may be called by position or name
    """ )
    print( "using eval_and_print for next examples --"
           "\n    all setup to all call eval_and_print() in basically the same way" )

    msg           = ( "1 this function returns a string documenting its call "
                      "\n    note: all positional arguments" )

    # ----
    code_string  =   "foo_positional( 'arg_val_1', 'arg_val_2', 'arg_val_3',  )"
    ret  = ex_helpers.eval_and_print( msg          = msg,
                                      code         = code_string,
                                      as_locals    = locals(),
                                      as_globals   = globals(), ) # globasl to define foo

    # ----
    msg          = ( "2 this function returns a string documenting its call"
                     "\n    note: 2 postitional arguments  one by name" )

    code_string  =   "foo_positional( 'arg_val_1', 'arg_val_2', argument_3 =  'arg_val_3' )"
    ret  = ex_helpers.eval_and_print( msg          = msg,
                                      code         = code_string,
                                      as_locals    = locals(),
                                      as_globals   = globals(), )

    # ----
    msg          = ( "3 this function returns a string documenting its call"
                     "\n    note: all by name out of order" )


    code_string  = ( 'foo_positional( argument_1 = "arg_val_1", '
                                     'argument_2 = "arg_val_2", '
                                     'argument_3 = "arg_val_3" )' )

    ret  = ex_helpers.eval_and_print( msg          = msg,
                                      code         = code_string,
                                      as_locals    = locals(),
                                      as_globals   = globals(), )

    # ----
    msg          = ( "4 this function returns a string documenting its call"
                     "\n    note: 2 postitional arguments one by name in a dict" )

    a_dict       = { "argument_3": "arg_dict_val_3"  }
    code_string  =   'foo_positional( "arg_val_1", "arg_val_2", **a_dict )'
    ret  = ex_helpers.eval_and_print( msg          = msg,
                                      code         = code_string,
                                      as_locals    = locals(),
                                      as_globals   = globals(), )
    # ----
    msg          = ( "5 this function returns a string documenting its call"
                     "\n    note: all in a dict, not in order"  )

    a_dict       = { "argument_3": "arg_val_3",   "argument_2": "arg_dict_val_2",  "argument_1": "arg_dict_val_1" }
    code_string  =   'foo_positional( **a_dict )'
    ret          = ex_helpers.eval_and_print( msg  = msg,
                                      code         = code_string,
                                      as_locals    = locals(),
                                      as_globals   = globals(), )

    # ----
    msg          = ( "6 this function returns a string documenting its call"
                     "\n    note: all in a dict, not in order, extra dict entry"  )

    a_dict       = { "argument_3": "arg_val_3",      "argument_2": "arg_dict_val_2",
                     "argument_1": "arg_dict_val_1", "argument_x": "arg_dict_val_x" }
    code_string  =   'foo_positional( **a_dict )'
    ret          = ex_helpers.eval_and_print( msg  = msg,
                                      code         = code_string,
                                      as_locals    = locals(),
                                      as_globals   = globals(), )


    ex_helpers.end_example( ex_name )

#ex_call_foo_positional()

# ----------------------------------------
def ex_call_foo_positional_2():
    ex_name  = "ex_call_foo_positional_2"
    print( f"""{ex_helpers.begin_example( ex_name )}
            repeat of some of ex_call_foo_positional not using eval_and_print
            a very simple function with positional arguments
            all arguments may be called by position or name

    """ )
    print( "\nuse try except for next examples: ( check msg matches code )\n" )

    # ----
    print()
    msg    = '1 foo_positional( "arg_val_1", "arg_val_2", "arg_val_3" )'
    print( msg )
    try:
        ret   = foo_positional( "arg_val_1", "arg_val_2", "arg_val_3" )
        print( f"   foo_positional() returned >{ret}<" )
    except:
        print( "    foo_positional call caused exception" )

    # ----
    print()
    msg    = '2 about to call foo_positional( "arg_val_1", "arg_val_2", argument_3 = "arg_dict_val_3" )'
    print( msg )
    ret   = foo_positional( "arg_val_1", "arg_val_2", argument_3 = "arg_dict_val_2" )
    print( f"    foo_positional() returned >{ret}<" )


# ----
    print()
    a_dict   = { "argument_3": "arg_dict_val_3" }
    msg      = '3 about to call foo_positional() with a **dict: foo_positional( "arg_val_1", "arg_val_2", **a_dict )'
    print( msg )
    ret   = foo_positional( "arg_val_1", "arg_val_2", **a_dict )
    print( f"    foo_positional() returned >{ret}<" )

    ex_helpers.end_example( ex_name )

ex_call_foo_positional_2()





# ----------------------------------------
def ex_call_foo():
    ex_name  = "ex_call_foo"
    print( f"""{ex_helpers.begin_example( ex_name )}
            a very simple function
            require call by name
    """ )

    print( "using eval_and_print for next examples" )
    code_string  =   "foo( 7, 11, 12 )"
    ret  = ex_helpers.eval_and_print( msg          = "this function returns a string documenting its call"
                                                     "\n    note: all positional",
                                      code         = code_string,
                                      as_locals    = None,
                                      as_globals   = globals(), ) # globasl to define foo



    code_string  =   "foo( 7, 11, argument_3 = 12 )"
    ret  = ex_helpers.eval_and_print( msg          = "this function returns a string documenting its call"
                                                     "\n    note: 2 postitional one by name"
                                                     " ",
                                      code         = code_string,
                                      as_locals    = None,
                                      as_globals   = globals(), ) # globasl to define foo



    print( "\nuse try except for next examples: ( check msg matches code )\n" )
    msg    = "about to call foo( 7, 11, argument_3 = 12"
    print( msg )
    ret   = foo( 7, 11, argument_3 = 12 )
    print( f"    returned >{ret}<" )

    print()
    msg    = "about to call foo( 7, 11, 12 )"
    print( msg )
    try:
        ret   = foo( 7, 11, 12 )
        print( f"   foo() returned >{ret}<" )
    except:
        print( "    call caused exception" )

    print()
    a_dict   = { "argument_3": 12 }
    msg      = "about to call foo() with a **dict: foo( 7, 11, **a_dict ) "
    print( msg )
    ret   = foo( 7, 11, **a_dict )
    print( f"    foo() returned >{ret}<" )

    ex_helpers.end_example( ex_name )

#ex_call_foo()


# ----------------------------------------
def ex_call_foo_named():
    ex_name  = "ex_call_foo_named"
    print( f"""{ex_helpers.begin_example( ex_name )}
    a very simple function with named arguments

    """ )
    print( "about to call foo_named() several different ways ")
    ret   = foo_named( 7, 11 )
    print( f"foo_named() returned {ret}" )

    # ret   = foo_named( argument_1 = 7, 11 )  # will throw error, once you start with named arguments keep it up
    # print( f"foo_named() returned {ret}" )

    ret   = foo_named( argument_1 = 7, argument_2 = 11 )
    print( f"foo_named() returned {ret}" )

    ret   = foo_named( argument_1 = 7,  )      # but arguments can be ommited, they default
    print( f"foo_named() returned {ret}" )

    ret   = foo_named( argument_2 = 11,  argument_1 = 7 )  # named argument can be called out of order
    print( f"foo_named() returned {ret}" )

    ex_helpers.end_example( ex_name )

#ex_call_foo_named()

# ----------------------------------------
def foo_documented(  ):
    """
    Purpose:
        This is a function .. showing possible way to document
        What it says, read
        I rairly see this much on github
        In my opinion the purpose is the most important part of the doc
    Args:
        n: the number to get the square root of.
    Returns:
        the ultimate answere to...
        mutates something
    Raises:
        TypeError: if n is not a number.
        ValueError: if n is negative.

    """

    return 42


# help( foo_documented )     # a way to read the documentation
# help( foo_documented() )   # get help but probably not what you want





# ----------------------------------------
def ex_call_with_keywords():
    ex_name  = "ex_call_with_keywords"   # end with >>    ex_helpers.end_example( ex_name )  # not part of example, marks end
    print( f"""{ex_helpers.begin_example( ex_name )}

    """ )

    fun_with_keywords_required( 1, 4,  )

    fun_with_keywords_required( 1, b=4,  )

    fun_with_keywords_required( a=1, b=4,  )

    fun_with_keywords_required(  b=4, a=1, )

#    fun_with_keywords_required( 1, 4,  ) # error
#
#    fun_with_keywords_required( 1, b=4,  ) # error

    fun_with_keywords_required( a=1, b=4,  )

    fun_with_keywords_required(  b=4, a=1, )

    ex_helpers.end_example( ex_name )

#ex_call_with_keywords()




# ----------------------------------------
def ex_function_with_star():
    ex_name  = "ex_function_with_star"
    print( f"""{ex_helpers.begin_example( ex_name )}
    """ )
    fun_with_star( 1, b=4,  )

#    fun_with_star( 1, b = 4, values = 6 ) # error: unexpected keyword

#    fun_with_star( 1, b = 4,  6 ) # error: positional after keyword
    fun_with_star( 1,     4,  6 ) # ok

    fun_with_star( 1,     4,  ( 6, 7 ) ) # ok but not right
    fun_with_star( 1,     4,  [ 6, 7 ] ) # ok but not right
    fun_with_star( 1,     4,  6, 7, 8, ) # ok this may be the right way

    ex_helpers.end_example( ex_name )

#ex_function_with_star()

# ----------------------------------------
def ex_call_with_star():
    ex_name  = "ex_call_with_star"
    print( f"""{ex_helpers.begin_example( ex_name )}
    beware using a generator instead of set, list, unless finite enough
    """ )
    fun_with_star( 1, b=4,  )

    fun_with_list( 1,     4,  *( "one", "two", "three" ) ) #
    fun_with_list( 1,     4,  *[ "one", "two", "three" ] ) #
    fun_with_list( 1,     4,  *range( 1, 3 ) ) #
    fun_with_list( 1,     4,  *( "one", "two",   ) ) # ok! b3 just fails to unpack
#    fun_with_list( 1,     4,  [ 6, 7 ] ) #
#    fun_with_list( 1,     4,  6, 7, 8, ) #
    ex_helpers.end_example( ex_name )

#ex_call_with_star()




# ----------------------------------------
def ex_call_with_function_with_starstar():
    ex_name  = "ex_call_with_function_with_starstar"   # end with >>    ex_helpers.end_example( ex_name )  # not part of example, marks end
    print( f"""{ex_helpers.begin_example( ex_name )}
            both define and call use the ** syntax
    """ )

    a_dict   = { "argument_1": "argument_1_value",
                 "argument_2": "argument_2_value",
                 "argument_3": "argument_3_value" }

    function_with_starstar( "positional_arg_value", **a_dict )

    ex_helpers.end_example( ex_name )   # standard end to example


#ex_call_with_function_with_starstar()







#-------------------
def ex_create_partial():
    ex_name  = "ex_create_partial"   # end with >>    ex_helpers.end_example( ex_name )  # not part of example, marks end
    print( f"""{ex_helpers.begin_example( ex_name )}
           create partial functions from other functions
    """ )

    # create a new function that multiplies by 2
    a_partial_foo       = functools.partial( value_from_digits, 3 )  # will set first arg
    print( f"partial function: a_partial_foo( 2, 1  ) {a_partial_foo( 2, 1  )}" )


    # #function_three_args( arg1, arg2, arg3

    # a_partial_foo  = functools.partial(function_three_args, arg2 = "replace arg2" )
    # a_partial_foo( arg1 = "explicit", arg3 = "arg2 exp" )

    # a_partial_foo     = functools.partial(function_three_args, arg3 = "replace arg3" )
    # a_partial_foo( arg1 = "explicit arg1", arg2 = "arg2 exp" )


    # set up a partial function
    value_from_hundreds = partial( value_from_digits, units = 2, tens = 1 )
    # call
    print( f"partial function: value_from_hundreds(3) >{value_from_hundreds(3)}<" )

    # # set up a partial function
    # value_from_tens = partial( value_from_digits, hundreds = 3, units = 6 )
    # # call
    # print( f"partial function: value_from_tens(9) >{value_from_tens(9)}<" )

    # set up a partial function
    value_from_tens = partial( value_from_digits, hundreds = 3, units = 6 )
    # call
    print( f"partial function: value_from_tens(tens = 9) >{value_from_tens( tens =9)}<" )



    ex_helpers.eval_and_print( msg   = "define a partial function",
                        code         = "value_from_tens = value_from_digits(1,2,3) ",
                        as_locals    = locals(),   # locals() # normally locals()
                        as_globals   = None,
                        print_flag   = True )



    ex_helpers.end_example( ex_name )


#ex_create_partial()













