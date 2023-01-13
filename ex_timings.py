# -*- coding: utf-8 -*-
#>>>>>python example timing of different code for speed differences or just timing
"""
Purpose:   Example timing of different code for speed differences
           purpose is not so much to have you run the fastest
           but often to show what you think is fastest is not, or
           only faster by a small amount.
           Often the faster is actually better in other respects
           in addition to speed

Status: seems to offer some useful info.

See Also:
    ex_helpers.py

Search for the following in the code below:

    def ex_          begins all examples

    call
    code timer
    cProfile
    codetimer
    dict
    else
    except
    if
    inline
    local variable
    perf_counter
    Profile
    sort
    time
    try

References:

    Python Code Optimization Tips and Tricks You Should Know
        *>url  https://www.techbeamers.com/python-code-optimization-tips-tricks/#h1

    Mike Müller - Faster Python Programs - Measure, don't Guess - PyCon 2019 - YouTube
        *>url  https://www.youtube.com/watch?reload=9&v=EcGWDNlGTNg

Note:
    Sometimes running the code again gives different results so some examples run the
    same code more than once.

"""

import datetime
import time
import sys
import timeit
import cProfile

import ex_helpers

# ------------------- helpers
class TestClass(  ):
    """
    simple class for testing, read
    """
    def func( self ,x ):
        tot   = x + x
        #print( x + x )
        return tot

    def func_1( self ,x ):
        tot   = x + x
        return tot

    def func_2( self ,x ):
        tot   = x + x
        return tot

    def __init__( self ):
        self.instance_var   = 37

# ----------------------------------------
def function_0( x ):
    tot   = x + x
    return tot

def function_1( x ):
    tot   = x + x
    return tot

def function_2( x ):
    tot   = x + x
    return tot

def function_3( x ):
    tot   = x + x
    return tot

# ---- Begin examples
# ----------------------------------------
def ex_dict_dispatch():
    ex_name  = "ex_dict_dispatch"
    print( f"""{ex_helpers.begin_example( ex_name )}
    compare switch case like statement based on a dict with on based on if elif
    Last test: dispatch dict is the faster method
    """)

    dispactch_cases   = [ "zero", "one",   "two", "three",
                          "zero", "one",   "two", "three",
                          "zero", "one",   "two", "three",
                          "zero", "one",   "two", "three",      ]

    dispatch_dict  = { "zero":  function_0,  "one":   function_1,
                        "two":  function_2,  "three": function_3,  }

    a_code_timer = ex_helpers.CodeTimer()

    a_code_timer.start( "Switch implemented with if, elif" )

    for a_case in dispactch_cases:

        if   a_case == "zero":
            function_0(0)
        elif a_case == "one":
            function_1(1)
        elif a_case == "two":
            function_2(2)
        elif a_case == "three":
            function_3(3)

    a_code_timer.stop()

    a_code_timer.start( "Switch implemented with dispatch dict" )

    for a_case in dispactch_cases:

        dispatch_dict[ a_case ]

    a_code_timer.stop()

    a_code_timer.start( "Switch implemented with if, elif repeated" )

    for a_case in dispactch_cases:

        if   a_case == "zero":
            function_0(0)
        elif a_case == "one":
            function_1(1)
        elif a_case == "two":
            function_2(2)
        elif a_case == "three":
            function_3(3)

    a_code_timer.stop()

    a_code_timer.report()

    ex_helpers.end_example( ex_name )   

#ex_dict_dispatch()              # run it
#eval( "ex_dict_dispatch()" )    # run it with eval
#dis.dis( ex_dict_dispatch  )    # disassemble it

# ----------------------------------------
def ex_call_or_inline():
    ex_name  = "ex_call_or_inline"    
    print( f"""{ex_helpers.begin_example( ex_name )}
    call seems about 4 times as expensive as add of 2 ints inline
    """)
    loop_max   = 10000

    a_code_timer = ex_helpers.CodeTimer()

    a_code_timer.start( "Call 0" )

    for i in range( loop_max ):
        function_0( i )

    a_code_timer.stop(   )

    # ----
    a_code_timer.start( "Inline" )

    for i in range( loop_max ):
        tot   = 1 + 1

    a_code_timer.stop(   )

    # # ----
    # a_code_timer.start( "With Module Variable" )

    # for i in range( loop_max ):
    #     function_1( i ) #

    # a_code_timer.stop(   )

    a_code_timer.start( "Call 1" )

    for i in range( loop_max ):
        function_0( i )

    a_code_timer.stop(   )

    a_code_timer.report(   )

    ex_helpers.end_example( ex_name )

