def solution():
    """At the park, Dimitri saw families riding bicycles and tricycles. Bicycles have two wheels and tricycles have three wheels. 6 adults were riding bicycles and 15 children were riding tricycles. How many wheels did Dimitri see at the park?"""
    # Define the number of adults riding bicycles and children riding tricycles
    adult_bicycles = 6
    child_tricycles = 15

    # Calculate the number of wheels from adults riding bicycles
    adult_wheels = adult_bicycles * 2

    # Calculate the number of wheels from children riding tricycles
    child_wheels = child_tricycles * 3

    # Calculate the total number of wheels
    total_wheels = adult_wheels + child_wheels

    # return the result
    result = total_wheels
    return result

print(solution())