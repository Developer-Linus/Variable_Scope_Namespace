# Variable Scope and NameSpace In Python
- Essential for effective variable management.
- Ensure clean code and error-free program
## Variable Scope
- Defines the accessibility of variable within a code.
### Types of Scope (LEGB Rule)
- Python program follows LEGB rule when trying to access a variable.
(a) **L(Local)**: Variables defined within a function or block have local scope. They're only accessible within that function or block. <br>
(b) **E(Enclosing)**: If a variable is not found locally, Python searches enclosing functions (nested functions) for variable. <br>
(c) **G(Global)**: Variables defined outside all functions have global scope. They are accessible from anywhere in the program. <br>
(d) **B(Built-In)**: Built-in functions and variables are part of Python's core functionality and are always accessible.