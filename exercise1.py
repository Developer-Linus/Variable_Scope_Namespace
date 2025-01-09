x = 10 # Global variable

# Function with same variable name inside it as local variable
def get_value():
    x = 8 # Local variable with same name as global variable
    print(f"The value of x is {x}")
get_value()
print(f"The global value of x is {x}")