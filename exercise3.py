y= 20 # Global variable

def outer_function():
    y = 3
    def inner_function():
        global y
        print(f"The global value is {y}")
        enclosing_y = 3
        print(f"The enclosing value is {enclosing_y}")
    inner_function()
outer_function()

# Extra Example
# Step 1: Define a global variable
x = "Global Variable"

# Step 2: Create a function with an enclosing scope
def enclosing_function():
    # Redefine the variable within the enclosing scope
    x = "Enclosing Variable"
    
    # Step 3: Create an inner function to access both variables
    def inner_function():
        # Access the global variable
        global x
        print("Global x:", x)
        
        # Access the enclosing variable
        enclosing_x = "Enclosing Variable"
        print("Enclosing x:", enclosing_x)
    
    # Call the inner function
    inner_function()

# Call the enclosing function
enclosing_function()


'''
LEGB RULE
- first, the python program checks for the variable within the block of the function.
- If the variable is not in the function code block, the program looks for the variable in the enclosing scope. If it finds, it uses it.
- If the variable is not in local scope and enclosing scope, the program looks for variable in global scope as defined in the top most level of the program.
- If it is not in the global scope, it looks for the variable in the built-in scope. 
'''


