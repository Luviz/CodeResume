def fizzBuzz_readable(n):
    ret = ''
    if n % 3 == 0:
        ret += "Fizz" 
    if n % 5 == 0:
        ret += "Buzz" 

    return ret if len(ret) > 0 else n 

def fizzBuzz(n): 
    ret = "Fizz" if n % 3 == 0 else ""
    ret += "Buzz" if n % 5 == 0 else ""
    return ret if len(ret) > 0 else n 


if __name__ == "__main__":
    print([fizzBuzz(n) for n in range(1,50)])