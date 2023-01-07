# -*- coding: utf-8 -*-

""""
This is a

Purpose:
    Pathlib examples

Status:
    draft, covers most of the basics

Search for the following in the code below:

        def ex_        for the beginning of an example

        anchor
        absolute       full path back to root
        change         os.chdir()
        cwd            current working directory
        exists         does a file, path, directory exist
        extension      suffix
        explore        explore a directory or tree
        delete         delete the file  -- called unlink
        forward slash  -- not covered -- same as joinpath
        home
        is_dir
        is_file
        iterdir()      loop thru files in a directory
        home           home path of user
        join
        list           itr
        glob
        mkdir          and rmdir
        name           name of path as a string
        open
        parent         next directory up
        parts          parts of the path
        pathlib
        read
        read_text      read text as a string
        rename
        resolve        convert to a full path from the root
        rmdir
        set            directory
        stat           function
        stem
        string         build from string
        suffix         as in extension
        size           >> not here now? see ex_file.py
        touch          create or overwrite an empty file
        unlink         delete
        ./
        ../

Additions to consider:
    PurePath().match() checks whether the path matches a given pattern:
    PurePath().with_name() changes the name of the final component with its suffix:

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

import os
import sys
import dis
from   pathlib import Path

# ------- local
import ex_helpers       # this has rouines to help in showing examples


# ----------------------------------------
def path_create_transform( a_string, resolve_it = False ):
    """
    helper to show path parts given a string name
    shows results of Pathlib attributes and functions
    this is also good example code for pathlib
    resolve_it = True will do most functions with the resolved file name
                 if the file does not exist then...
    note that types like pathlibs print looking like strings but they are usually not
    """
    print( f"\nShow Path and its parts for a path built from {a_string} with resolve_it "
           f"= {resolve_it} --------------" )

    a_path   = Path( a_string )     # build from string

    print( f"a_path                 {a_path}type: {type(a_path)}" )

    if resolve_it:
        a_path   = a_path.resolve()
        print( f"a_path resolved to     {a_path}" )
        print(  "    --- if file does not reslove, nothing much happens")
    else:
        print( f"a_path.resolve()       {a_path.resolve()}   type: {type(a_path.resolve())}" )

    print( f"a_path                 {a_path}type: {type(a_path)}" )

    print( f"str(a_path)            {str(a_path)}    type: {type(str(a_path))}" )
    print( f"repr( a_path )         {repr( a_path )}type: {type(repr( a_path ))}" )

    #print( f"absolute())            {a_path.absolute()}    type: {a_path.absolute()}" )
    obj    = a_path.absolute()
    print( f"absolute()             {str(obj):30}    type: {type(obj)}" )

    #-------------------------------+----------------
    #print( f"a_path.name            {a_path.name}" )   #.name: the file name without any directory

    print( f"a_path.exists()        {a_path.exists()}type: {type(a_path.exists())}" )
    #-------------------------------+----------------
    print( f"a_path.parent          {a_path.parent}type: {type(a_path.parent)}" )
    #-------------------------------+----------------
    # Get the Nth parent folder path mul_above = Path.cwd().parents[0]

    obj    = a_path.parents
    print( f"a_path.parents         {str(obj):30}    type: {type(obj)}" )

    obj    = len( a_path.parents )
    print( f"len( a_path.parents )  {str(obj):30}    type: {type(obj)}" )

    obj    = a_path.parents[0]
    print( f"a_path.parents[0]      {str(obj):30}    type: {type(obj)}" )  # may error out if does not exist
    #-------------------------------+----------------

    print( f"a_path.is_dir          {a_path.is_dir()}" )
    print( f"a_path.is_file         {a_path.is_file()}" )
    #-------------------------------+----------------
    obj    = a_path.name
    print( f"a_path.name            {str(obj):30}    type: {type(obj)}" )
        #.name: the file name without any directory
    obj    = a_path.stem
    print( f"a_path.stem            {str(obj):30}    type: {type(obj)}" )
        # .stem: the file name without the suffix
    print( f"a_path.suffix          {a_path.suffix}  type: {type(a_path.suffix)}" )
        # .suffix: the file extension
    print( f"a_path.parts           {a_path.parts}" )
    print( f"a_path.anchor          {a_path.anchor}" )
        # the part of the path before the directories
    #-------------------------------+----------------

    #print( f"a_path.owner()          {a_path.owner()}")   # linux only

    if a_path.exists():

       print( f"a_path.stat()          {a_path.stat()}" )     # file must exist
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

# ----------------------------------------
def ex_path_create_transform():
    """
    example code, see print and read codepath_create_transform
    """
    ex_name  = "ex_path_create_transform"
    print( f"{ex_helpers.begin_example( ex_name )} "
           f"\n    creation and transforms of path"
           f"\n    some create other paths or strings or ..."
           f"\n    prints function results and type of result" )
    # see helper function show_path( ) for more pathlib example code

    #show_path( r"D:\Russ\0000\python00\python3\_examples\ex_bulldog.py", resolve_it  = True )

    #show_path( "ex__ex.py",       resolve_it  = True )
    path_create_transform( "ex_pathlib.py", resolve_it  = True )


    path_create_transform( "ex_pathlib.py", resolve_it  = True )

    ex_helpers.end_example( ex_name )  

#ex_path_create_transform()     


# ----------------------------------------
def ex_path_create():
    ex_name  = "ex_path_create"
    print( f"""{ex_helpers.begin_example( ex_name )}
          path.is_xxx does some of this
          """ )

    # adjust a_string for your system, file will not be changed, file need not exist
    print( "Also see function show_path()")
    a_string        = r"D:/Russ/0000/python00/python3/_projects/structured_notes/data/test/mush_obs.txt"
    a_path          = Path( a_string )

    print( "as strings can use . ./ ../ ~")

    a_path          = Path( __file__  ) # current file
    print( f"{a_path}")

    a_path          = Path.cwd() #
    print( f"{a_path}")

    print( a_path.parents[1] )  # ?? itterable

    print( "can you use a file handel, you can use a path ??")

    ex_helpers.end_example( ex_name )   

#ex_path_create()

# ----------------------------------------
def ex_path_to_string():
    ex_name  = "ex_path_to_string"
    print( f"""{ex_helpers.begin_example( ex_name )}
           unless a path is resloved or absolute the str( a_path ) will refer
           to a file that depends on context, usually cwd
           so it may help to resolve it
          """ )
    print( "example not written !!")
    ex_helpers.end_example( ex_name )   

#ex_path_to_string()

# ----------------------------------------
def ex_path_exists():
    ex_name  = "ex_path_exists"
    print( f"""{ex_helpers.begin_example( ex_name )}
          path.is_xxx does some of this
          """ )

    # adjust a_string for your system, file will not be changed, file need not exist
    print( "Also see function show_path()")
    a_string        = r"D:/Russ/0000/python00/python3/_projects/structured_notes/data/test/mush_obs.txt"
    a_path          = Path( a_string )
    does_exist      = a_path.exists()

    print( f"\nthe path {a_path} exists = {does_exist}")

    ex_helpers.end_example( ex_name )   

#ex_path_exists()

# ----------------------------------------
def ex_path_joinpath():
    ex_name  = "ex_path_joinpath"
    print( f"""{ex_helpers.begin_example( ex_name )}

          """ )

    # Join paths joined_path = cwd / 'Output' / 'FolderName

    # example_file = Path( r"D:/Russ/0000/python00/python3/_examples/ex__ex.py")   # not cap sens  on win
    # example_path = Path( r"D:/Russ/0000/python00/python3/_examples/ex__ex.py")
    # example_path = Path( r"ex__ex.py")

    # create from scratch
    a_path         = Path()

    a_new_path     = a_path.joinpath( 'python', 'scripts', 'test.py')

    print( a_new_path )

    # or build on
    a_newer_path     = a_new_path.joinpath( 'python', 'scripts', 'test.py')
    print( a_newer_path )

    ex_helpers.end_example( ex_name )   

#ex_path_joinpath()     

# ----------------------------------------
def ex_path_read_write():
    ex_name  = "ex_path_read_write"
    print( f"{ex_helpers.begin_example( ex_name )}"
           f"\n    reading and writing" )
    """
    still to do:
        .writetext( )   will create and write somewhere
        / operator between path and string
    """
    a_path    = Path( "readme_rsh.txt")
    with a_path.open() as a_file:   # = a_file = open( a_path )
        print( a_file.readline() )

    print( "Methods read_text, read_bytes, write_text and write_bytes -> here only read_text")
    a_path    = Path( "readme_rsh.txt")
    file_text   =  a_path.read_text()
    print( f"file text read with read_text\n>{file_text}<")

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

    ex_helpers.end_example( ex_name )  

#ex_path_read_write()     

# ----------------------------------------
def ex_path_discovery():
    ex_name  = "ex_path_discovery"
    print( f"""{ex_helpers.begin_example( ex_name )}
          need to do
          """ )
    home_dir = Path.home()
    print( f"Path.home()     {home_dir}" )

    # Get the path to the current working directory
    print( f"Path.cwd()     {Path.cwd()}" )

    # with some literals
    a_string  = "./"
    a_path    = Path( a_string )
    a_path_resolved  = a_path.resolve()
    print( f'{a_string} gives >{a_path}< resolves to -> >{a_path_resolved}<' )

    # with some literals
    a_string  = "../"
    a_path    = Path( a_string )
    a_path_resolved  = a_path.resolve()
    print( f'{a_string} gives >{a_path}< resolves to -> >{a_path_resolved}<' )

    # current file
    print( f"Path(__file__)     {Path(__file__)}" )

    # Get the first parent folder path one_above
    parent = Path.cwd().parent
    print( parent )

    # explore a directory list and itterate down
    # stop too much output
    print( "\n\n------------- iterdir() ------------------")
    a_path    = home_dir
    print( f"iterdir from {a_path}")
    for ix, child in enumerate( a_path.iterdir()):
        print( f"{ix} found via iterdir: {child}   {type(child)} >{str( child )}<" )
        if ix > 10:
            break

    # use glob -- explores what ?? all sub directories
    print( "\n\n------------- glob() ------------------")

    # ---- choose one:
    a_path   = Path( r"../"  )
    # a_path   = Path( r"./"  )
    # a_path   = Path( r"."  )

    print( f"path is {a_path} resolves to {a_path.resolve()}")
    for child in a_path.glob('*.py'):
        print( child )

    ex_helpers.end_example( ex_name )   

#ex_path_discovery()

# ----------------------------------------
def ex_path_rename():
    ex_name  = "ex_path_rename"
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
    a_new_path      = Path( a_new_filename )
    a_path.rename( a_new_path )              # file with that name should not exist or error

    print( a_path.is_file())
    print( f"{a_new_filename} ... {a_new_path.is_file()}")

    # # --- more stuff to add somewhere
    # another_path    = a_path.with_suffix( ".05.ttxt")
    # a_new_path.rename( another_path )     # here using a path instead of string

    # print( a_new_path.suffixes )   # only last part after . is suffix

    ex_helpers.end_example( ex_name )  

#ex_path_rename()    

# ----------------------------------------
def ex_path_misc():
    ex_name  = "ex_path_misc"
    print( f"{ex_helpers.begin_example( ex_name )}"
            "" )

    print( f"Path.home() is the users home directory >{Path.home()}<")

    ex_helpers.end_example( ex_name )   

#ex_path_misc()     

# ----------------------------------------
def ex_path_cwd_and_context():
    ex_name  = "ex_path_cwd_and_context"
    print( f"{ex_helpers.begin_example( ex_name )}"
          "pathlib does not have a way to change cwd os does "
          "question: how does cwd interact with paths that are not 'complete'"
            "" )
    a_file_name            = "readme_rsh.lib"
    a_initial_cwd          = Path.cwd()

    print( f"\In our initial directory")
    print( f"{a_initial_cwd}")

    file_path_0     = Path( a_file_name )
    print(  f"file_path_0.absolute() >{file_path_0.absolute()}<")

    print( f"\nChange to ./dir_1")
    path_1          = a_initial_cwd / "dir_1"
    os.chdir( path_1 )
    print(  f"cwd                    >{Path.cwd()}<")
    file_path_1     = Path( a_file_name )
    print(  f"file_path_0.absolute() >{file_path_0.absolute()}<")
    print(  f"file_path_1.absolute() >{file_path_1.absolute()}<")

    print( f"\nChange to ./dir_2")
    path_2          = a_initial_cwd / "dir_2"
    os.chdir( path_2 )
    file_path_2     = Path( a_file_name )
    print(  f"file_path_0.absolute() >{file_path_0.absolute()}<")
    print(  f"file_path_1.absolute() >{file_path_1.absolute()}<")
    print(  f"file_path_2.absolute() >{file_path_2.absolute()}<")

    file_path_3     = Path( a_file_name ).absolute( )

    os.chdir( a_initial_cwd )
    print( Path.cwd() )

    print( "\nFinally back in our original directory...")

    print(  f"file_path_0 >{file_path_0}<")
    print(  f"file_path_1 >{file_path_1}<")
    print(  f"file_path_2 >{file_path_2}<")

    print( "\nAbsolute shows ....")
    print(  f"file_path_0.absolute() >{file_path_0.absolute()}<")
    print(  f"file_path_1.absolute() >{file_path_1.absolute()}<")
    print(  f"file_path_2.absolute() >{file_path_2.absolute()}<")

    print( "\nFile Path 3 is firmly attached to its cwd of the time it was created")
    print(  f"file_path_3.            >{file_path_3}<")
    print(  f"file_path_3.absolute()  >{file_path_3.absolute()}<")
    #rint( f"Path.home() is the users home directory >{Path.home()}<")

    print( "to attach your self thourugh to the cwd you might use " )
    file_path_3     = Path( a_file_name ).absolute( )


    ex_helpers.end_example( ex_name )   

#ex_path_cwd_and_context()    


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
    ex_name  = "ex_increment_extension"
    print( f"""{ex_helpers.begin_example( ex_name )}

          """ )

    # ---- choose a file name to try, initial file will be created
    file_name    = r"a_file.txt"
    #file_name    = r"a_file.01txt"
    file_name    = r"a_file.07txt"
    #file_name    = r"D:/Russ/0000/python00/python3/_examples/a_file.01txt"

    a_path       = Path( file_name )
    a_path.touch()                     #it will exist, old file if any gone

    # ---- setup done run it
    num    = increment_extension( a_path )

    print( f"file incremented to {num}")

    print( "Remember to clean up your file system " )

    ex_helpers.end_example( ex_name )   


#ex_increment_extension()     

# ----------------------------------------
def ex_path_application():
    ex_name  = "ex_path_application"
    print( f"""{ex_helpers.begin_example( ex_name )}
          need to do
          """ )
    """
    The / can join several paths or a mix of paths and strings (as above)
    as long as there is at least one Path object.
    If you do not like the special / notation, you can do
    the same thing with the .joinpath() method:

    >>> pathlib.Path.home().joinpath('python', 'scripts', 'test.py')
    PosixPath('/home/gahjelle/python/scripts/test.py')

    When you are renaming files, useful methods might be .with_name() and .with_suffix().
    They both return the original path but with the name or the suffix replaced, respectively.

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
    ex_helpers.end_example( ex_name )   