#ex_call_or_inline()

# ----------------------------------------
def ex_mod_or_count():
    ex_name  = "ex_mod_or_count"    
    print( f"""{ex_helpers.begin_example( ex_name )}
    in a loop we can use a counter instead of modulo which involves
    the expensive operation of division
    a function is called every modulo times through the loop
    which is faster?  Last test: modulo wins!
    """)
    loop_max   = 1000
    modulo     = 3

    a_code_timer = ex_helpers.CodeTimer()

    a_code_timer.start( "Count 0" )

    ix  = 0
    for i in range( loop_max ):

        if  ix == modulo:
            ix =  0
            function_0( i )
        ix += 1

    a_code_timer.stop(   )

    # ----
    a_code_timer.start( "Modulo 0" )

    for i in range( loop_max ):

        if  i % modulo == 0: #not quite the same bu still every modulo
            function_0( i )

    a_code_timer.stop(   )

    a_code_timer.start( "Count 0 again" )

    ix  = 0
    for i in range( loop_max ):

        if  ix == modulo:
            ix =  0
            function_0( i )
        ix += 1

    a_code_timer.stop(   )

    a_code_timer.report(   )

    ex_helpers.end_example( ex_name )

#ex_mod_or_count()

# ----------------------------------------
def ex_if_or_else():
    ex_name  = "ex_if_or_else"   
    print( f"""{ex_helpers.begin_example( ex_name )}
    question: is the if case or else case faster?
    Last test: mostly else !!
    """)
    loop_max   = 100000
    modulo     = 27

    a_code_timer = ex_helpers.CodeTimer()

    a_code_timer.start( "Mostly else is executed" )

    for i in range( loop_max ):

        if  i % modulo == 0:
            function_0( i )
        else:
            function_0( i )

    a_code_timer.stop(   )

    # ----
    a_code_timer.start( "Mostly if is executed" )

    for i in range( loop_max ):

        if  i % modulo != 0:
            function_0( i )

        else:
            function_0( i )

    a_code_timer.stop(   )

    a_code_timer.report(   )

    ex_helpers.end_example( ex_name )

#ex_if_or_else()

# ----------------------------------------
def ex_local_var():
    ex_name  = "ex_local_var"    
    print( f"""{ex_helpers.begin_example( ex_name )}
    compare local variable use to class instance variable
    here the variable is a function
    Which is faster: a local variable or a class instance
    Last test: Local variables win
    """)
    # Declaring variable that assigns class method object
    a_test_class    = TestClass()
    test_fun        = a_test_class.func # Declaring local variable

    loop_max        = 1000

    a_code_timer    = ex_helpers.CodeTimer()

    a_code_timer.start( "With Local Variable" )

    for i in range( loop_max ):
        test_fun( i ) # faster than Obj.func(i) ?

    a_code_timer.stop(   )

    # ----
    a_code_timer.start( "With Class Instance Variable" )

    for i in range( loop_max ):
        a_test_class.func( i ) # faster than Obj.func(i)

    a_code_timer.stop(   )

    # ----
    a_code_timer.start( "With Module Variable" )

    for i in range( loop_max ):
        function_1( i ) #

    a_code_timer.stop(   )

    a_code_timer.report(   )

    ex_helpers.end_example( ex_name )

#ex_local_var()

# ----------------------------------------
def ex_local_var_2():
    ex_name  = "ex_local_var_2"    
    print( f"""{ex_helpers.begin_example( ex_name )}
    compare local variable use to class instance variable
    here the variable is a function
    """)
    # Declaring variable that assigns class method object
    a_test_class    = TestClass()
    test_fun        = a_test_class.func # Declaring local variable

    loop_max   = 1000

    a_code_timer = ex_helpers.CodeTimer()

    a_code_timer.start( "With Local Variable" )

    local_var  = a_test_class.instance_var
    for i in range( loop_max ):
         x  = 2 * local_var

    a_code_timer.stop(   )

    # ----
    a_code_timer.start( "With Class Instance Variable" )

    for i in range( loop_max ):
        x  = 2 * a_test_class.instance_var

    a_code_timer.stop(   )


    a_code_timer.start( "With Class Instance Variable" )

    for i in range( loop_max ):
        local_var  = a_test_class.instance_var

        x  = 2 * local_var
        x  = 2 * local_var
        x  = 2 * local_var

    for i in range( loop_max ):

        x  = 2 * a_test_class.instance_var
        x  = 2 * a_test_class.instance_var
        x  = 2 * a_test_class.instance_var

    a_code_timer.stop(   )

    # # ----
    # a_code_timer.start( "With Module Variable" )

    # for i in range( loop_max ):
    #     function_1( i ) #

    # a_code_timer.stop(   )

    a_code_timer.report(   )

    ex_helpers.end_example( ex_name )

