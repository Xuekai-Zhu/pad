def solution():
    """The American swallow can lift into the air and carry a maximum of 5 pounds of weight, while the European swallow can lift and carry twice the weight as the American swallow.  If there was a flock of 90 swallows, containing twice as many American as European swallows, what is the maximum combined weight the flock can carry?"""
    # Define the maximum weight each type of swallow can carry
    AMERICAN_MAX_WEIGHT = 5
    EUROPEAN_MAX_WEIGHT = 2 * AMERICAN_MAX_WEIGHT

    # Define the number of American and European swallows in the flock
    american_count = 2/3 * 90
    european_count = 1/3 * 90

    # Calculate the maximum combined weight the flock can carry
    total_weight = (american_count * AMERICAN_MAX_WEIGHT) + (european_count * EUROPEAN_MAX_WEIGHT)

    # Display the maximum combined weight
    result = total_weight
    return result

print(solution())