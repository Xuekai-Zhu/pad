def solution():
    """Anna baked 60 cupcakes. She gives away 4/5 of the cupcakes to her classmates. Of the remaining 1/5 of cupcakes, she eats 3 cupcakes. How many cupcakes does she have left?"""
    # Define the initial number of cupcakes
    num_cupcakes = 60

    # Calculate the number of cupcakes given away
    given_away = num_cupcakes * (4/5)
    
    # Calculate the number of cupcakes remaining
    remaining = num_cupcakes - given_away
    
    # Subtract the number of cupcakes Anna ate
    remaining -= 3
    
    result = remaining
    return result

print(solution())