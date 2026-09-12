# Q1. InvalidAgeError naam ki custom exception class banao (koi extra logic nahi, sirf pass).
class InvalidAgeError(Exception):
    pass

# Q2. Ek function check_age(age) likho jo agar age < 0 ho to InvalidAgeError raise kare 
# with message "Age cannot be negative". Fir usay try/except mein call karo aur error message print 
# karo.
def checkAge(age):
    if age<0:
        raise InvalidAgeError("Age cannot be negative")

try:
    checkAge(-6)
except InvalidAgeError as e:
    print("Invalide Age ",e)    

# Q3. Ek retry loop likho jo function unstable_task() ko max 3 attempts tak try kare.
# Agar ConnectionError aaye to retry karo, warna (agar success ho) "Task completed" print karke 
# loop se nikal jao.Agar 3 attempts ke baad bhi fail ho to "All attempts failed" print karo
def unstable_task():
    raise ConnectionError("unstable connection")
max_attempt=3

for attempt in range(1,max_attempt+1):
    try:
        unstable_task()
        print("Task completed")
        break
    except ConnectionError as e:
        print("Retry", e)
        if attempt==max_attempt:
            print("All attempt failed")


print ("new prac")
# 1. Write safe_divide(a, b) that catches ZeroDivisionError and returns None instead of crashing.
def safe_divide(a,b):

    try:
        return a/b
    except ZeroDivisionError:
        return None  

safe_divide(10,0)    #to check

# 2. Write safe_int(value) that tries to convert value to an int, catches ValueError , and returns 0 if it fails.
def safe_int(value):
    
    try:
        return int(value)
    except ValueError:
        return 0 

# 3. Create a custom exception InvalidAgeError(Exception) . Write validate_age(age) that raises it if age is
# negative.
class InvalidAgeError(Exception):
    pass

def validate_age(age):
    if age<0:
        raise InvalidAgeError("Age cannot be negative")

try:
    validate_age(-6)
except InvalidAgeError as e:
    print("Invalide Age ",e)    
# 4. Write a function that tries something 3 times before giving up, printing “Attempt 1”, “Attempt 2”, etc.
# (simulate failure with a counter)
def something():
    raise ValueError("failed")

max_attempt= 3
for attempt in range(1, max_attempt+1):
    print(f"Attempt {attempt}")
    try:
        something()
        print("success")
        
    except ValueError:
        if attempt== max_attempt:
            print("failure")
             
            
            