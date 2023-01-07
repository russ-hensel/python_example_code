# -*- coding: utf-8 -*-

"""
Purpose:   String examples
           Some applies to other list like objects and itterables

Status: draft, ok a draft and a mess but possibly useful
        incomplete, but some string topics in other files 

See Also:
    ex_f_string.py

Search for the following in the code below:

    def ex_        for the beginning of an example

    align
    backslash              r"\" is ng use "\\""
    begin                  ->> startswith
    capitalize
    case
    concatenation          use join or f_strings not a loop
    convert
    ends
    endswith
    find
    join
    leading
    long
    lower
    lstrip
    multi line
    pad
    partition
    replace
    rpartition
    rsplit                     help( "".split   ) exists
    split                      maxsplit  keepends      help( "".split   )
    splitlines
    starts
    startswith
    strip                    which is a kind of trim
    title
    tokenize                 this is for python source code, help( "".tokenize   )
    trim
    upper
    upper


Reference:

    see ex_unicode.py for dealing with unicode conversion
    *>shell     D:/Russ/0000/python00/python3/_examples/ex_unicode.py

    #>>>>>python example string  see also for snipping and splitting
    #https://docs.python.org/2/library/string.html

    #http://www.tutorialspoint.com/python/string_find.htm

    Unicode/UTF-8-character table - starting from code position 2000
    https://www.utf8-chartable.de/unicode-utf8-table.pl?start=8192&number=128&utf8=string-literal

    # clean this up organize

    # see ex_lists.py for slicing
       *>shell  D:/Russ/0000/python00/python3/_examples/ex_string.py
       *>shell  D:/Russ/0000/python00/python3/_examples/ex_string_format.py
       *>shell  D:/Russ/0000/python00/python3/_examples/ex_string_parse_sql.py
       *>shell  D:/Russ/0000/python00/python3/_examples/ex_string_snips.py
       *>shell  D:/Russ/0000/python00/python3/_examples/ex_string_split.py
       *>shell  D:/Russ/0000/python00/python3/_examples/ex_string_strip.py

    # cvs module
    # partition
    # strip                  should be in seperate file
    # trim   is strip        should be in seperate file

    PEP 616 -- String methods to remove prefixes and suffixes | Python.org
        *>url  https://www.python.org/dev/peps/pep-0616/

    Pylint features — Pylint 2.11.2-dev0 documentation
        *>url  https://pylint.pycqa.org/en/latest/technical_reference/features.html?highlight=good-names#basic-checker-options

    python example code to align equal signs - Google Search
        *>url  https://www.google.com/search?q=python+example+code+to+align+equal+signs&client=firefox-b-1-d&sxsrf=AOaemvIeIiNcmwU6Qcs3_u65APjUwoLAIw%3A1637676043481&ei=C_ScYaK4HNquwbkP1Ze9mAw&ved=0ahUKEwji6c_W0q70AhVaVzABHdVLD8MQ4dUDCA0&uact=5&oq=python+example+code+to+align+equal+signs&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsAM6BwgjELACECc6BAghEApKBAhBGABQxA1YqCtg-TBoAHACeACAAWmIAfYFkgEDNS4zmAEAoAEByAEEwAEB&sclient=gws-wiz

    String Alignment in Python f-string - GeeksforGeeks
        *>url  https://www.geeksforgeeks.org/string-alignment-in-python-f-string/

    Sharp Column Indenter - Visual Studio Marketplace
        *>url  https://marketplace.visualstudio.com/items?itemName=kudchikarsk.sharp-column-indenter&ssr=false

    smart-column-indenter/src/languages at master · lmcarreiro/smart-column-indenter · GitHub
        *>url  https://github.com/lmcarreiro/smart-column-indenter/tree/master/src/languages

    Elastic tabstops - a better way to indent and align code
        *>url  https://nickgravgaard.com/elastic-tabstops/

    Releases · nickgravgaard/ElasticNotepad · GitHub
        *>url  https://github.com/nickgravgaard/ElasticNotepad/releases

    ElasticNotepad/elasticTabstops.scala at master · nickgravgaard/ElasticNotepad · GitHub
        *>url  https://github.com/nickgravgaard/ElasticNotepad/blob/master/app/src/elasticTabstops.scala

    Download Komodo Edit - ActiveState
        *>url  https://www.activestate.com/products/komodo-ide/downloads/edit/

    String Manupulation extension - Google Search
        *>url  https://www.google.com/search?q=String+Manupulation+extension&client=firefox-b-1-d&sxsrf=AOaemvIVPrwsrp2B2t5Y3b9CxUhozmJExg%3A1637677875746&ei=M_ucYfjkLJGJwbkPobu7iA0&ved=0ahUKEwi4yqjA2a70AhWRRDABHaHdDtEQ4dUDCA0&uact=5&oq=String+Manupulation+extension&gs_lcp=Cgdnd3Mtd2l6EAMyBwghEAoQoAE6BwgAEEcQsAM6BwgAELEDEAo6BAgAEAo6BAgAEA06BggAEBYQHkoECEEYAFDVC1ibQmDCRWgBcAF4AIABiwGIAbgIkgEDNC42mAEAoAEByAEIwAEB&sclient=gws-wiz

    Front-End Alignment code editor extension - Google Search
        *>url  https://www.google.com/search?q=Front-End+Alignment+code+editor+extension&client=firefox-b-1-d&sxsrf=AOaemvIHj6q4I1a-t1xWkdtzpHFY3vrKLA%3A1637677913914&ei=WfucYaCXN5SSwbkPt_CCiAE&ved=0ahUKEwjgp8LS2a70AhUUSTABHTe4ABEQ4dUDCA0&uact=5&oq=Front-End+Alignment+code+editor+extension&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKsCMgUIIRCrAjIFCCEQqwI6BwgAEEcQsAM6BwgjELACECdKBAhBGABQ_gpYmyRg5yZoAXACeACAAYYBiAHXCZIBAzYuNpgBAKABAcgBCMABAQ&sclient=gws-wiz

    Versions: Front End Alignment - IntelliJ IDEs Plugin | Marketplace
        *>url  https://plugins.jetbrains.com/plugin/7465-front-end-alignment/versions

    Vertical code alignment. A coder named Terence Eden posted this… | by Tyler Neylon | Medium
        *>url  https://medium.com/@tylerneylon/vertical-code-alignment-9635bd2ee08c

    Do you guys "align" your code into columns? : readablecode
        *>url  https://www.reddit.com/r/readablecode/comments/19vkkz/do_you_guys_align_your_code_into_columns/

    atom-alignment
        *>url  https://atom.io/packages/atom-alignment

    GitHub - Freyskeyd/atom-alignment: Multi-line and multiple selection alignment package for atom
        *>url  https://github.com/Freyskeyd/atom-alignment

    String Formatting with str.format() in Python 3 | DigitalOcean
        *>url  https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3

    Built-in Types — Python 3.10.0 documentation
        *>url  https://docs.python.org/3/library/stdtypes.html

    Python String Methods
        *>url  https://www.w3schools.com/python/python_ref_string.asp

    Python 3 String Methods
        *>url  https://www.python-ds.com/python-3-string-methods

    Learn Python 3: Strings Cheatsheet | Codecademy
        *>url  https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-strings/cheatsheet

    Python String Methods | Programiz
        *>url  https://www.programiz.com/python-programming/methods/string

    Search · Sublime Alignment · GitHub
        *>url  https://github.com/search?q=Sublime+Alignment

    Search · python string utility · GitHub
        *>url  https://github.com/search?q=python+string+utility&type=Repositories

    GitHub - ikamensh/flynt: A tool to automatically convert old string literal formatting to f-strings
        *>url  https://github.com/ikamensh/flynt

    GitHub - daveoncode/python-string-utils: A handy Python library to validate, manipulate and generate strings
        *>url  https://github.com/daveoncode/python-string-utils

    GitHub - wroberts/fsed: Aho-Corasick string replacement utility
        *>url  https://github.com/wroberts/fsed

    stringutils/__init__.py at develop · huntie/stringutils · GitHub
        *>url  https://github.com/huntie/stringutils/blob/develop/stringutils/__init__.py


"""


