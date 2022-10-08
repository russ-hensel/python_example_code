# -*- coding: utf-8 -*-

""""
This is a

What:
    Pathlib examples
Status:
    draft, covers most of the basics



Search for the following in the code below:

        anchor
        cwd            current working directory
        exists         does a file, path, directory exist
        home
        is_dir
        is_file
        join
        list          itr
        glob
        mkdir          and rmdir
        name           name of path as a string
        open
        parent         next directory up
        parts          parts of the path
        pathlib
        rename
        resolve        convert to a full path from the root
        rmdir
        stat           function
        stem
        suffix         as in extension
        touch          create or overwrite an empty file
        unlink         delete

Reference:

    Python 3's pathlib Module: Taming the File System – Real Python
    https://realpython.com/python-pathlib/

    PEP 428 – The pathlib module – object-oriented filesystem paths | peps.python.org
    https://peps.python.org/pep-0428/


    pathlib — Object-oriented filesystem paths — Python 3.10.7 documentation
    https://docs.python.org/3/library/pathlib.html

    A Deep Dive Into Pathlib And The Magic Behind It - YouTube
    https://www.youtube.com/watch?v=UcKkmwaRbsQ&t=143s


"""


import sys
import dis
from pathlib import Path

# ------- local
import ex_helpers       # this has rouines to help in showing examples


# ----------------------------------------
def show_path( a_string, resolve_it = False ):
    """
    helper to show path parts given a string name
    shows results of Pathlib attibutes and functions
    """
    print( f"\nShow Path for a path built on {a_string} with resolve_it = {resolve_it} --------------")
    a_path   = Path( a_string )
    print( f"a_path                 {a_path}" )

    if resolve_it:
        a_path   = a_path.resolve()
        print( f"a_path resolved to {a_path}" )

    print( f"a_path                 {a_path}" )
    #-------------------------------+----------------
    print( f"a_path.name            {a_path.name}" )   #.name: the file name without any directory
    print( f"a_path.exists          {a_path.exists}" )
    print( f"a_path.parent          {a_path.parent}" )
    #-------------------------------+----------------

    # Get the Nth parent folder path mul_above = Path.cwd().parents[0]

    print( f"a_path.parents         {a_path.parents}" )
    print( f"len( a_path.parents )  {len(a_path.parents)}" )
    print( f"a_path.parents(2)      {a_path.parents[0]}" )   # may error out if does not exist
    #-------------------------------+----------------

    print( f"a_path.is_dir          {a_path.is_dir()}" )
    print( f"a_path.is_file         {a_path.is_file()}" )
    #-------------------------------+----------------
    print( f"a_path.name            {a_path.name}" )          #.name: the file name without any directory
    print( f"a_path.stem            {a_path.stem}" )          # .stem: the file name without the suffix
    print( f"a_path.suffix          {a_path.suffix}" )        # .suffix: the file extension
    print( f"a_path.parts           {a_path.parts}" )
    print( f"a_path.anchor          {a_path.anchor}" )        # the part of the path before the directories
    #-------------------------------+----------------

    #print( f"a_path.owner()          {a_path.owner()}")   # linux only
    print( f"a_path.stat()          {a_path.stat()}" )
    """

    # .parent: the directory containing the file, or the parent directory if path is a directory

    other mostly linux
    p.is_symlink()
    p.is_socket()
    p.is_fifo()
    p.is_block_device()
    p.is_char_device()
    p.owner()
    """

    return


# ----------------------------------------
def ex_path_parts():
    ex_name  = "ex_path_parts"   # end with >>    ex_helpers.end_example( ex_name )  # not part of example, marks end
    print( f"""{ex_helpers.begin_example( ex_name )}

          """ )

    # see helper function show_path( ) for pathlib example code
    show_path( "ex__ex.py" )
    show_path( "ex__ex.py", resolve_it  = True )

    ex_helpers.end_example( ex_name )  # not part of example, marks end


# ex_path_parts()    # comment out this line to stop example from running
#eval( f"{ex_name}()" )         # run it
#dis.dis( ex_path_parts )    # disassemble it

#----------------------------------------

