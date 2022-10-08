# -*- coding: utf-8 -*-

""""
This is a meta example file to explain the layout of example files:
some content taken from a version of ex_string.py

content explanations in { ---- text ----}

{--- begin with a brief purpose of the file  and its status ex: ----}

What:
    String examples
Status:
    draft, ok draft but possibly useful

{--- search section, suggest key words for fruitful search comments to right
     following from ex_string.py but examples are imcomplete ----}


Search for the following in the code below:
    Some applies to other lists and itterables

    align
    backslash                r"\" is ng use "\\""
    concatination            use join not a loop or f_strings
    ends






"""




# { ----  generally all imports at top ---- }

import sys
import dis


import ex_helpers       # this has rouines to help in showing examples


# {---- files may contain helper functions that help with the example
# but are not really part of them,
# an eample here, not a particularlly useful one does not begin with ex_
# ----}

# ---- helper function
def print_double_bar_sep( ):
    """
    helpers should have some minimal doc string

    prints a "double bar" across output
    read it
    """
    print( "\n" + 50 * "=" + "\n")

# ----------------------------------------
# {---- ex_with_no_content follows, there is no content just standard starting
#   and ending code from ex_helpers which help identify console output
#    all examples begin with ex_
# ----}
# ----------------------------------------
def ex_with_no_content():
    ex_name  = "ex_copy_no_content"   # end with >>    ex_helpers.end_example( ex_name )  # not part of example, marks end
    print( f"""{ex_helpers.begin_example( ex_name )}
          room for more content
          """ )

    # {---- this has no content, you would add it here
    # we will use the helper print_double_bar_sep()
    # ----}

    print_double_bar_sep()

    ex_helpers.end_example( ex_name )  # not part of example, marks end

ex_with_no_content()    # comment out this line to stop example from running

#eval( f"{ex_name}()" )         # run it
#dis.dis( eval( ex_name ) )    # disassemble it

#----------------------------------------

# ----------------------------------------
def ex_with_no_content2():
    ex_name  = "ex_with_no_content2"
    print( f"""{ex_helpers.begin_example( ex_name )}
          ...
          """ )
    ex_helpers.end_example( ex_name )

ex_with_no_content()    # comment out this line to stop example from running

#eval( f"{ex_name}()" )         # run it
#dis.dis( eval( ex_name ) )    # disassemble it

#----------------------------------------












