def solution():
    """It costs $.10 to print one page. Jenny wants to print 7 copies of her 25-page essay. She also wants to buy 7 pens that each cost $1.50. If she pays the store with 2 twenty dollar bills, how much money should she get in change?"""
    # Define the cost of printing one page
    PRINT_COST = 0.1

    # Define the number of copies and pages in the essay
    num_copies = 7
    num_pages = 25

    # Calculate the total cost of printing the essay
    essay_cost = num_copies * num_pages * PRINT_COST

    # Calculate the total cost of the pens
    pen_cost = 7 * 1.5

    # Calculate the total cost of the purchase
    total_cost = essay_cost + pen_cost

    # Calculate the amount paid
    amount_paid = 2 * 20

    # Calculate the change
    change = amount_paid - total_cost

    # Display the change
    result = change
    return result

print(solution())