import string
import itertools
import dis
import sys

import ex_helpers


# ---------------- helper functions ---------------
# ---- helper
def print_with_comment( a_comment, a_string ):
    """
    what it says, read
    print the comment then on nexts line the string, making its beginning and
    end clearer with >>><<<
    """
    print( "" )
    print( a_comment )
    print( f"    >>>{a_string}<<<")   # >>>to make clear where string starts and stops <<<

# ----  basics ------
# ----------------------------------------
def ex_literals():
    """
    what it says, read
    """
    ex_name  = "ex_literals"    
    print( f"""{ex_helpers.begin_example( ex_name )}
    including across lines special characters .....
    """ )

    print()
    print( "Simple string literal, you can use single or double quotes")
    test_string  = "this is a string"
    print_with_comment( "basic double quoted string literal:", test_string )

    print( )
    print( "For special characters like new line and tab, use a backslash")
    test_string  = "backslash escapes for a special character >\t<  "   # \n new line .....
    print_with_comment( "a backslash escape sequence example:", test_string )

    print()
    print( "An r in front ( without a space of the first quote makes a")
    print( "    a raw string, the backslash not longer denotes an escape sequence")
    test_string  = r"an r string diables the backslash escape this is a string with a special character >>>\1<<<"
    print_with_comment( "a r quote or raw string:", test_string )

    print()
    print( "Strings may be added with a + sign, and using parens, the code may" )
    print( "    span lines  ... note this is as fast for literals as having" )
    print( "    the string on just one line" )
    print( "    for literals this is optimized at compile time, no runtime" )
    print(  "    addition" )
    print( "Two line literal with + sign:" )
    test_string  = ( "line 1 " +
                  "line 2")
    print_with_comment( "strings added across 2 lines of code ", test_string )

    print()
    print( "Multi line literals do not even need + sign")
    print( "    this is just as optimized as with the + sign ")
    test_string  = (  "no + sign "
                      "line 1 "
                      "line 2" )

    print_with_comment( "miltline line liter in ()'s no +", test_string )

    print( "*** note above is also true for f-strings, see f-string example")

    # ---- f string on multiple lines -- parens required
    test_string      =  ( f"no + sign {'inside braces'}"
                          f"with var a_string"     # same result with or without f on this line
                          # having f does not generated a pylint complaint
                          f"line 2 {1+1}" )
    print_with_comment( "\nTN lines in () no +... include an f-string", test_string )

    # ---- repeat on one line -- gives same as above
    test_string      = (  f"no + sign {'inside braces'} with var a_string line 2 {1+1}" )
    print_with_comment( "\nTN lines in () no +... include an f-string", test_string )

    # same as above ???
    test_string  = (  "f-string: no + sign "
                      f"line 1 {1+1}"
                       "line 2 {2+2}")
    print_with_comment( "N lines to one with f string no +  BEST??", test_string )

    # ---- works but picks up lots of spaces on line 1 and 2
    test_string   = """triple quotes
                    line 1
                    line 2"""
    print_with_comment( "triple quotes give multiline and indent", test_string )

    ex_helpers.end_example( ex_name )  # not part of example, marks end

