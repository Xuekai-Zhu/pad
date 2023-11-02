def solution():
    """Apples used to cost $1.6 per pound.  The price got raised 25%.  How much does it cost to buy 2 pounds of apples for each person in a 4 member family?"""
    # Define the original cost per pound and the percentage increase
    original_cost = 1.6
    percent_increase = 25

    # Calculate the new cost per pound
    new_cost = original_cost * (1 + percent_increase/100)

    # Calculate the total cost for 2 pounds of apples per person
    cost_per_person = 2 * new_cost

    # Calculate the total cost for a 4-member family
    total_cost = cost_per_person * 4

    # Display the total cost
    result = total_cost
    return result

print(solution())