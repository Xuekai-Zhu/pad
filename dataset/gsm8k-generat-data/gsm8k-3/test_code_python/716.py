def solution():
    """Lance has 70 cents, Margaret has three-fourths of a dollar, Guy has two quarters and a dime, and Bill has six dimes. How many cents do they have combined?"""
    # Convert Margaret's money from dollars to cents
    margaret_cents = 75 * 100 / 4

    # Calculate the total amount of money in cents
    total_cents = 70 + margaret_cents + 2*25 + 10 + 6*10

    # Display the total amount of money in cents
    result = total_cents
    return result

print(solution())