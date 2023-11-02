def solution():
    """At a party, there are 50 people. 30% of them are boys. How many girls are at this party?"""
    # Define the total number of people and the percentage of boys
    total_people = 50
    boys_percentage = 30

    # Calculate the number of boys
    boys = total_people * boys_percentage / 100

    # Calculate the number of girls
    girls = total_people - boys

    # Display the number of girls
    result = girls
    return result

print(solution())