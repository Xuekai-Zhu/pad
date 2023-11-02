def solution():
    """Sarah wants to start a cupcake business and was approved for a business loan.  The loan has 0% interest if she pays the entire amount back in 5 years, which she decides to do.  If she put $10,000 down as a down payment and her monthly payments are $600.00, how much was her loan for (including the down payment)?"""
    # Define the number of months in 5 years
    MONTHS_IN_5_YEARS = 60

    # Calculate the total amount Sarah borrowed, including the down payment
    total_borrowed = 10_000 + (MONTHS_IN_5_YEARS * 600)

    # Display the total amount borrowed
    result = total_borrowed
    return result

print(solution())