def solution():
    """At a party, there are 50 people. 30% of them are boys. How many girls are at this party?"""
    # Define the total number of people at the party and the percentage that are boys
    total_people = 50
    boys_percentage = 0.3

    # Calculate the number of boys at the party
    boys = total_people * boys_percentage

    # Calculate the number of girls at the party
    girls = total_people - boys

    # return the result
    result = girls
    return result

print(solution())