# -*- coding: utf-8 -*-

""""
This is a meta example file to explain the layout of others example files:

content explanations in {---- text ----}

{---- begin with a brief purpose of the file  and its status
     the following is taken from ex.string, then edited down ----}


Purpose:   String examples
           Some applies to other list like objects and itterables

Status: draft, ok draft but possibly useful

See Also:
    ex_f_string.py

{--- search section, suggest key words for fruitful search comments to right
     following from ex_string.py  ----}

Search for the following in the code below:

    def ex_        for the beginning of an example

    align
    backslash              r"\" is ng use "\\""
    begin                  ->> startswith
    ...

Reference:

    see ex_unicode.py for dealing with unicode conversion
    *>shell     D:/Russ/0000/python00/python3/_examples/ex_unicode.py

    #>>>>>python example string  see also for snipping and splitting
    #https://docs.python.org/2/library/string.html

    ...

"""

# {----  generally all imports at top ----}

import sys
import dis

import ex_helpers       # this has routines to help in showing examples

# {---- files may contain helper functions that help with the example
# but are not really part of them,
# an example here, not a particularly useful one does 
# helpers do not begin with ex_
# ----}

def foo():
    """
    a dummy helper function
    """
    return 42

# ----------------------------------------
# {---- ex_with_no_content follows, there is no content just standard starting
#   and ending code from ex_helpers which help identify console output
#   all examples begin with ex_
#   note that the name needs to be copied into the example in a few places
# ----}
# ----------------------------------------
def ex_with_no_content():
    ex_name  = "ex_with_no_content"   # {---- end with >>  ex_helpers.end_example( ex_name ) ----}
    print( f"""{ex_helpers.begin_example( ex_name )}
          room for more content
          """ )

    # {---- this example has no content, you would add it here
    # we will use the helper print_double_bar_sep()
    # ----}

    ex_helpers.end_example( ex_name )  #  {---- not part of example, marks end  ----}

#ex_with_no_content()    # {---- comment out this line to stop example from running ----}

# other things to do with an example
#eval( "ex_with_no_content()" )    # {---- run it -- may need to add locals or globals? ----}
#dis.dis( ex_with_no_content  )    # {---- disassemble it----}

#----------------------------------------
def ex_using_eval_and_print():
    ex_name  = "ex_using_eval_and_print"   # {---- end with >>  ex_helpers.end_example( ex_name ) ----}
    print( f"""{ex_helpers.begin_example( ex_name )}
          example using the helper function eval_and_print
          eval_and_print is widely used in examples so is good to understand
          """ )

    code_string  = "foo()"
    ret  = ex_helpers.eval_and_print( msg          = "code in a function is an expression so eval can run it a lot like exec",
                                      code         = code_string,
                                      as_locals    = None,
                                      as_globals   = globals(), )  # need globals() to get foo in scope

    ex_helpers.end_example( ex_name )  #  {---- not part of example, marks end  ----}

ex_using_eval_and_print()    # {---- comment out this line to stop example from running ----}

# other things to do with an example
#eval( "ex_using_eval_and_print()" )    # {---- run it -- may need to add locals or globals? ----}
#dis.dis( ex_using_eval_and_print  )    # {---- disassemble it----}

#----------------------------------------