#ex_literals()
 

# ----------------------------------------
def ex_str_commands():
    ex_name  = "ex_str_commands"
    print( f"""{ex_helpers.begin_example( ex_name )}
    build strings to be used as commands to bash or sql....
    """ )

    print( )
    print( "example of long string to be as a linux command, hear with" )
    print( "raw strings can use regular strings or f strings, but do not mix" )
    print( "optimized at compile time, no runtime adding of strings" )
    cmd   = ( r'sudo mount -t cifs -o '
              r'username="russ",password="squeaksqueaksqueak",workgroup="MSHOME",'
              r'file_mode=0777,dir_mode=0777,nobrl,vers=1.0 '
              r'//192.168.0.170/share/_Source/rPi  /mnt/share1' )
    print_with_comment( "r string in () across multiple lines", cmd )

    print( )
    print( "example of an SQL command, a single line string wirtten")
    print( "across multiple lines")
    sql    = ( "SELECT timestamp_key, pressure_1, FROM well_data "
              "  WHERE ( timestamp_key > %s ) AND ( timestamp_key < %s ) "
              "order by gh_time asc"
             )
    print_with_comment( "sql in () across multiple lines", sql )

    print( )
    print( "example looking for a home" )
    print( "\nstrings may be added with a +" + " and new lines created with a backslash n")

    ex_helpers.end_example( ex_name )

#ex_str_commands()


