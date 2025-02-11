cube = lambda x: x ** 3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    
    fib_numbers = [0,1]
    
    for _ in range(n - 2):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
        
    return fib_numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))