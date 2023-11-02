def solution():
    # Calculate the total miles Tom drives in a year
    total_miles = (50 * 3) + (100 * 4 * 52)  # Tom drives 50 miles on Monday, Wednesday, and Friday, and 100 miles on the other 4 days of the week for a year

    # Calculate the total cost Tom has to pay for the miles he drives and the weekly fee
    total_cost = (total_miles * 0.1) + (100 * 52)  # Tom has to pay $0.1 per mile and a weekly fee of $100

    result = total_cost
    return result

print(solution())