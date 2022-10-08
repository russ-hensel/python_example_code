# -*- coding: utf-8 -*-



"""

Search:
        argv             get full file and path to initial file
        dir
        is
        isinstance
        callable(y)       add
        current         as in current directory
        file
        file name         xxx
        globals
        help
        locals
        memory
        path
        pre
        reps
        see all of running on
        size of
        str
        sys
        time
        type
        version
        __name__

       mem
       type

See Also:
        see also ex_dunder.py   and ex_class.py   ex_dis.py





---- template header example -----
What:   introspection type stuff
Status: draft, ok draft but possibly useful
Refs:

Code introspection in Python - GeeksforGeeks
    *>url  https://www.geeksforgeeks.org/code-introspection-in-python/

home-assistant/home-assistant: Open source home automation that puts local control and privacy first
    *>url  https://github.com/home-assistant/home-assistant


view.View Python Example
    *>url  https://www.programcreek.com/python/example/15897/view.View

What are Python dictionary view objects?
    *>url  https://www.tutorialspoint.com/What-are-Python-dictionary-view-objects

python - What are dictionary view objects? - Stack Overflow
    *>url  https://stackoverflow.com/questions/8957750/what-are-dictionary-view-objects

Python reflection: how to list modules and inspect functions - Federico Tomassetti - Software Architect
    *>url  https://tomassetti.me/python-reflection-how-to-list-modules-and-inspect-functions/


Notes:
    see also import ex_debug.py


    ** memory
    ** disassemble
    types              ex_type.py

    is instance
    issubclass()	Checks if a specific class is a derived class of another class.
    isinstance()	Checks if an objects is an instance of a specific class.



    ** help()	It is used it to find what other functions do
    hasattr()	Checks if an object has an attribute
    getattr()	Returns the contents of an attribute if there are some.
    repr()	Return string representation of object
    callable()	Checks if an object is a callable object (a function)or not.

    sys()	Give access to system specific variables and functions
    __doc__	Return some documentation about an object
    __name__	Return the name of the object.
    ** which version of python
    ** which version of os

    inspect — Inspect live objects — Python 3.8.0 documentation
    *>url  https://docs.python.org/3/library/inspect.html
dunder

print( repr( "z" ) )
'z'

print( repr( type("z" ) ) )
<class 'str'>

isinstance( a_series, str )

or int float ......
!!  add
#baz.py
import inspect
class foo:
      def bar():
          print 'Hello'
print(inspect.getsource(foo))

ssuming you have that package installed, you can use

    import numpy.random
    print(numpy.random.__file__)


    see and improve running_on.py   search for it figure out master copy where ???


"""


"""

!! add this
inspect — Inspect live objects

Source code: Lib/inspect.py

The inspect module provides several useful functions to help get information about live objects such as modules, classes, methods, functions, tracebacks, frame objects, and code objects. For example, it can help you examine the contents of a class, retrieve the source code of a method, extract and format the argument list for a function, or get all the information you need to display a detailed traceback.

There are four main kinds of services provided by this module: type checking, getting source code, inspecting classes and functions, and examining the interpreter stack.
Types and members


"""


import sys
import math
import timeit  # look for another util perf.....
import dis
import os
import time

import platform
import socket
import pkgutil

import psutil

import ex_helpers

ex_name    = "use as global pylint complains "



# ---- Helper classes and functions   -----
# ========================== ========================
class AppClass( object ):   # object for new style
    """
    """
    #  I put "static" in quotes because Python does not really have static variables in the sense that C++ and Java do.
    # these are class variables not instance ones
    class_var_1     = 5
    class_var_2     = "joe"

    # Class methods are different than C++ or Java static methods. If you want those, see staticmethod() in this section.
    @classmethod
    def foo( cls, arg1, arg2,):
        # cls will be passed as a ref to the class ( never an instance??  )
        # think you may be able to call dotted from an instance, but then do you get cls as class or instance
        ret  = cls.class_var_1
        print( ret )

