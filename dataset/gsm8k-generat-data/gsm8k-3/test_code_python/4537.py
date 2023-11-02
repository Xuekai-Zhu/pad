def solution():
    """Miranda wants to buy a pair of heels she saw online. She saved money for 3 months. Her sister heard that she was sad and gave her $50 for her to buy the heels. If she paid $260 in total for the heels, how much money did she save per month?"""
    # Define the total amount of money Miranda spent on the heels
    total_cost = 260

    # Subtract the amount of money her sister gave her
    total_cost -= 50

    # Calculate the amount of money Miranda saved per month
    savings_per_month = total_cost / 3

    # Display the amount of money Miranda saved per month
    result = savings_per_month
    return result

print(solution())