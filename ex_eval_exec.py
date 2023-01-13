# -*- coding: utf-8 -*-

""""
Purpose:
    Examples of eval and exec

    these are used in ex_helpers.eval_and_print()
    and ex_helpers.exec_and_print()
    and that code should be considered part of these examples
    when they are called


Search:
    def ex_       for any example

    eval          evaluates and returns the value of an expression
    exec          runs code but returns nothing

    globals
    locals

Ref:

    really good tutorial, with more arguments

    Python eval(): Evaluate Expressions Dynamically – Real Python
    *>url https://realpython.com/python-eval-function/#the-first-argument-expression

    Ned Batchelder: Eval really is dangerous
    *>url https://nedbatchelder.com/blog/201206/eval_really_is_dangerous.html

    http://effbot.org/zone/librarybook-core-eval.htm
    look at this may be used in cad, is used in smart terminal to allow function specification for late autostart
    *>url http://lybniz2.sourceforge.net/safeeval.html

    a_dict   with variable names as strings for keys

"""

import ex_helpers

# ----------------------------------------
def ex_eval_exec():
    ex_name  = "ex_eval_exec"     # end with >>  ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )}
           simple example of eval and exec without use of helpers

    """)
    print( "eval evaluates expressions...")
    result = eval( " 10 + 20"  )
    print( f"Result of eval of 10 + 20 is >{result}<")

    print( "\nexec executes code")
    result = exec( "10 + 20"  )
    print( f"Result of exec of 10 + 20 is >{result}< -- exec does not return a result" )

    ex_helpers.end_example( ex_name )

#ex_eval_exec()

# ----------------------------------------
def ex_eval_exec_with_helpers():
    ex_name  = "ex_eval_exec_with_helpers"
    print( f"""{ex_helpers.begin_example( ex_name )}
           a repeat of above with ex_helper. functions

    """)
    code_string  =   "10 + 20"
    ret  = ex_helpers.eval_and_print( msg          = "eval with no globals or locals",
                                      code         = code_string,
                                      as_locals    = None,
                                      as_globals   = None, )

    code_string  =   "10 + 20"
    ret  = ex_helpers.exec_and_print( msg          = "exec with no globals or locals -- no result ",
                                      code         = code_string,
                                      as_locals    = None,
                                      as_globals   = None, )

    # we get a return here, a tuple, not sure it is useful
    # uncomment if you wish
    print( f"\nexec_and_print() returned {ret}" )

    ex_helpers.end_example( ex_name )

#ex_eval_exec_with_helpers()

# ----------------------------------------
def ex_eval_locals():
    ex_name  = "ex_eval_locals"     # end with >>  ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )}
           show how locals might be used

    """)
    code_string  =   "10 + 20"
    ret  = ex_helpers.eval_and_print( msg          = "eval with no globals or locals is fine",
                                      code         = code_string,
                                      as_locals    = None,
                                      as_globals   = None, )

    x            = 10
    code_string  = "x + 20"
    ret  = ex_helpers.exec_and_print( msg          = "eval with no globals or locals - x will be undefined ",
                                      code         = code_string,
                                      as_locals    = None,
                                      as_globals   = None, )

    x            = 10
    code_string  = "x + 20"
    ret  = ex_helpers.eval_and_print( msg          = "eval with locals() - x will now defined ",
                                      code         = code_string,
                                      as_locals    = locals(),
                                      as_globals   = None, )

    code_string  = "x = 10 + 20"
    ret  = ex_helpers.eval_and_print( msg          = "eval does not allow assignment use exec instead",
                                      code         = code_string,
                                      as_locals    = None,
                                      as_globals   = None, )

    ex_helpers.end_example( ex_name )

#ex_eval_locals()