# ------------------------------
    def __init__(self, arg ):
        # this is the constructor run when you create
        # like  app = AppClass( 55 )
        """
        private hidden  not including dunder
        """
        self.arg                   = arg
        self._private              = 6
        self.__mangled_private     = 9

    # =====----------------------------------
    # two decorated functions for set and get, note name match
    @property    # lets us get not set
    def demo_property( self ):
        print( " return self.__demo_property getter" )
        return self.__demo_property
    # ----------------------------------------
    @demo_property.setter
    def demo_property(self,  arg ):
        self.__demo_property   = arg
        print( " set self.__demo_property setter" )
        return

a_app_class  = AppClass  # to be used later



# ----- Helpers cont  -----
# ----------------------------------------
def print_eval( eval_string, msg = "Next eval the string"  ):
    """
    note may need to make objects in string global from caller
    move to ex_helpers.py
    """
    1/0   # now obsolete
    ex_helpers.print_eval( eval_string = eval_string , msg = msg )
    # print( f"\n{ msg }: >>{eval_string}<<" )
    # ret   = f"     >>{eval( eval_string )}<<end eval\n"
    # #ret   = obj2.index
    # # next is may not be useful, eval returns None ( at least in some cases )
    # print( ret  )

# ----------------------------------------
def  info_about_series( a_series, msg = "for a_series:" ):
    # depricated should be:
    ex_helpers.info_about_series( a_series, msg )
    # if  isinstance( a_series, Series ):
    #     print( f"\nmsg {msg}" )
    #     print( f"     series: >{a_series}<" )
    #     print( f"     a_series.values: >{a_series.values}<" )
    #     print( f"     a_series.index: >{a_series.index}<" )
    # else:
    #     print( f"\nfor msg = {msg} object is not an instance of Series" )
    # print( "------\n")

# ----------------------------------------
def time_me( ):
    """
    a helper, just something to be timed
    """
    for ix in  range( 100 ):
        sr   = math.sqrt( ix )

#time_me()

# ----------------------------------------
def intro_me( msg, a_object ):
    """
    helper function -- never used !!
    some introspection on the object
    and how to do it
    args:
        msg        a message to print
        a_object   a object whose infomration will be printed
    """
    print( f"{msg}" )

    the_type    = type( a_object )
    print( f"    as a string        >>{a_object}<<" )
    print( f"    type               >>{the_type}" )
    print( f"    type.__name__      >>{the_type.__name__}" )
    print( f"is it a string?        >>{the_type == str }")   # list....
    print( f"is it a lsit?          >>{the_type == list }")  # list....

# ----------------------------------------
def run_intro_me( ):
    intro_me( "try the greating", "hello world")
    intro_me( "try a list", [1,2,3])

#run_intro_me()


# ----------------------------------------
def linux_distribution():
    """
    helper function
    determines which linux distribution you are running on

    """
    try:
        return platform.linux_distribution()
    except:
        return "N/A"

# ----------------------------------------
def get_ip():
    """
    helper function

    Returns
       ip address, ip_address
    """
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        a_socket.connect(('10.255.255.255', 1))
        ip_address = a_socket.getsockname()[0]
    except:
        ip_address = '127.0.0.1'
    finally:
        a_socket.close()
    return ip_address

# ---------------------------------


def explore_package(module_name):
    """
    ng seem out of date


    List all the packages, modules installed in python pip - DataScience Made Simple
        *>url  http://www.datasciencemadesimple.com/list-packages-modules-installed-python/

    Python reflection: how to list modules and inspect functions - Federico Tomassetti - Software Architect
        *>url  https://tomassetti.me/python-reflection-how-to-list-modules-and-inspect-functions/


    """

    loader = pkgutil.get_loader(module_name)
    for sub_module in pkgutil.walk_packages([loader.filename]):
        _, sub_module_name, _ = sub_module
        qname = module_name + "." + sub_module_name
        print(qname)
        explore_package(qname)

# ----------------------------------------

class AnExClass( object ):
    def __init__(self):
        """

        """
        self.name  = ">>>>this is self.name<<<<"


# ------------- end helpers ---------------------------

# ---- examples ----

