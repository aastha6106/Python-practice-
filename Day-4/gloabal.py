
count = 10

def display_count():
    """Function that accesses the global variable"""
    print("Global variable 'count':", count)

def modify_count():
    """Function that modifies the global variable"""
    global count
    count = 20
    print("Modified global variable 'count':", count)

display_count()      
modify_count()       
display_count()      
