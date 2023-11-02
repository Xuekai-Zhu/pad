def solution():
    """Archie received his medical receipt from his doctor, and he needs to take antibiotics three times a day. If antibiotic costs $3 each and he needs to take it for a week, how much money does he need to buy the antibiotics?"""
    # Define the cost of each antibiotic and the number of doses per day
    ANTIBIOTIC_COST = 3
    DOSES_PER_DAY = 3

    # Define the number of days that Archie needs to take the antibiotics
    DAYS = 7

    # Calculate the total number of doses that Archie needs to take
    total_doses = DAYS * DOSES_PER_DAY

    # Calculate the total cost of the antibiotics
    total_cost = total_doses * ANTIBIOTIC_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())