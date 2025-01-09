count = 10 # Global variable

def outer_function():
    count = 5 # Local variable within outer_function
    def inner_function():
        count = 2 # Local variable within inner_function
        print(f"Inner function: {count}") # Accesses local count(2)
    inner_function()
    print(f"outer function: {count}") # Access local count(5)
print(f"Global scope: {count}") # Accesses global count(10)
outer_function()