# ----------------------------------------
def ex_path_exists():
    ex_name  = "ex_path_exists"   # end with >>    ex_helpers.end_example( ex_name )  # not part of example, marks end
    print( f"""{ex_helpers.begin_example( ex_name )}
          path.is_xxx does some of this
          """ )

    # adjust a_string for your system, file will not be changed, file need not exist
    print( "Also see function show_path()")
    a_string        = r"D:\Russ\0000\python00\python3\_projects\structured_notes\data\test\mush_obs.txt"
    a_path          = Path( a_string )
    does_exist      = a_path.exists()

    print( f"\nthe path {a_path} exists = {does_exist}")

    ex_helpers.end_example( ex_name )  # not part of example, marks end


#ex_path_exists()

#eval( f"{ex_name}()" )         # run it
#dis.dis( eval( ex_name ) )    # disassemble it


# Moving and Deleting Files
# Create and write

# Explore

# Applications


# Possibly the most unusual part of the pathlib library is the
# use of the / operator. For a little peek under the hood, let us see how that is implemented.
# This is an example of operator overloading: the behavior of an operator is changed depending on
# the context. You have seen this before. Think about how +
# means different things for strings and numbers. Python implements operator
# overloading through the use of double underscore methods (a.k.a. dunder methods).


# ----------------------------------------
def ex_path_join():
    ex_name  = "ex_path_join"   # end with >>    ex_helpers.end_example( ex_name )  # not part of example, marks end
    print( f"""{ex_helpers.begin_example( ex_name )}

          """ )

    # Join paths joined_path = cwd / 'Output' / 'FolderName

    # example_file = Path( r"D:\Russ\0000\python00\python3\_examples\ex__ex.py")   # not cap sens  on win
    # example_path = Path( r"D:\Russ\0000\python00\python3\_examples\ex__ex.py")
    # example_path = Path( r"ex__ex.py")

    # create from scratch
    a_path    = Path()

    a_new_path     = a_path.joinpath( 'python', 'scripts', 'test.py')

    print( a_new_path )

    # or build on

    a_newer_path     = a_new_path.joinpath( 'python', 'scripts', 'test.py')

    print( a_newer_path )


    # !!!!!!!!!!!!!!!! recurse down to delete empty dir


    # parts  = example_path.parts
    # print( f"parts {parts }")

    # some more itterating over a file

    #=----read write open...

    # Python 3's pathlib Module: Taming the File System – Real Python
    # https://realpython.com/python-pathlib/

    # # The .resolve() method will find the full path. Below, we confirm that the
    # current working directory is used for simple file names:
    # resolve_me   = example_path.resolve()
    # print( f"resolve_me {resolve_me }  of type {type(resolve_me)}")

    # example_file = Path( r"D:\Russ\0000\python00\python3\_examples\ex__ex.py")   # not cap sens  on win
    # example_path = Path( r"D:\Russ\0000\python00\python3\_examples\ex__ex.py")
    # example_path = Path( r"ex__ex.py")



    # some more itterating over a file

    # == read write open...

    # Python 3's pathlib Module: Taming the File System – Real Python
    # https://realpython.com/python-pathlib/

    # # The .resolve() method will find the full path. Below, we confirm that the current working directory is used for simple file names:
    # resolve_me   = example_path.resolve()
    # print( f"resolve_me {resolve_me }  of type {type(resolve_me)}")

    ex_helpers.end_example( ex_name )  # not part of example, marks end


#ex_path_join()    # comment out this line to stop example from running


# ----------------------------------------
def ex_path_read_write():
    ex_name  = "ex_path_read_write"   # end with >>    ex_helpers.end_example( ex_name )  # not part of example, marks end
    print( f"""{ex_helpers.begin_example( ex_name )}

          """ )

    """
    still to do:

        .writetext( )   will create and write somewhere
        / operator between path and string

    """
    a_path    = Path( "readme_rsh.txt")
    with a_path.open() as a_file:
        print( a_file.readline() )

    # create empty file ... if it already exists or not
    a_path    = Path( "delete_me.txt")
    a_path.touch()

    # delete a file, exception if it does not exist
    a_path    = Path( "delete_me.txt")
    a_path.unlink()

    #Path.mkdir(mode=0o777, parents=False, exist_ok=False)

    a_path    = Path( "./sub_dir" )
    a_path.mkdir(   )   # return none

    print( f"your new dircctory exists = {a_path.exists()}")


    a_path.rmdir()   # dir must be empty to remove else exception ??
    print( f"your new dircctory exists = {a_path.exists()}")


    ex_helpers.end_example( ex_name )  # not part of example, marks end

