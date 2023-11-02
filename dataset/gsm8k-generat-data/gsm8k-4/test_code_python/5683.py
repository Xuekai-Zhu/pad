def solution():
    """Four runners ran a combined total of 195 miles last week. Katarina ran 51 miles. Tomas, Tyler, and Harriet all ran the same distance. How many miles did Harriet run?"""
    # Define the total distance run by Katarina
    katarina_distance = 51

    # Define the total number of runners
    total_runners = 4

    # Calculate the total distance run by the other three runners
    other_runners_distance = 195 - katarina_distance
    other_runners_distance /= 3

    # Calculate the distance run by Harriet
    harriet_distance = other_runners_distance

    # Return the result
    result = harriet_distance
    return result

print(solution())