#----- lists  split partition join
# ==========================================================
def ex_misc():
    ex_name  = "ex_misc"    
    print( f"""{ex_helpers.begin_example( ex_name )}
    character manipulation strip

    """)
    print( "\nstring.punctuation")
    for ix_char, i_char in enumerate(  string.punctuation ):
        print( f"{ix_char} >>{i_char}<<"  )

    # string.punctuation same as remove ascii??

    # from tweet app
    remove_ascii        = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"   # removable ascii

    print( "\nAscii Char List ( special )")
    for ix_char, i_char in enumerate( remove_ascii ):
        print( f"{ix_char} >>{i_char}<<"  )

    print( "\n\nlets try iterating with replace and ascii list")
    a_string   = "*the quick ? brown + or - fox !"
    print( f"string before >>{a_string}<<" )

    b_string = a_string
    for i_char in remove_ascii:
        b_string   = b_string.replace( i_char, "" )  # must be same string on both sides !

    print( f"string after >>{b_string}<<" )

    #----
    print( "\n\nlets try with strip -- works at ends ")

    # works only at ends perhaps apply at word level
    word   = "*the quick ? brown + or - fox !"
    print( f"word dressed {word}" )
    word = word.strip( string.punctuation ).lower()

    print( f"word stripped {word}" )

    ex_helpers.end_example( ex_name )  

#ex_misc()

# ==========================================================
def ex_join():
    ex_name  = "ex_join"    
    print( f"""{ex_helpers.begin_example( ex_name )}
    including across lines special characters .....
    """ )
    string_list    = ['this','is','a','sentence']
    join_string    = "-" # may be 0 to n char long
    joined         = join_string.join(string_list)
    print( f"join list >>{string_list}<<")
    print( f"with the string >>{join_string}<<")
    print(  f"gives >>{joined}<<" )
    ex_helpers.end_example( ex_name )   

#ex_join()


# ====================== helper ====================================
def part_report( to_partition, partition_with ):
    """
    helper function to show result of partition function
    read it
    """
    print( "\nPartition:")
    partition_0, partition_1, partition_2     =  to_partition.partition( partition_with )
    print( f"    partion target >>{to_partition}<<")
    print( f"    partition on >>{partition_with}<< \n        ----partition --- "
           f"0>>{partition_0}<<  1>>{partition_1}<<  2>>{partition_2}<<" )

# ====================== helper ====================================
def rpart_report( to_partition, partition_with ):
    """
    helper function to show result of rpartition function
    read it
    """
    print( "\nRight Partition:")
    partition_0, partition_1, partition_2     =  to_partition.rpartition( partition_with )
    print( f"    partion target >>{to_partition}<<")
    print( f"    partition on >>{partition_with}<< \n        ----partition --- "
           f"0>>{partition_0}<<  1>>{partition_1}<<  2>>{partition_2}<<" )

# --- breaking up  strings
# ----------------------------------------
def ex_partition():
    ex_name  = "ex_partition"   # end with >>    ex_helpers.end_example( ex_name )  # not part of example, marks end
    print( f"""{ex_helpers.begin_example( ex_name )}
        seperate string into 3 parts based on a given string
        seperate on a character how different from split
        Simply put, split will split the string at any occurrence of the given argument, while partition will only split the string
        at the first occurrence of the given argument and will return a 3-tuple with the given argument as the middle value.
        see also rpartition

    """)

    # sentence    = ['this.','is','a.','sentence']
    # new         = '-'.join(sentence)

    # print(f"string is {new}")

    # part        = new.partition( "." )
    # print( f"partion with . is {part}" )

    # part        = new.partition( "-" )
    # print( f"partion with - is {part}" )

    # part        = new.partition( "&" )
    # print( part )

    # word       =  "may_let_a new_relief program run out of money.
    #    https://t.co/2nihHg8DQw via @WSJ"
    # word       =  "https://t.co/2nihHg8DQw via @WSJ"
    # partition_url_0, partition_url_1, partition_url_2     =  word.partition( " " )
    # print( f"partition on ' ' >>>>>>partition tuple >>>>>>  {partition_url_0}< >
    #    {partition_url_1}< >{partition_url_2}<" )

    # word              =  "a https://t.co/2nihHg8DQw via @WSJ"  # url and 2 other words
    # partition_with    = "https"
    # part_report( word,  partition_with )

    # word              = "a https://t.co/2nihHg8DQw"    # leading word
    # partition_with    = "https"
    # part_report( word,  partition_with )

    # word              = "https://t.co/2nihHg8DQw trailing_word"    # trailing word
    # partition_with    = "https"
    # part_report( word,  partition_with )

    # word              = "https://t.co/2nihHg8DQw"    # just one url
    # partition_with    = "https"
    # part_report( word,  partition_with )

    # -------- right partition

    word              = "leading_word https://t.co/2nihHg8DQw trailing_word"    # trailing word
    partition_with    = "https"
    rpart_report( word,  partition_with )

    word              = "leading_word https://t.co/2nihHg8DQw"    # leading word
    partition_with    = "https"
    rpart_report( word,  partition_with )

    word              = "https://t.co/2nihHg8DQw trailing_word"    # trailing word
    partition_with    = "https"
    rpart_report( word,  partition_with )

    word              = "https://t.co/2nihHg8DQw"    # just one url
    partition_with    = "https"
    rpart_report( word,  partition_with )

    word              = "leading_word middle_word trailing_word"     # just one url
    partition_with    = "https"
    rpart_report( word,  partition_with )

    ex_helpers.end_example( ex_name )  # not part of example, marks end

