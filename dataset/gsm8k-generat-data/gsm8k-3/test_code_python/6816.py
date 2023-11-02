def solution():
    """Every morning Harry takes 15 minutes to buy coffee and a bagel and twice that long to read the paper and eat before going in to work. How long does Harry's morning routine take?"""
    # Define the time it takes to buy coffee and a bagel
    coffee_bagel_time = 15

    # Define the time it takes to read the paper and eat
    paper_eating_time = coffee_bagel_time * 2

    # Calculate the total time for Harry's morning routine
    total_time = coffee_bagel_time + paper_eating_time

    # Display the total time
    result = total_time
    return result

Note: The above solution assumes that Harry has no other activities in his morning routine besides buying coffee and a bagel, and reading the paper and eating. If there are other activities, the solution will need to be modified accordingly.

print(solution())