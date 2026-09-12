# Build: A SafeExecutor — a small reusable retry helper. What it should do: A function
# run_with_retries(func, max_attempts=3) that calls func() , and if it raises an exception, tries again, up to
# max_attempts times, then raises a clear final error. Test it against a fake function that fails the first 2 times
# then succeeds. Files: week1/day03_safe_executor.py

calls=[0]
def func():
    calls[0]+=1
    if calls[0]<3 :
        raise Exception("Try again")
    return("success")  

def run_with_retries(func,max_attempts=3):
    for attempt in range(1,max_attempts+1):
        try:
           result=func()
           return result
        except Exception as e:
            if attempt==max_attempts:
               raise RuntimeError("FAIL to load function",e)
            
print(run_with_retries(func))
            

# CHALLENGE
# You’ll soon call a real API that can fail with different error types (network error vs invalid input). Write 2
# custom exceptions: RetryableError and PermanentError . Write a function that decides which type to raise
# based on a fake “status code” input (e.g., 500 = retryable, 400 = permanent), and only retries on
# RetryableError . Try for 20–30 minutes before looking anything up

class RetryableError(Exception):
    pass
class PermanentError(Exception):
    pass

def  function(status_code):
    if status_code >=500:
        raise RetryableError("Retry")
    elif status_code==400:
        raise PermanentError("permanent")
    else:
        return "Success in Status code"


def retries(function,max_attempt=3):
    
    for attempt in range(1, max_attempt+1):
        print(f"Attempt {attempt}")
        try:
            result=function()
            return result
        except RetryableError as e:
            if attempt== max_attempt:
                raise 
        except PermanentError as e:
            raise 

try:
    print(retries(lambda: function(500)))   # retryable test
except Exception as e:
    print("Final Error:", e)

try:
    print(retries(lambda: function(400)))   # permanent test
except Exception as e:
    print("Final Error:", e)


    
     


        