#ex_partition()

# ----------------------------------------
def count_leading_spaces_1( a_string ):
    """
    helper function
    what it says, read
    https://stackoverflow.com/questions/13648813/what-is-the-pythonic-way-to-count-the-leading-spaces-in-a-string
    """
    leading_spaces   = sum( 1 for _ in itertools.takewhile( str.isspace, a_string ) )

    return leading_spaces

# ----------------------------------------
def count_leading_spaces_2( a_string ):
    """
    helper function
    what it says, read
    return:
        count of leading spaces
        https://stackoverflow.com/questions/13648813/what-is-the-pythonic-way-to-count-the-leading-spaces-in-a-string
    """
    leading_spaces   = len(a_string) - len( a_string.lstrip(' ') )

    return leading_spaces

# ----------------------------------------
def ex_count_leading_spaces():
    ex_name  = "ex_count_leading_spaces"
    print( f"""{ex_helpers.begin_example( ex_name )}
    demo simple but perhaps useful
    """)
    a_string      = "     i have n leading spaces"
    eval_string   = f"leading spaces in >>{a_string}<< =\n leading_spaces_1( a_string) = {count_leading_spaces_1( a_string)}"
    print( eval_string )
    #ex_helpers.eval_it( eval_string, msg = None )

    eval_string   = f"leading spaces in >>{a_string}<< =\n leading_spaces_2( a_string) = {count_leading_spaces_2( a_string)}"
    print( eval_string )

    ex_helpers.end_example( ex_name )

#ex_count_leading_spaces()

# ----------------------------------------
def ex_tokenize():
    ex_name  = "ex_tokenize"      
    print( f"""{ex_helpers.begin_example( ex_name )}
    looks like ex_partition() ??===============
    """)

    sentence    = ['this.','is','a.','sentence']
    new         = '-'.join(sentence)

    print(f"string is {new}")

    part        = new.partition( "." )
    print( f"partion with . is {part}" )

    part        = new.partition( "-" )
    print( f"partion with - is {part}" )

    part        = new.partition( "&" )
    print( part )
    ex_helpers.end_example( ex_name )
#ex_tokenize()

# ----------------------------------------
def ex_split():
    ex_name  = "ex_split"   
    print( f"""{ex_helpers.begin_example( ex_name )}
    rsplit
    see also ex_string_split which may be moved here
    also max occur
    """ )

    print( r"raw stirng" )

    # escape string The backslash (  \ ) character is used to escape characters that otherwise have a special ...
    "\""

    print(( "2.7.0_bf4fda703454".split("_") ))

     #res = test_string.rsplit(', ', 1)

    # use try except to see if conversion works
    a = "545.2222"
    print(( float(a) ))

    # can i convert, using try except

#ex_split()

