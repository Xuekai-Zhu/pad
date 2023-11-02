def solution():
    """Mary is paying her monthly garbage bill for a month with exactly four weeks. The garbage company charges Mary $10 per trash bin and $5 per recycling bin every week, and Mary has 2 trash bins and 1 recycling bin. They're giving her an 18% discount on the whole bill before fines for being elderly, but also charging her a $20 fine for putting inappropriate items in a recycling bin. How much is Mary's garbage bill?"""
    # Define the cost per bin per week
    TRASH_PRICE = 10
    RECYCLING_PRICE = 5

    # Define the number of bins Mary has
    trash_bins = 2
    recycling_bins = 1

    # Calculate the total cost for trash bins for the month
    trash_cost = trash_bins * TRASH_PRICE * 4

    # Calculate the total cost for recycling bins for the month
    recycling_cost = recycling_bins * RECYCLING_PRICE * 4

    # Calculate the total cost before discounts and fines
    total_cost = trash_cost + recycling_cost

    # Calculate the discount
    discount = total_cost * 0.18

    # Add the discount to the total cost
    total_cost -= discount

    # Add the recycling fine
    total_cost += 20

    # Display the total cost
    result = total_cost
    return result

print(solution())