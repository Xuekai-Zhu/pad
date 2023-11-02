def solution():
    """At the Bertolli Farm, they grow 2073 tomatoes, 4112 cobs of corn, and 985 onions. How many fewer onions are grown than tomatoes and corn together?"""
    # Define the number of tomatoes, corn, and onions grown
    tomatoes = 2073
    corn = 4112
    onions = 985

    # Calculate the total number of onions grown compared to tomatoes and corn together
    total_onions = tomatoes + corn - onions

    # Display the difference
    result = total_onions
    return result

print(solution())