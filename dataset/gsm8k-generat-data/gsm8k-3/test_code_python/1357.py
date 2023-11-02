def solution():
    """Lizzy's mother gave her 80 cents and her father gave her 40 cents for keeping to her promise. She went to her uncle's and spent 50 cents buying candy for her little cousin. Her uncle gave her another 70 cents. How many cents does she have now?"""
    # Determine the starting amount of money
    starting_amount = 80 + 40

    # Determine the amount of money remaining after buying candy
    remaining_amount = starting_amount - 50

    # Determine the total amount of money after receiving money from her uncle
    total_amount = remaining_amount + 70

    # Display the total amount of money in cents
    result = total_amount
    return result

print(solution())