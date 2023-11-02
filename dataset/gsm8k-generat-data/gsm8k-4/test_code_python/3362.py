def solution():
    """The American swallow can lift into the air and carry a maximum of 5 pounds of weight, while the European swallow can lift and carry twice the weight as the American swallow. If there was a flock of 90 swallows, containing twice as many American as European swallows, what is the maximum combined weight the flock can carry?"""
    # Define the weight capacity of the American and European swallows
    american_capacity = 5
    european_capacity = 2 * american_capacity

    # Define the number of American and European swallows
    american_count = 2/3 * 90
    european_count = 1/3 * 90

    # Calculate the maximum weight the flock can carry
    max_weight = american_count * american_capacity + european_count * european_capacity

    # return the result
    result = max_weight
    return result

print(solution())