#ex_path_read_write()    # comment out this line to stop example from running


# ----------------------------------------
def ex_path_discovery():
    ex_name  = "ex_path_discovery"   # end with >>    ex_helpers.end_example( ex_name )  # not part of example, marks end
    print( f"""{ex_helpers.begin_example( ex_name )}
          need to do
          """ )

    """

    """

    home_dir = Path.home()
    print( f"Path.home()     {home_dir}" )

    # Get the path to the current working directory
    print( f"Path.cwd()     {Path.cwd()}" )


    # current file
    print( f"Path(__file__)     {Path(__file__)}" )

    # Get the first parent folder path one_above
    parent = Path.cwd().parent
    print( parent )

    # explore a directory list and itterate down
    a_path    = home_dir
    for child in a_path.iterdir():
        print( child )

    # use glob -- explores what ?? all sub directories
    print( "\n\n------------- glob() ------------------")

    # ---- choose one:
    a_path   = Path( r"../"  )
    # a_path   = Path( r"./"  )
    # a_path   = Path( r"."  )

    print( f"path is {a_path} resolves to {a_path.resolve()}")
    for child in a_path.glob('*.py'):
         print( child )

    ex_helpers.end_example( ex_name )  # not part of example, marks end


#ex_path_discovery()    # comment out this line to stop example from running

# ----------------------------------------
def ex_path_rename():
    ex_name  = "ex_path_rename"   # end with >>    ex_helpers.end_example( ex_name )  # not part of example, marks end
    print( f"""{ex_helpers.begin_example( ex_name )}

          """ )

    # setup and delete files if they exist
    a_filename    = r"a_tile.txt"
    a_path    = Path( a_filename )
    if a_path.exists():
        a_path.unlink()                # delete if exists else error

    a_new_filename  = r"a_new_title.txt"
    a_new_path  = Path( a_new_filename )
    if a_new_path.exists():
        a_new_path.unlink()

    # end setup start create and rename
    a_path.touch( )
    print( a_path.is_file() )


    a_new_filename  = r"a_new_title.txt"
    a_new_path  = Path( a_new_filename )
    a_path.rename( a_new_path )              # file with that name shoud not exist or error

    print( a_path.is_file())
    print( f"{a_new_filename} ... {a_new_path.is_file()}")

    # # --- more stuff to add somewhere
    # another_path    = a_path.with_suffix( ".05.ttxt")
    # a_new_path.rename( another_path )     # here using a path instead of string

    # print( a_new_path.suffixes )   # only last part after . is suffix


    ex_helpers.end_example( ex_name )  # not part of example, marks end


#ex_path_rename()    # comment out this line to stop example from running

# ----------------------------------------
def increment_extension( a_path ):
        """
        good to 90ish files
        increments first 2 characters in extension ( if not numbers, extends the extensin )
        read the code
        """
        a_path_less_suffix   = Path.joinpath( a_path.parent, a_path.stem )
        #rint( f"a_path_less_suffix   {a_path_less_suffix}" )

        suffix          = a_path.suffix
        num             = suffix[ 1:3 ]   # skip . get next two
        suffix_suffix   = suffix[ 3: ]

        try:
            num            = int( num )
        except:
            num            = 0
            suffix_suffix  = suffix[ 1:]
            #rint( f"no num at first 2 car in extension set suffix_suffix to {suffix_suffix}" )

        while True:
            num = num + 1
            if num > 98:
                raise Exception( )  # fix for which one

            new_suffix         = f".{num:0>2}{suffix_suffix}"   # pad and put back .
            #rint( new_suffix )

            a_rename_path      = a_path.with_suffix(  new_suffix  )

            if a_rename_path.exists():
                pass
            else:
                #rint( a_rename_path )
                a_path.rename( a_rename_path )
                return num
                # break