def ex_misc():
    #global ex_name
    ex_name  = "ex_misc"    # end with >> ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )}
    misc things that need a home
    """ )
    a_str    = str( math )   # string representation linked to __str__
    #a_str  = str( pi )
    print( f"a_str for math -> {a_str}")

    a_repr    = repr( math )   #  machine readable representation of a type.
    print( f"a_repr for math -> {a_repr}")

    ex_helpers.end_example( ex_name )

#ex_misc()                     # run it
#dis.dis( eval( ex_name ) )    # disassemble it

# ----------------------------------------
def ex_top_modules():
    ex_name  = "ex_top_modules"  # end with >> ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )}
    also use pip, these are top level ....
    a sort and filter might be nice
    this prints too much
    """ )

    for p in pkgutil.iter_modules():
        print( p[1] )
    #print( "hi" )


    #explore_package(sys.argv[1])

    #explore_package( "xml")
    ex_helpers.end_example( ex_name )

#ex_top_modules()

# ----------------------------------------
def ex_eval():
    ex_name  = "ex_eval"  # end with >> ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_eval )}
    evaluation of a string as py code using a helper:

    ex_helpers.eval_and_print( msg           ="this is an example",
                               values        = locals(),
                               eval_string   = "2=2",
                              )
    ex_helpers.print_eval( a_string, gl = globals(), lo = locals() )
    """ )


    ex_helpers.eval_and_print( msg           = "compare for equality",
                        values        = locals(),
                        eval_string   = "2==2",
                        )

    eval_string  = " 3/5 "
    ex_helpers.eval_and_print( "math",
                        values  = locals(),
                        eval_string   = "2+2",
                        )
   # eval_it( eval_string )

    eval_string  = "print( 3/5 )"
    ex_helpers.eval_and_print( "math with print",
                        values  = locals(),
                        eval_string   = "print( 3/5 )",
                        )
    # eval_it( eval_string )
    ex_helpers.end_example( ex_name )

# ex_eval()

# ----------------------------------------
def ex_isinstance():
    ex_name  = "ex_isinstance"  # end with >> ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )}     ===============
    this needs better examples
    """ )
    # ----- current scope
    msg, obj     = "test isinstance of string", "this is a string"
    print( msg, obj, isinstance( obj, str ))

    msg, obj     = "test isinstance of list", "this is a string"
    print( msg, obj, isinstance( obj, list ))

    msg, obj     = "test isinstance of list", [ "a", "b", ]
    print( f"{msg}: for;{obj}: result; {isinstance( obj, list )}"  )

    ex_helpers.end_example( ex_name )

#ex_isinstance()

