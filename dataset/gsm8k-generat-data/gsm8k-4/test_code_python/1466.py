def solution():
    """A dog barks 30 times per minute. If 2 dogs bark 30 times per minute, how many times will they have barked after 10 minutes?"""
    # Define the number of dogs and the barking rate per dog
    num_dogs = 2
    barking_rate = 30

    # Calculate the total number of barks in 10 minutes
    total_barks = num_dogs * barking_rate * 10

    # return the result
    result = total_barks
    return result

print(solution())