#ex_local_var_2()

# ----------------------------------------
def ex_local_var_3():
    ex_name  = "ex_local_var_3"    
    print( f"""{ex_helpers.begin_example( ex_name )}
    compare local variable use to class instance variable -- just a few uses
    last test showed even 2 uses makes it useful to go local

    """)
    # Declaring variable that assigns class method object

    use_max         = 2
    a_test_class    = TestClass()
    test_fun        = a_test_class.func # Declaring local variable

    loop_max        = 1000

    a_code_timer = ex_helpers.CodeTimer()

    a_code_timer.start( "With Local Variable" )
    for i in range( loop_max ):
        local_var  = a_test_class.instance_var
        for j in range( use_max ):
            x          = 2 * local_var
    a_code_timer.stop()

    # ----
    a_code_timer.start( "With Class Instance Variable" )
    for i in range( loop_max ):
        for j in range( use_max ):
            x  = 2 * a_test_class.instance_var

    a_code_timer.stop()

    a_code_timer.report(   )

    ex_helpers.end_example( ex_name )

#ex_local_var_3()

# ----------------------------------------
def ex_try():
    ex_name  = "ex_try"    
    print( f"""{ex_helpers.begin_example( ex_name )}

    Question: how expensive is try catch
    Last test: try is not expensive
    Note that Without try ver 1 at end runs faster than same code ( ver 0 ) it suggests some cashing is going on.
    """)
    loop_max   = 10
    a_code_timer = ex_helpers.CodeTimer()

    for i in range( loop_max ):
        squ   = i*i

    # ---- no try
    a_code_timer.start( "Without try ver 0" )

    for i in range( loop_max ):
        squ   = i*i

    a_code_timer.stop(   )

    # ----  try
    a_code_timer.start( "With try ver 0" )

    try:
        for i in range( loop_max ):
            squ   = i*i

    except Exception as an_exception:
        print( an_exception )

    a_code_timer.stop(   )

    # ---- no try
    a_code_timer.start( "Without try ver 1" )

    for i in range( loop_max ):
        squ   = i*i

    a_code_timer.stop(   )

    # ----  try
    a_code_timer.start( "With try ver 2" )

    try:
        for i in range( loop_max ):
            squ   = i*i

    except Exception as an_exception:
        print( an_exception )

    a_code_timer.stop(   )

    # ---- no try
    a_code_timer.start( "Without try ver 0 repeat" )

    for i in range( loop_max ):
        squ   = i*i

    a_code_timer.stop(   )

    # ----
    a_code_timer.report(   )

    ex_helpers.end_example( ex_name )

#ex_try()

# ----------------------------------------
def ex_time_some_code():
    ex_name  = "ex_time_some_code"   
    print( f"""{ex_helpers.begin_example( ex_name )}
    bunch of conversions from web  good: keep
    see also  ex_dicct_dispach
    """ )
    # code_timer
    code_timer      = ex_helpers.CodeTimer()
    msg             = f"\nfor {loop_max} itterations code took - using CodeTimer"

    timestamp       = 1226527167.595983
    loop_max        = int( 1e5 )

    code_timer.start(  )
    for ix in range( 1, loop_max  ):

          time_tuple = time.gmtime( timestamp )

    code_timer.stop()

    code_timer.report()

    ex_helpers.end_example( ex_name )

#ex_time_some_code()

