# For: fizzbuzz.py
def fizzbuzz(upto):
    num = 1
    while num < upto:
        if (num % 3) and (num % 5) == 0:
            print("Fizzbuzz", end=', ')
            num = num + 1
        elif (num % 3) == 0:
            print("Fizz", end=', ')
            num = num + 1
        elif (num % 5) == 0:
            print("Buzz", end=', ')
            num = num + 1
        else:
            print(num, end=', ')
            num = num + 1
    
    print('')

#spent a bit too much time on this. I think the way
# was to have results not printed but added to a list
# , then you split them out, then you join them with comma
# separation. this would allow you to test the object list
# in the unittest, meaning you could say "X in OBJECT", IF X % 3 AND 5 = fizzbuzz etc