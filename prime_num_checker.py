while True:
    def prime_checker(number):
        is_prime = True
        for i in range(2,n):
            if n%i == 0:
              is_prime = False
        if is_prime == True:
            print("Its a prime number.")
        else:
            print("Its not a prime number.")
            
    n = int(input("Provide the number that you want to check: "))
    prime_checker(number=n)
    