# ----------------------------------------
def ex_built_in_map():
    ex_name  = "ex_built_in_map"    
    print( f"""{ex_helpers.begin_example( ex_name )}
    not a great example because of course append is a slow way, compare instead to list comp
    """)
    # Python program to illustrate library functions
    # save time while coding with the example of map()

    # slower (Without map())
    start = time.clock()
    s = 'geeks'
    U = []
    for c in s:
        U.append(c.upper())
    print( U )
    elapsed = time.clock()
    e1 = elapsed - start
    print( "Time spent in function is: ", e1 )

    # Faster (Uses builtin function map())
    s = 'geeks'
    start = time.clock()
    U = map(str.upper, s)
    print( U )
    elapsed = time.clock()
    e2 = elapsed - start
    print( "Time spent in builtin function is: ", e2 )

    ex_helpers.end_example( ex_name )

#ex_built_in_map()

# ----------------------------------------
def ex_sort():
    ex_name  = "ex_sort"    
    print( f"""{ex_helpers.begin_example( ex_name )}
          looks like unfinished
          should be in some other examaple like ex_lists.py?
    """)
    # Python program to illustrate
    # using keys for sorting
    somelist = [1, -3, 6, 11, 5]
    somelist.sort()
    print( somelist )

    s = 'geeks'
    # use sorted() if you don't want to sort in-place:
    s = sorted(s)
    print( s )

    ex_helpers.end_example( ex_name )

#ex_sort()

# ----------------------------------------
def ex_idiomatic():
    ex_name  = "ex_idiomatic"    
    print( f"""{ex_helpers.begin_example( ex_name )}
    misc examples, without comparison
    probably should be finished if you are interested
    """)
    # Python program to illustrate using
    # optimized loops for faster coding

    # slow O(n^2) - ( Note: In latest implementations it is O(n) )
    s = 'hellogeeks'
    slist = ''
    for i in s:
        slist = slist + i
    print( slist )

    # string concatenation (idiomatic and fast O(n))
    st = 'hellogeeks'
    slist = ''.join([i for i in s])
    print( slist )

    # Better way to iterate a range
    evens = [ i for i in range(10) if i%2 == 0]
    print( evens )

    # Less faster
    i = 0
    evens = []
    while i < 10:
        if i %2 == 0:
            evens.append(i)
        i += 1
    print( evens )

    # slow
    v = 'for'
    s = 'geeks ' + v + ' geeks'
    print( s )

    # fast
    s = 'geeks %s geeks' % v
    print( s )

    ex_helpers.end_example( ex_name )

#ex_idiomatic()
 
# ----------- helper
def repeat_it(   ):
    """
    just some code to profile
    """
    repeat = 100_000
    a      = 100
    b      = 10005
    for i in range( repeat ):
        x = a + b
        y = b ** a


# next is also a kind of introspection
"""
The Python Profilers — Python 3.7.4 documentation
    *>url  https://docs.python.org/3/library/profile.html
"""
# ----------------------------------------
def ex_c_profile():
    ex_name  = "ex_c_profile"    
    print( f"""{ex_helpers.begin_example( ex_name )}
    """)

    for i in range( 0, 10 ):
        profiler    = cProfile.Profile( )
        a_profile   = profiler.runcall( repeat_it )
    profiler.print_stats()
    profiler.dump_stats("result.txt")
    #print( f" a _profile = {a_profile}"  )
    ex_helpers.end_example( ex_name )   

#ex_c_profile()
 
# ---- old timinging without timing utility might work or not ========================
 
# ----------------------------------------
def ex_time_some_code():
    ex_name  = "ex_template"    
    print( f"""{ex_helpers.begin_example( ex_name )}
    bunch of conversions from web  good: keep   ===============
    """ )
    start           = time.time()
    perf_start      = time.perf_counter()

    timestamp       = 1226527167.595983
    loop_max        = int( 1e5 )
    for ix in range( 1, loop_max  ):

          time_tuple = time.gmtime( timestamp )

    end              = time.time()
    perf_end         = time.perf_counter()

    print( f"for {loop_max} itterations code took" )

    msg   = ( f"    by time:         {end - start} seconds" )
    print( msg )

    msg   = ( f"    by perf_counter: {perf_end - perf_start} seconds" )
    print( msg )

    # again with time_util
    code_timer    = ex_helpers.CodeTimer()
    msg           = f"\nfor {loop_max} itterations code took - using CodeTimer"
    code_timer.reset(  )

    timestamp       = 1226527167.595983
    loop_max        = int( 1e5 )
    
    for ix in range( 1, loop_max  ):
          time_tuple = time.gmtime( timestamp )

    code_timer.stop()
    ex_helpers.end_example( ex_name )