# ----------------------------------------
def ex_exec_locals():
    ex_name  = "ex_exec_locals"     # end with >>  ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )}
           similar to ex_eval_locals() but with exec, no return values

    """)
    code_string  =   "print( 10 + 20 )"
    ret  = ex_helpers.exec_and_print( msg          = "exec with no globals or locals is fine",
                                      code         = code_string,
                                      as_locals    = None,
                                      as_globals   = None, )

    x            = 10
    code_string  = "x + 20"
    ret  = ex_helpers.exec_and_print( msg          = "exec with no globals or locals - x will be undefined ",
                                      code         = code_string,
                                      as_locals    = None,
                                      as_globals   = None, )

    x            = 10
    code_string  = "x + 20"
    ret  = ex_helpers.exec_and_print( msg          = "exec with locals() - x will now defined ",
                                      code         = code_string,
                                      as_locals    = locals(),
                                      as_globals   = None, )

    code_string  = "x = 10 + 20"
    ret  = ex_helpers.exec_and_print( msg          = "exec does allow assignment unlike eval",
                                      code         = code_string,
                                      as_locals    = None,
                                      as_globals   = None, )

    ex_helpers.end_example( ex_name )

#ex_exec_locals()

# ----------------------------------------
def foo( ):
    """
    Purpose:
        helper function can contain any code

    """
    print( "my name is foo \n   I return 42" )
    return 42

# ----------------------------------------
def ex_more_eval():
    ex_name  = "ex_more_eval"     # end with >>  ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )}
           more eval examples

    """)
    print( "====" )  # marker for example
    code_string  =   "print( 10 + 20 )"
    ret  = ex_helpers.eval_and_print( msg          = "eval can print, if you wish, probably not useful with eval_and_print()"
                                                     "\n    note that output is 'above' the call to eval_and_print",
                                      code         = code_string,
                                      as_locals    = None,
                                      as_globals   = None, )
    print( "----" )  # end marker for example

    x            = 10
    locals_dict  = { "y": 30 }
    code_string  = "y + 20"
    ret  = ex_helpers.eval_and_print( msg          = "eval can uses any dict as a locals dict",
                                      code         = code_string,
                                      as_locals    = locals_dict,
                                      as_globals   = None, )

    x            = 10
    locals_dict  = { "x": 30 }
    code_string  = "x + 20"
    ret  = ex_helpers.eval_and_print( msg          = "eval with locals() - x will now defined but not our local",
                                      code         = code_string,
                                      as_locals    = locals(),
                                      as_globals   = None, )


    code_string  = "foo()"
    ret  = ex_helpers.eval_and_print( msg          = "code in a function is an expression so eval can run it a lot like exec",
                                      code         = code_string,
                                      as_locals    = None,
                                      as_globals   = globals(), )  # need globals() to get foo in scope

    ex_helpers.end_example( ex_name )

ex_more_eval()

# ----------------------------------------
def ex_more_exec():
    ex_name  = "ex_more_exec"
    print( f"""{ex_helpers.begin_example( ex_name )}
           similar to ex_more_eval() but with exec, no return values
           we can use locals to get 'return' values

    """)
    code_string  =   "print( 10 + 20 )"
    ret  = ex_helpers.exec_and_print( msg          = "exec can print, if you wish, probably not useful with eval_and_print()",
                                      code         = code_string,
                                      as_locals    = None,
                                      as_globals   = None, )

    x            = 10
    code_string  = "x = 10 + 20"
    ret  = ex_helpers.exec_and_print( msg          = "exec with locals() - x (an imutable) will now defined ",
                                      code         = code_string,
                                      as_locals    = locals(),
                                      as_globals   = None, )
    print( f"    x is now >{x}< unchanged")



    x            = 10
    code_string  = "x = 10 + 20;x=1 + 2;print(x)"
    ret  = ex_helpers.exec_and_print( msg          = "exec with multiple lines is fine",
                                      code         = code_string,
                                      as_locals    = locals(),
                                      as_globals   = None, )

    x            = 10
    some_locals  = locals()
    code_string  = "x = 10 + 20"
    ret  = ex_helpers.exec_and_print( msg          = "exec with locals() - x (an imutable) will now defined we will recover it",
                                      code         = code_string,
                                      as_locals    = some_locals,
                                      as_globals   = None, )
    print( "    recover x from the some_locals dict..." )
    x    = some_locals[ "x" ]
    print( f"    x is now >{x}< changed")

    x            = [10]
    code_string  = "x.append( 30 )"
    ret  = ex_helpers.exec_and_print( msg          = "exec with locals() - x (an imutable) will now defined we will recover it",
                                      code         = code_string,
                                      as_locals    = locals(),
                                      as_globals   = None, )
    print( "    recover x as a mutable need not explicitly pull from a dict" )
    print( f"   x is now >{x}< changed")


    a_list            = [10]
    code_string  = "a_list.append( 20 )\na_list.append( 30 )\na_list.append( 40 )"
    ret  = ex_helpers.exec_and_print( msg          = "exec with multiple 'lines' using a new line",
                                      code         = code_string,
                                      as_locals    = locals(),
                                      as_globals   = None, )
    print( f"    a_list is now >{a_list}<")

    a_list            = [10]
    code_string  = "a_list.append( 20 );a_list.append( 30 );a_list.append( 40 )"
    ret  = ex_helpers.exec_and_print( msg          = "exec with multiple 'lines' using a ;",
                                      code         = code_string,
                                      as_locals    = locals(),
                                      as_globals   = None, )
    print( f"    a_list is now >{a_list}<")

    ex_helpers.end_example( ex_name )

#ex_more_exec()







