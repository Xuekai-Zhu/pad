def solution():
    """Charles is moving from Springfield, which has 482,653 people, to Greenville, which has 119,666 fewer people. What is the total population of Springfield and Greenville?"""
    # Define the population of Springfield
    springfield_pop = 482653

    # Calculate the population of Greenville
    greenville_pop = springfield_pop - 119666

    # Calculate the total population
    total_pop = springfield_pop + greenville_pop

    # Display the total population
    result = total_pop
    return result

print(solution())