# ---- find replace categorize  strings
# ----------------------------------------
def ex_finding():
    ex_name     = "ex_finding"
    print( f"""{ex_helpers.begin_example( ex_name )}
    find, begins with = startwith  ( in  contains: use find  )..... ===============
    How to Search within a String in Python
    https://www.dummies.com/programming/python/how-to-search-within-a-string-in-python/
    there is no in method or contains --- use find
    """ )
    #   str1.find(str, beg=0 end=len(string))
    #
    #    find1  = str1.find( "bar", 0, len(str1) )   # do not use default is to end
    #
    #    find1  = str1.find( "bar", 0, len(str1) )   # do not use default is to end

    #    Syntax
    #    str.find(str, beg=0, end=len(string))
    #    Parameters
    #    str -- This specifies the string to be searched.
    #
    #    beg -- This is the starting index, by default its 0.
    #
    #    end -- This is the ending index, by default its equal to the length of the string.
    #
    #    Return Value
    #    Index if found and -1 otherwise.

    str1 = "this is string example....wow!!!"
    str2 = "exam"
    print( "----testing find  ----- -1 not found else beginning loc " )
    print(( f"str1.find(str2) {str1.find(str2)}" ))   # find str2 in str1
    print(( str1.find(str2, 10, 50)))    # second arg is starting pos ??  third ending pos ??
    print(( str1.find(str2, 40)))

    print( "\n----testing find  ----- strip from end of str2 " )
    print(( f"find in  >>{str2}<<  in >>{str1}<<" ))   # find str2 in str1
    ix    =  str1.find( str2, 10)
    ix    =  str1.find( str2, )
    if ix >=0:
        print( f"found at {ix}" )
        print( f"cut out {str1[ix + len(str2): ]}"  )   # may not be best way to find
    else:
        print( "not found" )

    #if str1.

    # ---------------------------------

    """
    Return the lowest index in s where the substring sub is found such that sub is
    wholly contained in s[start:end]. Return -1 on failure. Defaults for start and end and
    interpretation of negative values is the same as for slices.

    string.find(s, sub[, start[, end]])
    """
    str1 = "this is string example not ....pow!!!"
    str2 = "exam"
    print( "\n----testing find in reverse not ----- -1 not found else beginning loc " )
    print(( f"find in reverse >>{str2}<<  in >>{str1}<<" ))   # find str2 in str1
    ix    =  str1.find( str2, - 1, 0 )
    if ix >=0:
        print( str1[ix + len(str2): ] )
    else:
        print( "not found" )

    print( "\n----testing in  -----" )
    foo = "blahblahblah"
    bar = "somethingblahblahblahmeep"
    if foo in bar:
        print( "foo was in bar do something" )
    else:
        print( "foo NOT in bar do something" )

    # Second the string.find() and string.index() actually return the index of a substring.
    # The only difference is how they handle the substring not found situation:
    # string.find() returns -1 while string.index() raises an ValueError.

    a_string    = "*>bat and then some more stuff "
    print( a_string )
    print(( a_string.startswith( "*>bat" ) ))  #str, beg=0,end=len(string));  is beginswith
    # do not use is "" use == ""
    #if not my_string:
    #However, you may want to strip white space because:

    a_string    = ">bat and then some more stuff "
    print( a_string )
    print( f'a_string.startswith( "*>bat" ) {a_string.startswith( "*>bat" )}'  )
        #str, beg=0,end=len(string));

    a_string = "this is string example....wow!!!"
    print( a_string.startswith( 'this' ))
    print( a_string.startswith( 'is', 2, 4 ))
    print( a_string.startswith( 'this', 2, 4 ))

    print( f"test endswith >{a_string.endswith( 'this', 2, 4 )}<" )

    ex_helpers.end_example( ex_name )

#ex_finding()


