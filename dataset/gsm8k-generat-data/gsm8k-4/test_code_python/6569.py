def solution():
    """Ali and Leila reserve their places for a trip to Egypt. The price is $147 per person, but they were each given a discount of $14 since there are two of them. How much does their trip cost?"""
    # Define the cost per person and the discount amount
    cost_per_person = 147
    discount = 14

    # Calculate the total cost after the discount
    total_cost = (cost_per_person * 2) - (discount * 2)

    result = total_cost
    return result

print(solution())