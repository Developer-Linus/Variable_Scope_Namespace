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
## Best Practices for Variable Scope
- Favor local variables for function-specific data.
- Use global variables sparingly and only when truly necessary.
- Consider using nonlocal variables for modifying variables from enclosing functions.

## Exploring Namespaces
- **Namespace** is like a container that holds names (variables, functions, classes, etc) mapped to their corresponding objects (values, codeblocks, etc).
- Help in organizing and managing names in code to avoid conflicts between different parts of the program.
### Preventing Naming Conflicts
- Consider a scenario where you've two variables with same name but different purposes in your code. Without namespaces, there would be ambiguity, and Python wouldn't know which variable you're referring to.
### Types of Namespaces
(a) *Built-in Namespace*: contains built-in functions and variables accessible throughout your program (e.g, print, len). <br>
(b) *Global Namespace*: Holds variables defined at the top level of your script or module. <br>
(c) *Local Namespace*: Created for each function and block, containing local variables defined with that scope.
(d) *Module namespace*: Each imported module has its own namespace to avoid conflicts with global names.
### Namespace Lifecyle and Scope Resolution
1. **Global Namespace**: When you start a Python program, a global namespace is created. This namespace holds names (variables, functions, classes) defined at the outermost level of your code, outside of any functions or classes. <br>
2. **Local Namespace (function scope)**: Whenever a function is callled, a new local namespace is created for that function. This namespace contains names specific to that function including function parameters and local variables defined inside the function. <br>
3. **Scope Resolution and LEGB Rule**: 
- *L*: Python first looks for a variable name in the local namespace (current function scope). If the variable is found, Python uses that value.
- *E*: If the variable is not found in the local namespace, Python searches in the enclosing (or non-local) namespaces. This process continues until the variable is found or until the global namespace is reached. <br>
- *G*: If the variable is not found in the local or enclosing namespaces, Python looks in th global namespace (module-levle scope). <br>
- *B*: If the variable is not still found, Python checks the built-in namespace, which contains built-in functions and objects. 


# Exercises
## Exercise 1: Local vs Global Scope Instruction:

- Define a variable with the same name in both global and local scopes within a function.
- Print the variable from inside the function and outside the function, observing how Python accesses each variable based on its scope (local vs global).
## Exercise 2: Namespace Exploration Instruction:

- Create a Python script with two functions, each defining a variable with the same name but with different purposes (e.g., count variable in a counting function and a logging function).
- Call both functions and print the variable inside each function, observing how namespaces keep variables separate within functions.

## Exercise 3: Scope Hierarchy Instructions
* Define a variable in the global scope, then create a function with an enclosing scope that redefines a variable with the same name. * Inside this function, access both the global and enclosing variables and print their values. * Discuss with comments in the code how Python follows the LEGB rule for variable lookup.