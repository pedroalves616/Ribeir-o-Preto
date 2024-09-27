def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > n:
            break
        fib_sequence.append(next_fib)
    return fib_sequence

def is_fibonacci_number(num):
    if num < 0:
        return False
    fib_sequence = fibonacci_sequence(num)
    return num in fib_sequence

# Solicita ao usuário para inserir um número
number = int(input("Digite um número: "))

# Verifica se o número pertence à sequência de Fibonacci
if is_fibonacci_number(number):
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} NÃO pertence à sequência de Fibonacci.")
