def solution():
    # Calculate the total number of cupcakes before Carla gives some to her dogs
    total_cupcakes = 65 * 45  

    # Calculate the total number of cupcakes after Carla gives some to her dogs
    cupcakes_left = total_cupcakes - (5 * 45) 

    # Calculate the number of cupcakes each of the daughter's friends ate
    friends = 19  # The daughter and 18 friends shared the remaining cupcakes
    cupcakes_per_person = cupcakes_left / friends  
    result = cupcakes_per_person
    return result

print(solution())