#    How can I time a code segment for testing performance with Pythons timeit? - Stack Overflow
#    *>url  https://stackoverflow.com/questions/2866380/how-can-i-time-a-code-segment-for-testing-performance-with-pythons-timeit
#   timeit.timeit('foobar()', number=1000)

#You can use time.time() or time.clock() before and after the block you want to time.
#
#This method is not as exact as timeit (it does not average several runs) but it is straightforward.
#
#time.time() (in Windows and Linux) and time.clock() (in Linux) are not precise enough for
#fast functions (you get total = 0). In this case or if you want to average the time elapsed by several runs,
# you have to manually call the function multiple times (As I think you already do in you example code and
#timeit does automatically when you set its number argument)

#In Windows, as Corey stated in the comment, time.clock() has much higher precision (microsecond instead of second)
#
#and is preferred over time.time().

#ex_time_some_code()

#------------helper object -----------------------------
class Pet(object):

    # will have instance and class

    def __init__(self, name, species):
        self.name     = name
        self.species  = species
        self.age      = 22

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)
        return f"{self.name} is a {self.species} "


# ----------------------------------------
def ex_time_class_access():
    ex_name  = "ex_time_class_access"    
    print( f"""{ex_helpers.begin_example( ex_name )}
    class, instance and local versions   ===============
    python might be smart enough to cache ??
    """ )

    # instance reference
    loop_max        = int( 1e7 )
    a_pet           = Pet( "Spike", "mut" )

    # --------------------------
    msg   = "local instance reference "
    msg   = "instance reference       "

    start = time.time()

    total           = 0
    for ix in range( 1, loop_max  ):

           total    = total + a_pet.age
           total    = total - a_pet.age

    # class reference
    total           = 0
    end             = time.time()
    print( f"{msg} for {loop_max} itterations code took {end - start} seconds")

    # --------------------------
    msg   = "local instance reference "
    msg   = "class reference          "
    start = time.time()     # yes it is faster
    for ix in range( 1, loop_max  ):

           total    = total +  Pet.class_age
           total    = total -  Pet.class_age

    end = time.time()
    print( f"{msg} for {loop_max} itterations code took {end - start} seconds")

    # --------------------------
    total             = 0
    l_age             = 0
    msg               = "local instance reference "
    msg               = "local   reference        "
    # this uses a local rev
    start = time.time()     # yes it is faster
    for ix in range( 1, loop_max  ):
           total    = total +  l_age
           total    = total -  l_age

    end = time.time()
    print( f"{msg} for {loop_max} itterations code took {end - start} seconds")

    # --------------------------
    age             = a_pet.age
    msg   = "local instance reference "
    msg   = "local instance reference "
    # this uses a local rev
    start = time.time()     # yes it is faster
    for ix in range( 1, loop_max  ):
           total    = total +  age
           total    = total -  age

    end = time.time()
    print( f"{msg} for {loop_max} itterations code took {end - start} seconds")

    # --------------------------
    total           = 0
    age             = Pet.class_age
    msg   = "local instance reference "
    msg   = "local class  reference   "
    # this uses a local rev
    start = time.time()     # yes it is faster
    for ix in range( 1, loop_max  ):

           total    = total +  age
           total    = total -  age

    end = time.time()
    print( f"{msg} for {loop_max} itterations code took {end - start} seconds")

    # --------------------------
    total           = 0
    age             = Pet.class_age
    a_pet           = Pet( "joe",  "duck")
    msg   = "local instance reference "
    msg   = "local class for 2 uses reference   "
    # this uses a local rev
    start = time.time()     # yes it is faster
    for ix in range( 1, loop_max  ):
           age      = Pet.class_age
           total    = total +  age
           total    = total -  age

    end = time.time()
    print( f"{msg} for {loop_max} itterations code took {end - start} seconds")

    # --------------------------
    total           = 0
    age             = Pet.class_age
    a_pet           = Pet( "joe",  "duck")
    msg   = "local instance reference "
    msg   = "local inst 2 uses reference   "
    # this uses a local rev
    start = time.time()     # yes it is faster
    for ix in range( 1, loop_max  ):
           age      = a_pet.age
           total    = total +  age
           total    = total -  age

    end = time.time()
    print( f"{msg} for {loop_max} itterations code took {end - start} seconds")

# ex_time_class_access()



# ========================= eof =========================