# ----------------------------------------
def ex_dir():
    ex_name  = "ex_dir"  # end with >> ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )}
    dir() __dir__ __dir__()  class and module info
    some are not working due to import issues, think used to work so ??? change to print eval ??
    import lots in ex_helpers
    """ )
    # ---- dir  -- but not sure what to expect
    print( "\n----" )
    print( eval("dir()" ) )

    print( dir() )

    # ----- current scope
    a_string = "dir()"
    ex_helpers.print_eval( a_string , gl = globals(), lo = locals() )

    # ---- isinstance
    print("\n---- isinstance")
    print( isinstance( a_string, str ))

    # ---- locals a dict of all locals
    print( "\n---- locals")
    print( f"locals() >>{locals()}<<")

    # # ---- globals, output can be long
    # print()
    # print( f"globals() >>{globals()}<<")

    # # ---- directory of a module -- fairly long output
    # print()
    # # try a module and package
    # # a_string = "sys.__dir__"   # this is a functin
    # # ex_helpers.print_eval( a_string , gl = globals(), lo = locals() )

    # a_string = "sys.__dir__()"
    # ex_helpers.print_eval( a_string, gl = globals(), lo = locals() )
    # #print( sys.dir() )

    # a_string = "sys.__package__"    # not a function not clear what it was
    # ex_helpers.print_eval( a_string  , gl = globals(), lo = locals() )

    # ---- filepath to a class
    print( "\n---- filepath to a class")

#    How do I get the filepath for a class in Python? - Stack Overflow
#    https://stackoverflow.com/questions/697320/how-do-i-get-the-filepath-for-a-class-in-python
    print( ">>os.path.abspath(sys.modules[ AppClass.__module__].__file__)<<" )   # where AppClass is a class

    a_module   = sys                # ng, perhaps because installed ?
   # a_module   = ex_debug           # works
#    a_module   = ex_introspection   # not defined -- maybe import not complete

    # ?? not working now ??
    #print( sys.__file__ )
    #print( math.__file__() )
    #print( a_module.__file__ )
    # Will actually give you the path to the .pyc file that was loaded, at least on Mac OS X.
    #   So I guess you can do:

    # # sys.__file__
    # a_path = os.path.abspath( a_module.__file__ )
    # print( a_path )


    # a_path = os.path.dirname( a_module.__file__)
    # print( a_path )


    # a_string = "os.path.dirname( ex_debug.__file__)"  # ex_debug ok   # math ng
    # ex_helpers.print_eval( a_string, gl = globals(), lo = locals() )


    a_string = "os.path.dirname(__file__)"
    ex_helpers.print_eval( a_string, gl = globals(), lo = locals() )

    # ---- argv and startup path
    print( "\n---- argv and startup path")

    for ix_arg, i_arg in enumerate( sys.argv ):   # enumerate probably the right way
        msg = f"command line arg + {str( ix_arg ) }  =  { i_arg }"
        print( msg )

    # take apart argv[0] to get path and file name
    msg        = sys.argv[0]
    print( f"sys.argv[0]  {sys.argv[0]}" )
    msg        = msg.replace("\\", "/" )
    splits     = msg.split( "/" )
    path_to_start     = "/".join( splits[ :-1] )
    print( f"path to start up >>{path_to_start}<<")

    # ---- current working directory
    print( "\n---- current working directory" )
    # depending on how launched may be same as
    eval_string    = "os.getcwd()"      # Return the current working directory
    #print( f"current directory  os.getcwd() {msg}")

    ex_helpers.eval_and_print( msg           ="current directory",
                               use_globals   = globals(),
                               values        = locals(),
                               eval_string   = eval_string,
                              )


    ex_helpers.end_example( ex_name )

#ex_dir()

# ----------------------------------------
def ex_help():
    ex_name  = "ex_help"  # end with >> ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )}
    """ )
#    a_string = "help()"    # eval will leave you in help function
#    eval_it( a_string )

    a_string = "help(str)"   # lots of help for string might try to use something shouret
    ex_helpers.print_eval( a_string, gl = globals(), lo = locals() )

    ex_helpers.end_example( ex_name )

# ex_help()

# ----------------------------------------
def ex_doc():
    ex_name  = "ex_doc"  # end with >> ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )}
    get the doc string for some classes and this function
    """ )
    print(__doc__)      # doc of this module
    print(str.__doc__)  # doc of this module

    a_string = "str.__doc__"
    ex_helpers.print_eval( a_string, gl = globals(), lo = locals() )

    a_string = "math.__doc__"
    ex_helpers.print_eval( a_string, gl = globals(), lo = locals() )

    #print( type(math.__doc__) )
    ex_helpers.end_example( ex_name )


#ex_doc()

# ----------------------------------------
def ex_type():
    ex_name  = "ex_type"  # end with >> ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )}
    type and isinstance
    """)
    # print type of math
    print(type(math))

    # print type of 1
    print(type(1))

    # print type of "1"
    print(type("1"))

    # print type of rk
    rk =[1, 2, 3, 4, 5, "radha"]

    print( type(rk))
    print( type(rk[1]))
    print( type(rk[5]) )

    # # fix next !!
    # a_type_ret   = type( rk[5] )
    # print(   f"for  rk[5]  its type is { a_type_ret }  with __repr_ >>{a_type_ret.__repr__()}<<" )

    an_instance = AnExClass()

    a_type   = type( AnExClass )   # <class '__main__.AnExClass'>
    print( a_type )
    print( f"for instance of AnExClass type is {type( an_instance)}" )

    a_type   = type( an_instance )
    print( f"a_type {a_type}" )
    #print( f"for instance of AnExClass type is {type( an_instance)} the str is {str(type( an_instance)) and ""}" )
    class_name  = "AnExClass"

    print( "-----")
    print( f"<class '__main__.{class_name}'>" )
    print( ( type( an_instance ) ) )

    if   str( type( an_instance ) ) == f"<class '__main__.{class_name}'>":
        print( True )
    else:
        print( False )

    print( "check exact type of object inc your own classes ---type( an_instance ) is AnExClass --")
    if type( an_instance ) is AnExClass:
        print( True )
    else:
        print( False )

    a_type   = type( a_type )
    print( f"a_type 3 {a_type}" )

    ex_helpers.end_example( ex_name )