#ex_path_application()     

# ------------------- helper
def find_directory( a_path, do_resolve = False ):
    """
    given a path find the directory ( which is the path if it exists )
    if not a directory move up one level and see if that

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

    return None

# ----------------------------------------
def ex_find_directory():
    ex_name  = "ex_find_directory"
    print( f"""{ex_helpers.begin_example( ex_name )}
          adjust a_string for your tests
          """ )
    a_string        = r"D:/Russ/0000/python00/python3/_projects/structured_notes/data/test/mush_obs.txt"
    a_path          = Path( a_string )
    a_new_path      = find_directory( a_path )
    print( f"found dir = {a_new_path}")

    # again
    print()
    a_string        = r"D:/Russ/0000/python00/python3/_projects/structured_notes/data/test/mush_obs.tx"
    a_path          = Path( a_string )
    a_new_path      = find_directory( a_path )
    print( f"found dir = {a_new_path}")

    # again
    print()
    a_string        = r"D:/Russ/0000/python00/python3/_projects/structured_notes/data/test"
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

    ex_helpers.end_example( ex_name )   

#ex_find_directory()

# ----------------------------------------
def list_path_with_extension( dir_path, ext ):
    """
    Purpose:
        given a directory list all files with a given extension
    Args:
        dir_path      a directory path
        ext           extension as a string
    Retrun:
        list of file_paths
        Print paths as strings
    Note:
        probably could convert to list comp
    """
    a_list        = []
    a_path        = dir_path.resolve()
    for i_child in a_path.iterdir():
        #rint( i_child )
        i_ext     = i_child.suffix
        if i_ext == ext:
            a_list.append( i_child )
            #rint( i_child )
    return a_list

 # ----------------------------------------
def ex_list_path_with_extension( ):
    ex_name  = "ex_list_path_with_extension"
    print( f"{ex_helpers.begin_example( ex_name )}"
            "\nlist files in a directory with a given extension"
            "" )

    a_list   = list_path_with_extension( Path("./"), ".jpg" )
    ex_helpers.info_about_list( a_list )

    a_list   = list_path_with_extension( Path("./"), ".png" )
    ex_helpers.info_about_list( a_list )

    a_list   = list_path_with_extension( Path("./"), ".py" )
    ex_helpers.info_about_list( a_list )


    ex_helpers.end_example( ex_name )  

#ex_list_path_with_extension()


# ---- Ideas for more content  ....

"""

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

    # !!!!!!!!!!!!!!!! recurse down to delete empty dir

    # parts  = example_path.parts
    # print( f"parts {parts }")

    # some more iterating over a file

    #=----read write open...

    # Python 3's pathlib Module: Taming the File System – Real Python
    # https://realpython.com/python-pathlib/

    # # The .resolve() method will find the full path. Below, we confirm that the
    # current working directory is used for simple file names:
    # resolve_me   = example_path.resolve()
    # print( f"resolve_me {resolve_me }  of type {type(resolve_me)}")

    # example_file = Path( r"D:/Russ/0000/python00/python3/_examples/ex__ex.py")   # not cap sens  on win
    # example_path = Path( r"D:/Russ/0000/python00/python3/_examples/ex__ex.py")
    # example_path = Path( r"ex__ex.py")

    # some more iterating over a file

    # == read write open...

    # Python 3's pathlib Module: Taming the File System – Real Python
    # https://realpython.com/python-pathlib/

    # # The .resolve() method will find the full path. Below, we confirm that the current working directory is used for simple file names:
    # resolve_me   = example_path.resolve()
    # print( f"resolve_me {resolve_me }  of type {type(resolve_me)}")

"""
