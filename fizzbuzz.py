# my code is now here I know its not the most efficient possible 
# I wanted to try this method to see if it works

printword = []
for number in range(1, 101):
    divisible3 = number % 3
    divisible5 = number % 5
    if divisible3 == 0 and divisible5 == 0:
        printword.append('FizzBuzz')
    elif divisible3 == 0:
        printword.append('Fizz')
    elif divisible5 == 0:
        printword.append('Buzz')
    else:
        printword.append(str(number))

print(' '.join(printword))