#ex_type()


# ----------------------------------------
def ex_timeit():
    ex_name  = "ex_timeit"  # end with >> ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )}
    timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000, globals=None)
    timeit — Measure execution time of small code snippets — Python 3.8.0 documentation
    ht ps://docs.python.org/3/library/timeit.html
    hard to put code in same module as your are tring to test, seems that namespace is new to timeit, maybe a global in it....
    """)
    call_time_me  = time_me # trying to get namespace issue resolved
    #a_time   = timeit.timeit( stmt = "time_me()", number=100 )
#    a_time   = timeit.timeit( setup="global call_time_me", stmt = "call_time_me()", number=100 )  no good

#    a_time   = timeit.timeit( stmt = "call_time_me", number=100 )
#    a_time   = timeit.timeit( stmt = "1+1; 2+2", number=100 )
    #a_time   = timeit.timeit( setup="from __main__ import test"   stmt = "import ex_introspection; print('hi')", number=10  )   # ng trys to run on import
    #print( f"a timeit time {a_time}" )

    ex_helpers.end_example( ex_name )

#ex_timeit()

# ----------------------------------------
def ex_time_with_clock():
    ex_name  = "ex_time_with_clock"  # end with >> ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )}
    how different from time.time
    D:/Russ/0000/python00/python3/_examples/ex_introspection.py:
        182: DeprecationWarning: time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8:
       use time.perf_counter or time.process_time instead
    """)

#    start    = time.clock()
#    start    = time.process_time()    # just to .1 sec ??
    start    = time.perf_counter()     # more precision

    # -------- what we time
    time_me()

    for i in range( 100 ):
        time_me()
    # ----------- end what we time
#    stop     = time.clock()
#    stop     = time.process_time()
    stop     = time.perf_counter()

    elapsed  = stop - start
    print( f"Time spent elapsed {elapsed}" )
    ex_helpers.end_example( ex_name )

#ex_time_with_clock()

