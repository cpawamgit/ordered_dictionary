#!/usr/local/bin/python3
import time

def time_controller(this_function):
    
    def modified_function():
        before = time.time()
        this_function()
        after = time.time()
        total_time = after - before
        print("this function : {} has taken {} seconds to run".format(this_function, total_time))
        return this_function
    return modified_function

@time_controller
def display():
    i = 0
    while i < 1000000:
        print("something to print")
        i += 1

display()