# ----------------------------------------
def ex_rfinding():
    ex_name  = "ex_rfinding"    
    print( f"""{ex_helpers.begin_example( ex_name )}
    and rpartition  .....
    """ )

    """
    Following is the syntax for rfind() method −

    obj.rfind(str, beg=0 end=len(string))
    Parameters
    str − This specifies the string to be searched.

    beg − This is the starting index, by default its 0.

    end − This is the ending index, by default its equal to the length of the string.

    """
    str1 = "foo bar foobar squeak is a great bar cat perhaps not in a hat"
    str2 = "bar"

    print( f"rfind >>{str2}<< in  >>{str1}<<")
    ix    =  str1.rfind( str2,   )
    print(  f"   ix is {ix}" )

    """
    The rpartition method returns a 3-tuple containing:

    the part before the separator,
    separator parameter,
    and the part after the separator if the separator parameter is found in the string
    two empy strings, followed by the string itself if the separator parameter is not found
    """
    print( "\n-----------------------")
    a_rpartition    =  str1.rpartition( str2 )
    print(  f"a_rpartition is >>{a_rpartition}<<" )
    print(  f"a_rpartition \n    1>>{str2}<<\nin  2>>{str1}<<")
    print( "\n gives:" )
    print(  f"   0 >>{a_rpartition[ 0 ]}<< " )
    print(  f"   1 >>{a_rpartition[ 1 ]}<< " )
    print(  f"   2 >>{a_rpartition[ 2 ]}<< " )
    if a_rpartition[0] == "":
        msg = "not found "
        print( msg )
    else:
        msg = "found "
        print( msg )
        print( f"re assemble as if prefix  >>{a_rpartition[ 1 ] + a_rpartition[ 2 ]}<<" )

#ex_rfinding()

#   str1.find(str, beg=0 end=len(string))
#
#    find1  = str1.find( "bar", 0, len(str1) )   # do not use default is to end
#
#    find1  = str1.find( "bar", 0, len(str1) )   # do not use default is to end

#    Syntax
#    str.find(str, beg=0, end=len(string))
#    Parameters
#    str -- This specifies the string to be searched.
#
#    beg -- This is the starting index, by default its 0.
#
#    end -- This is the ending index, by default its equal to the length of the string.
#
#    Return Value
#    Index if found and -1 otherwise.

#    print(( str1 [find1:find1+3] ))

# ----------- helper ---------------------
def if_startswith_list( a_line ):
    """
    helper function for ??
    check if string starts with anything from a list of items

    """
    check_list  = [ "!", "#",]
    check_list  = [ "skip ",  "adding" ]

    for i_check in check_list:
        if a_line.startswith( i_check ):
            return True

    return False

# ----------------------------------------
def ex_findreplace():
    ex_name  = "ex_findreplace"    
    print( f"""{ex_helpers.begin_example( ex_name )}
    find, replace ..... can delete if replace with ""  
    but strings are immutable so it produces a new string not mututate an old one
    """ )

    str1  = "foo, bar, foobar squeak is a great cat"
    print( f"original >> {str1}" )

    str2  = str1.replace( 'bar ', '-bar- ' )
    print( f"replaced >> {str2}" )

    str2  = str1.replace( 'bar, ', '-bar,- ' )

    print( f"replaced >> {str2}" )

    a_string = "this is string example....wow!!! this is really string"
    print( a_string )
    print(( a_string.replace("is", "was")  ))
    print(( a_string.replace("is", "was", 3) ))
    print( "can use as a delete" )
    print( "see translate" )
    #s .translate(table[, deletechars]);
    #s = s.replace("World", "")
    ex_helpers.end_example( ex_name )  

#ex_findreplace()


# ==========================================================
def ex_upper_lower():
    ex_name  = "ex_upper_lower"
    print( f"""{ex_helpers.begin_example( ex_name )}
    convert case upper lower capitalize title

    """ )

    a_string   = "FOR EXAMPLE: this is originally lower case "
    new = str.lower( a_string )
    print ( new )

    # both of next work
    newer   = str.upper( a_string )
    newer   = a_string.upper()
    print( newer )
    test_str = "geeksforgeeks and other gods"

     # printing original string
    print("The original string is : " + str(test_str))

    # Using capitalize() + string slicing
    # Initial character upper case
    res = test_str.capitalize()
    print(f"the result of capitalize is >{res}<")

    print( "hello world as a title".title() )
    ex_helpers.end_example( ex_name )

#ex_upper_lower()

#eval( "ex_upper_lower()" )     
#dis.dis( ex_upper_lower  )    