# ----------------------------------------
def ex_running_from():
    ex_name  = "ex_running_from"  # end with >> ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )}
    see also ex_dir.py
    """)
    # ---- current working directory
    print( "\n----- Mess with current directory -----" )
    cur_dir  = os.getcwd()
    print( f"os.getcwd()              >>{os.getcwd()}<<" )
    # ------"---------------------------{-------------------

    os.chdir( "../")
    print( f"os.getcwd()              >>{os.getcwd()}<<" )
    os.chdir( cur_dir )
    print( f"os.getcwd()              >>{os.getcwd()}<<" )

    print( "\n----- On to Python -----" )
    from platform import python_version
    print( f"python_version()         >>{ python_version()}<<" )
    print( f"python_file location  sys.executable"
         f"\n                         >>{sys.executable}<<" )
    # ------"---------------------------{-------------------
    print( f"os.path.dirname(__file__)>>{os.path.dirname(__file__)}<<" )
    print( f"__file__                 >>{__file__}<" )

    # and more in sys
    # ------"---------------------------{-------------------

    # Running "python -v"from the command line tells you what is being
    # imported and from where. This is useful if you want to know the location of built in modules.
    # for some modules not the c ones?
    #print( f"sys.__file__()             {sys.__file__}" )  # ng

    import math
    # print( f"math.__file__()          >>{math.__file__}<<" ) # had error in 3.8
    # ------"------------------------->>{-------------------
    print( f"os.__file__              >>{os.__file__}<<" )
    # print( f"time.__file__()             {time.__file__}" )  # ng

    # ------"------------------------->>{-------------------
    # import libxml2
    # print( f"libxml2.__file__         >>{libxml2.__file__}<<" )

    # ---- filepath to a class and instance
    print( "\n---- filepath to a class and instance ----")
#    How do I get the filepath for a class in Python? - Stack Overflow
#    https://stackoverflow.com/questions/697320/how-do-i-get-the-filepath-for-a-class-in-python
    # ------"---------------------------{-------------------
    print( f"os.path.abspath(sys.modules[ AppClass.__module__].__file__)"
         f"\n                           >>{os.path.abspath(sys.modules[ AppClass.__module__].__file__)}<<" )
    # ------"---------------------------{-------------------
    print( f"os.path.abspath(sys.modules[ a_app_class.__module__].__file__)"
         f"\n                           >>{os.path.abspath(sys.modules[ a_app_class.__module__].__file__)}<<" )
    a_app_class
    a_module   = sys                # ng, perhaps because installed ?
   # a_module   = ex_debug           # works
#    a_module   = ex_introspection   # not defined -- maybe import not complete

    print( "\n---- more module location ----")
    # may be more complete names
    a_module   = os
    a_path     = os.path.abspath( a_module.__file__ )
    print( f"os.path.abspath( a_module.__file__ )"
         f"\n                            {os.path.abspath( a_module.__file__ )}" )
    # -------x---------------------------{-------------------

    a_path = os.path.dirname( a_module.__file__)
    print( a_path )
    print( f"os.path.dirname( a_module.__file__)"
         f"\n                          >>{os.path.dirname( a_module.__file__)}<<" )

    # ---- argv and startup path
    print( "\n---- argv and startup path ----")

    for ix_arg, i_arg in enumerate( sys.argv ):   # enumerate probably the right way
        msg = ( f"command line arg{str( ix_arg ) }  = "
             f"\n                          >>{ i_arg }<<" )
        # -------x---------------------------{-------------------
        print( msg )

    # take apart argv[0] to get path and file name
    msg        = sys.argv[0]
    print( f"sys.argv[0]               >>{sys.argv[0]}<<" )
    # -------x---------------------------{-------------------
    msg        = msg.replace("\\", "/" )
    splits     = msg.split( "/" )
    path_to_start     = "/".join( splits[ :-1] )
    print( f"path to start up          >>{path_to_start}<<")

    # ---- memory
    print( "\n---- memory ----")
    # -------x---------------------------{-------------------

    process = psutil.Process(os.getpid())
    print( f"process.memory_info().rss >>{process.memory_info().rss}<<")  # in bytes
    # -------x------------------------->>{-------------------
    print( f"sys.getsizeof([])         >>{sys.getsizeof([])}<<" )

    print( f"sys.getsizeof( sys )      >>{sys.getsizeof( sys )}<<" )

    ex_helpers.end_example( ex_name )

ex_running_from()

# ----------------------------------------
def ex_running_on():
    ex_name  = "ex_running_on"  # end with >> ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )}
    os operating system and python
    sys
    distro · PyPI
    https://pypi.org/project/distro/
    this should link to the rhslib one
    """)
    some_char   = "\n"

    print(  "\n---- sys ----"  )
    print( f"sys.platform()        {platform.platform()}" )
    print( f"sys.version           {sys.version}" )
    print( f"sys.version_info      {sys.version_info}" )
    print( f"sys.hexversion        {sys.hexversion}" )
    print( f"sys.executable        {sys.executable}" )
    print()
    print( f"sys.path              {sys.path}" )
    print()
    print(  "and sys has more..." )
    # ------"----------------------+---------------

    print( "\n---- ----"  )
    from platform import python_version

    print( f"python_version()     { python_version()}" )

    print( "\n---- platform ----"  )
    # ------"----------------------+---------------
    print( f"platform.platform()   {platform.platform()}" )

    print( f"platform.system()     {platform.system()}" )

    print( f"platform.release()    {platform.release()}" )
    # ------+----------------------+---------------
    print( f"platform.version()    {platform.version()}" )

    print( f"platform.processor()  {platform.processor()}" )

    print( f"""Python version: {sys.version.split( some_char )}

    linux_distribution: linux_distribution(),
    system:       {platform.system()}
    machine:      {platform.machine()}
    platform:     {platform.platform()},
    uname:        {platform.uname()},
    version:      {platform.version()},
    mac_ver:      {platform.mac_ver()},
    """ )

    #dist:              {str(platform.dist())}      # not working

    tcpip2   =  socket.gethostbyname(socket.getfqdn())  # – gimel Oct 3 '08 at 12:08
    print( f"tcpip2               >{tcpip2}<" )
    # ------+----------------------+---------------
    #This appears to only return a single IP address. What if the machine has multiple addresses? – Jason R. Coombs Oct 23 '09 at 14:39

    #  @Jason R. Coombs, use following code to retrieve list of IPv4 addresses that belong to the host machine:

    tcpip3  = socket.gethostbyname_ex(socket.gethostname())[-1]    #  – Barmaley
    print( f"tcpip3               >{tcpip3}<" )
    # ------+----------------------+---------------
    tcpip4   = get_ip()
    print( f"tcpip4               >{tcpip4}<" )
    # ------+----------------------+---------------
    ex_helpers.end_example( ex_name )

