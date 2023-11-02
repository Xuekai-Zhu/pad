def solution():
    
    dozens_of_cupcakes = 2.5
    total_cupcakes = dozens_of_cupcakes * 12
    total_people = 27+1+1-3
    cupcakes_given = total_people
    cupcakes_left = total_cupcakes - cupcakes_given
    result = cupcakes_left
    return result

print(solution())