def solution():
    """Harly's animal shelter has 80 dogs. She adopts out 40% of them but then has to take back 5 because of personality conflicts with other dogs in their adopted homes. How many dogs does she have now?"""
    # Define the initial number of dogs
    INITIAL_DOGS = 80

    # Calculate the number of dogs adopted out
    adopted_dogs = INITIAL_DOGS * 0.4

    # Calculate the number of dogs returned
    returned_dogs = 5

    # Calculate the final number of dogs
    final_dogs = INITIAL_DOGS - adopted_dogs + returned_dogs

    # Return the result
    result = final_dogs
    return result

print(solution())