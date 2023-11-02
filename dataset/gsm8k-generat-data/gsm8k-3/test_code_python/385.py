def solution():
    """Anna baked 60 cupcakes. She gives away 4/5 of the cupcakes to her classmates. Of the remaining 1/5 of cupcakes, she eats 3 cupcakes. How many cupcakes does she have left?"""
    # Define the number of cupcakes Anna baked
    total_cupcakes = 60

    # Calculate the number of cupcakes Anna gives away
    given_cupcakes = total_cupcakes * 4 / 5

    # Calculate the number of cupcakes Anna has left
    remaining_cupcakes = total_cupcakes - given_cupcakes

    # Eat 3 cupcakes
    remaining_cupcakes -= 3

    # Display the number of cupcakes Anna has left
    result = remaining_cupcakes
    return result

print(solution())