# ==========================================================
def ex_strip_split():
    ex_name  = "ex_strip_split"   # end with >>    ex_helpers.end_example( ex_name )  # not part of example, marks end
    print( f"""{ex_helpers.begin_example( ex_name )}
    moved to split and strip.py ??
    this is an example of string spliting and stripping
    much content has been moved to another file 
    strip is trim, there is a lstrip and rstrip, you can sepify the characters
    """ )

    str_0 = "   Line1-abcdef \nLine2-abc \nLine4-abcd    "

    str_1 = str_0.split( )    # default to new line ?  what happened to blanks
    print( str_1 )
    #print str.split(' ', 1 )
    for junk in str_1:
        junk_1 = junk.strip()    # no strip necessary ?
        print( junk )
        print( junk_1 )

    print( "--- pt 2 ---" )
    str_0 = "Line1 abcdef \nLine2 abc \nLine4 abcd"

    str_1 = str_0.split( "\n" )
    print( str_1 )
    #print str.split(' ', 1 )
    for junk in str_1:
        junk_1 = junk.strip()
#        The method strip() returns a copy of the string in which all chars have been stripped
#        from the beginning and the end of the string (default whitespace characters).

        print( junk_1 )
    ex_helpers.end_example( ex_name )  # not part of example, marks end

#ex_strip_split()

# ---------------- helper ------------------------
def is_not_empty( a_string ):
    """

    is this even right ??
    """
    return bool( a_string and a_string.strip())

# ----------------------------------------
def ex_truth_of_strings():
    ex_name  = "ex_truth_of_strings"    
    print( f"""{ex_helpers.begin_example( ex_name )}
    """ )

    # do not use is "" use == ""
    #if not my_string:
    #However, you may want to strip white space because:

    print(( bool("") ))
     #False
    print(( bool("   ") ))
     #True
    print(( bool("   ".strip()) ))
     #False

    print( "===== is not empty ====== " )
    print(( is_not_empty("")    )) # False
    print(( is_not_empty("   ") )) # False
    print(( is_not_empty("ok")  )) # True
    print(( is_not_empty(None)  )) # False


#ex_truth_of_strings()

# ---- applications


# ----------------------------------------
def substitute_into_string( a_string, sub_list ):
    """
    seems ok ?
    """
    for i_sub in sub_list:
        a_string  = a_string.replace( *i_sub )   # !! even if not found

    return a_string

# ----------------------------------------
def substitute_into_string_list( a_string_list, sub_list ):
    """
    really just for testing
    """
    # !! switch to list comp
    for ix_string, i_string in enumerate( a_string_list ):
        i_string = substitute_into_string( i_string, sub_list )
        a_string_list[ ix_string ] = i_string

    return a_string_list

# ----------------------------------------
def ex_substitute_into():
    ex_name  = "ex_substitute_into"    
    print( f"""{ex_helpers.begin_example( ex_name )}
    a little application function; see code
    """ )
    subs       = [ ("<old>",   "new" ),
                   ("<old_1>", "new 1" ),
                   ("<old_2>", "new two" ),
                 ]
    print( f"use the following list of substutions: \n {subs}" )

    a_string     = "i was too <old> but later i grew to <old_2> years"
    print( f"\ninitial string >>{a_string}<<")

    new_string   = substitute_into_string( a_string, subs )
    print( f"becomes        >>{new_string}<<")

    print( )
    print( "next apply list to a list of strings")
    a_string_list   = [ a_string,
                        a_string,
                        "i was too <old_1> but later i grew to <old> years",
                       ]

    new_list     = substitute_into_string_list( a_string_list, subs )

    print( new_list )

    ex_helpers.end_example( ex_name )  
    
#ex_substitute_into()

# ----------------------------------------
def ex_is_numeral():
    ex_name  = "ex_is_numeral"   # end with >>    ex_helpers.end_example( ex_name )  # not part of example, marks end
    print( f"""{ex_helpers.begin_example( ex_name )}
    copy and paste fix  .....
    """ )

    ex_helpers.end_example( ex_name )

#     user_input = input("Enter your Age")
# try:
#     val = int(user_input)
#     print("Input is an integer number. Number = ", val)
# except ValueError:
#     try:
#         val = float(user_input)
#         print("Input is a float  number. Number = ", val)
#     except ValueError:
#         print("No.. input is not a number. It's a string")
# Output: Run Online


# user_number  = input("Enter your number")
# if( user_number.isdigit()):
#     print("User input is Number ")
# else:
#     print("User input is string ")


#  def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass

#     try:
#         import unicodedata
#         unicodedata.numeric(s)
#         return True
#     except (TypeError, ValueError):
#         pass

# return False

# """

#ex_is_numeral()