#ex_running_on ()

# ----------------------------------------
sys.path.append( "../_projects/rshlib")
import running_on
def ex_running_on_rsh():
    ex_name  = "ex_running_on_rsh"  # end with >> ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )}
    this shows the function of rshlib.running_on.RunningOn     """)

    running_on.RunningOn.gather_data()
    print( f"running_on.RunningOn     >>{running_on.RunningOn}<<" )
    # ------"-------------------------..{-------------------
    print( f"running_on.RunningOn.get_str()"
         f"\n                         >>{running_on.RunningOn.get_str()}<<" )
    # ------"-------------------------..{-------------------
    ex_helpers.end_example( ex_name )

#ex_running_on_rsh()

# ----------------------------------------
def ex_disassemble():
    ex_name  = "ex_disassemble"  # end with >> ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )}

    """)
    some_code   = dis.dis( time_me )
    print( some_code )
    ex_helpers.end_example( ex_name )

#ex_disassemble()

# ----------------------------------------
def ex_memory():
    ex_name  = "ex_memory"  # end with >> ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )}
    How to profile memory usage in Python | Pluralsight
    *>url  https://www.pluralsight.com/blog/tutorials/how-to-profile-memory-usage-in-python

    """)
    process = psutil.Process(os.getpid())
    print( f"process memory = {process.memory_info().rss}")  # in bytes

#    10,.2f
    # nicer
    mem          = process.memory_info().rss
    # convert to mega and format
    mem_mega     = mem/( 1e6 )
    msg          = f"process memory = {mem_mega:10,.2f} mega bytes "
    print( msg )

    msg          = f"process memory = {mem_mega:,.2f} mega bytes "
    print( msg )

    a_size    = sys.getsizeof({})
    print( a_size )
    print( f"sys.getsizeof({{}})    {sys.getsizeof({})}" )

    print( f"sys.getsizeof([])      {sys.getsizeof([])}" )

    print( f"sys.getsizeof( sys )   {sys.getsizeof( sys )}" )

#    from guppy import hpy   # not installed
#    h = hpy()
#    print( h.heap() )

#>>> sys.getsizeof(set())
    """
    add this later
    Understand How Much Memory Your Python Objects Use
    *>url  https://code.tutsplus.com/tutorials/understand-how-much-memory-your-python-objects-use--cms-25609
    """
    ex_helpers.end_example( ex_name )

#ex_memory()

# ----------------------------------------
def ex_built_in_map():
    ex_name  = "ex_built_in_map"  # end with >> ex_helpers.end_example( ex_name )
    print( f"""{ex_helpers.begin_example( ex_name )}
    """)
    # Python program to illustrate library functions
    # save time while coding with the example of map()

    no_loops  = 1000
    # slower (Without map())
    start = time.perf_counter()
    s = 'geeks'

    for ix_index in range( no_loops ):
        U = []
        for c in s:
            U.append(c.upper())
    print( U )
    stop = time.perf_counter()
    e1 = stop - start
    print( "Time spent in function is:         ", e1 )

    # Faster (Uses builtin function map())
    s = 'geeks'
    start = time.perf_counter()
    for ix_index in range( no_loops ):
        U = map(str.upper, s)
    print( U )
    stop = time.perf_counter()
    e2 = stop - start
    print( "Time spent in builtin function is: ", e2 )

    print( f"ratio {e1/e2}" )

    ex_helpers.end_example( ex_name )

#ex_built_in_map()


# keep alive -- works in spyder not on double click -- maybe because of python w

# while True:
#     print( "what")
#     time.sleep( 1 )







