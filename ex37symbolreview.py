#!/usr/bin/env python

# Printing of Symbol Review page.

print "----------KEYWORDS----------"
print "Keyword           | Description                                       | Example"
print "and               | Logical and.                                      | True and False == False"
print "as                | Part of the with-as statement.                    | with X as Y: pass"
print "assert            | Assert (ensure) that something is true.           | assert False, 'Error!'"
print "break             | Stop this loop right now.                         | while True: break"
print "class             | Define a class.                                   | class Person(object)"
print "continue          | Don't process more of the loop, do it again.      | while True: continue"
print "def               | Define a function.                                | def X(): pass"
print "del X[Y]          | Delete from dictionary.                           | del X[Y}"
print "elif              | Else if condition.                                | if: X; elif: Y; else: J"
print "else              | Else condition.                                   | if: X; elif: Y; else: J"
print "except            | If an exception happens, do this.                 | except ValueError, e: print e"
print "exec              | Run a string as Python.                           | exec \'print \"hello\""
print "finally           | Exceptions or not, finally do this no matter what.| finally: pass"
print "for               | Loop over a collection of things.                 | for X in Y : pass"
print "from              | Importing specific parts of module.               | from x import Y"
print "global            | Declare that you want a global variable.          | global X"
print "if                | If condtion.                                      | if: X; elif: Y; else: J"
print "import            | Import a module into this one to use.             | import os"
print "in                | Part of for-loops .Also a test of X in Y.         | for X in Y: pass also 1 in [1] == True"
print "is                | Like == to test equality.                         | 1 is 1 == True"
print "lambda            | Create a short anonymous function.                | s = lambda y: y ** y; s(3)"
print "not               | Logical not.                                      | not True == False"
print "or                | Logical or.                                       | True or False == False"
print "pass              | This block is empty.                              | def empty(): pass"
print "print             | Print this string.                                | print \'this string\'"
print "raise             | Raise an exception when things go wrong.          | raise ValueError(\"No\")"
print "return            | Exit the function with a return value.            | def X(): return Y"
print "try               | Try this block, and if exeption, go to except.    | try: pass"
print "while             | While loop.                                       | While X: pass"
print "with              | with an expression as a variable do.              | with X as Y: pass"
print "yield             | Pause here and return to caller.                  | def X(): yield Y; X().next()"

print ""
print "----------DATA TYPES----------"
print "Type     | Description                              | Example"
print "True     | True boolean value.                      | True or False == True"
print "False    | False boolean value.                     | False and True == False"
print "None     | Represents \"nothing\" or \"no value\".      | x = None"
print "strings  | Stores textual information.              | x = \"hello\""
print "numbers  | Stores integers.                         | i = 100"
print "floats   | Stores decimals.                         | i = 10.389"
print "lists    | Stores a lists of things.                | j = [1,2,3,4]"
print "dicts    | Stores a key=value mapping og things.    | e = {'x': 1, 'y': 2}"
 
print ""
print "----------STRING ESCAPE SEQUENCES----------"
print "Escape  | Description"
print "\\\\      | Backslash"
print "\\\'      | Single-quote"
print "\\\"      | Double-quote"
print "\\a      | Bell"
print "\\b      | Backspace"
print "\\f      | Formfeed"
print "\\n      | Newline"
print "\\r      | Carriage"
print "\\t      | Tab"
print "\\v      | Vertical"

print ""
print "----------STRING FORMATS----------"
print "Escape  | Description                               | Example"
print "%d      | Decimal integers(not floating point).     | \"%d\" % 45 == \'45\'"
print "%i      | Same as %d.                               | \"%i\" % 45 == \'45\'"
print "%o      | Octal number.                             | \"%o\" % 1000 == \'1750\'"
print "%u      | Unsigned decimal.                         | \"%u\" % -1000 == \'-1000\'"
print "%x      | Hexadecimal lowercase.                    | \"%x\" % 1000 == \'3e8\'"
print "%X      | Hexadecimal uppercase.                    | \"%X\" % 1000 == \'3E8\'"
print "%e      | Exponential notation, lowercase \'e\'.      | \"%e\" % 1000 == \'1.000000e+03\'"
print "%E      | Exponential notation, uppercase \'E\'.      | \"%E\" % 1000 == \'1.000000E+03\'"
print "%f      | Floating point real number.               | \"%f\" % 10.34 == \'10.340000\'"
print "%F      | Same as %f.                               | \"%F\" % 10.34 == \'10.340000\'"
print "%g      | Either %f or %e, whichever is shorter.    | \"%g\" % 10.34 == \'10.34\'"
print "%G      | Same as %g but uppercase.                 | \"%G\" % 10.34 == \'10.34\'"
print "%c      | Character format.                         | \"%c\" % 34 == \'\"\'"
print "%r      | Repr format (debugging format).           | \"%r\" % int == \"<type \'int\'\>\""
print "%s      | String Format.                            | \"%s there\" % \'hi\' == \'hi there\'"
print "%%      | A percent sign.                           | \"%g%%\" % 10.34 == \'10.34%\'"

print ""
print "----------OPERATORS----------"
print "Operator  | Description                          | Example"
print "+         | Addition                             | 2 + 4 == 6"
print "-         | Subtraction                          | 2 - 4 == -2"
print "*         | Multiplication                       | 2 * 4 == 8"
print "**        | Power of                             | 2 ** 4 == 16"
print "/         | Division                             | 2 / 4.0 == 0.5"
print "//        | Floor Division                       | 2 // 4.0 == 0.0"
print "%         | String interpolate or modulus        | 2 % 4 == 2"
print "<         | Less than                            | 4 < 4 == False"
print ">         | Greater than                         | 4 > 4 == False"
print "<=        | Less than equal                      | 4 <= 4 == True"
print ">=        | Greater than equal                   | 4 >= 4 == True"
print "==        | Equal                                | 4 == 5 == False"
print "!=        | Not equal                            | 4 != 5 == True"
print "<>        | Not equal                            | 4 <> 5 == True"
print "( )       | Parenthesis                          | len(hi) == 2"
print "[ ]       | List brackets                        | [1,3,5]"
print "{ }       | Dict curly braces                    | {'x': 5, 'y': 10}"
print "@         | At (decorators)                      | @classmethod"
print ",         | Comma                                | range(0, 10)"
print ":         | Colon                                | def X():"
print ".         | Dot                                  | self.x = 10"
print "=         | Assign equal                         | x = 10"
print ";         | semi-colon                           | print \"hi\"; print \"there\""
print "+=        | Add and assign                       | x = 1; x += 2"
print "-=        | Subtract and assign                  | x = 1; x -= 2"
print "*=        | Multiply and assign                  | x = 1; x *= 2"
print "/=        | Divide and assign                    | x = 1; x /= 2"
print "//=       | Floor divide and assign              | x = 1; x //= 2"
print "%=        | Modulus and assign                   | x = 1; x %= 2"
print "**=       | Power assign                         | x = 1; x **= 2"
