multiplo = 3

for i in range(1, 101):
    if i % multiplo == 0:
        print("Fizz")
    else:
        print(i)

    if i % 5 == 0:
        print("Buzz") 

    if i % multiplo == 0 and i % 5 == 0:
        print("FizzBuzz")