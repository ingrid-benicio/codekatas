def sum_of_positive(numbers):
    total = 0 # this variable will going to hold the sum of the numbers greater than 0
    for i in numbers:
        if i > 0:
            total = total + i # other way to do this is total += i, but i dont know this too well so i used the way i know how to do. 
    return total 
    

print(sum_of_positive([-1,2,3,4,-5]))

# also, i needed some help in this kata so i used this video https://www.youtube.com/watch?v=vLsLOXrJolQ to understand how to do and where i was getting wrong