# ----------------------------------------
def ex_increment_extension():
    ex_name  = "ex_increment_extension"   # end with >>    ex_helpers.end_example( ex_name )  # not part of example, marks end
    print( f"""{ex_helpers.begin_example( ex_name )}

          """ )

    # ---- choose a file name to try, initial file will be created
    file_name    = r"a_file.txt"
    #file_name    = r"a_file.01txt"
    file_name    = r"a_file.07txt"
    #file_name    = r"D:\Russ\0000\python00\python3\_examples\a_file.01txt"

    a_path       = Path( file_name )
    a_path.touch()                     #it will exist, old file if any gone

    # ---- setup done run it
    num    = increment_extension( a_path )

    print( f"file incremented to {num}")

    print( "Remember to clean up your file system " )

    ex_helpers.end_example( ex_name )  # not part of example, marks end


#ex_increment_extension()    # comment out this line to stop example from running

# ----------------------------------------
def ex_path_application():
    ex_name  = "ex_path_application"   # end with >>    ex_helpers.end_example( ex_name )  # not part of example, marks end
    print( f"""{ex_helpers.begin_example( ex_name )}
          need to do
          """ )


    """
    The / can join several paths or a mix of paths and strings (as above) as long as there is at least one Path object.
    If you do not like the special / notation, you can do the same thing with the .joinpath() method:

    >>> pathlib.Path.home().joinpath('python', 'scripts', 'test.py')
    PosixPath('/home/gahjelle/python/scripts/test.py')

    When you are renaming files, useful methods might be .with_name() and .with_suffix(). They both return the original path but with the name or the suffix replaced, respectively.

    For instance:

    >>> path
    PosixPath('/home/gahjelle/realpython/test001.txt')
    >>> path.with_suffix('.py')
    PosixPath('/home/gahjelle/realpython/test001.py')
    >>> path.replace(path.with_suffix('.py'))

    from the real python
    Display a Directory Tree

    Find the Last Modified File


    Create a Unique File Name


    """
    ex_helpers.end_example( ex_name )  # not part of example, marks end


#ex_path_application()    # comment out this line to stop example from running

# ------------------- helper
def find_directory( a_path, do_resolve = False ):
    """
    given a path find the directory ( which is the path if it exists )
    if not a directory move up one level and see if that

    see rshlib

    Returns:
        path of the directory or None


    """
    if a_path.exists() and a_path.is_dir():
        if do_resolve:
            # un-necessary to have 2 steps, just if you want to debug
            a_r_path    = a_path.resolve( )
            a_path      = a_r_path
        return a_path

    # strip one level and check again

    a_new_path  = a_path.parent
    #rint( f"a_new_path = {a_new_path}" )
    if a_new_path.exists() and a_new_path.is_dir():
        # un-necessary to have 2 steps, just if you want to debug
        a_r_path    = a_new_path.resolve( )
        a_new_path      = a_r_path
        return a_new_path
    # else return None

# ----------------------------------------
def ex_find_directory():
    ex_name  = "ex_find_directory"   # end with >>    ex_helpers.end_example( ex_name )  # not part of example, marks end
    print( f"""{ex_helpers.begin_example( ex_name )}
          adjust a_string for your tests
          """ )


    a_string        = r"D:\Russ\0000\python00\python3\_projects\structured_notes\data\test\mush_obs.txt"
    a_path          = Path( a_string )
    a_new_path      = find_directory( a_path )
    print( f"found dir = {a_new_path}")

    # again
    print()
    a_string        = r"D:\Russ\0000\python00\python3\_projects\structured_notes\data\test\mush_obs.tx"
    a_path          = Path( a_string )
    a_new_path      = find_directory( a_path )
    print( f"found dir = {a_new_path}")


    # again
    print()
    a_string        = r"D:\Russ\0000\python00\python3\_projects\structured_notes\data\test"
    a_path          = Path( a_string )
    a_new_path      = find_directory( a_path )
    print( f"found dir = {a_new_path}")

    # again
    print()
    a_string        = r"./ex_pathlib.py"
    a_path          = Path( a_string )
    a_new_path      = find_directory( a_path )
    print( f"found dir = {a_new_path}")
    a_new_path      = find_directory( a_path, do_resolve = True )
    print( f"found dir = {a_new_path}")
    a_new_new_path  = a_new_path.resolve( )
    print( f"a_new_new_path = {a_new_new_path}")

    ex_helpers.end_example( ex_name )  # not part of example, marks end


ex_find_directory()    # comment out this line to stop example from running
