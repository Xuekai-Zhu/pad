def solution():
    """Justin bought some jerseys. He bought four long-sleeved ones that cost $15 each, and some striped ones that cost $10 each. How many striped jerseys did Justin buy if he spent a total of $80?"""
    # Define the cost of a long-sleeved jersey and a striped jersey
    long_sleeve_cost = 15
    striped_cost = 10

    # Define the number of long-sleeved jerseys bought
    long_sleeve_count = 4

    # Define the total amount spent on long-sleeved jerseys
    long_sleeve_total = long_sleeve_count * long_sleeve_cost

    # Calculate the remaining amount spent on striped jerseys
    striped_total = 80 - long_sleeve_total

    # Calculate the number of striped jerseys bought
    striped_count = striped_total / striped_cost

    # Round the result to the nearest integer
    result = round(striped_count)
    return result

print(solution())