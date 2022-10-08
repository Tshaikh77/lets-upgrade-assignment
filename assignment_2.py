
# Write a Program which has function to find out a number is prime or not

def number(prime_or_not):
    if prime_or_not == 1 :
      print("1 is neither prime nor composite")
      
    for x in range(2, prime_or_not):
        if prime_or_not % x == 0 :
            print(str(prime_or_not) + " is not a prime no.")
            break
    else:
      if prime_or_not != 1:
        print(str(prime_or_not) + " is a prime no.")


number(2)
number(3)
number(7)
number(10)
number(1)
