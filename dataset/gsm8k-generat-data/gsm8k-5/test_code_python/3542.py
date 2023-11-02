def solution():
    # Calculate the cost for the first book
    days_first_book = 20  # Celine returned the first book after 20 days
    cost_first_book = days_first_book * 0.5  # The cost is $0.50 per day
    # Calculate the cost for the second and third book
    days_second_third_books = 31  # May has 31 days
    cost_second_third_books = days_second_third_books * 0.5 * 2  # Two books stayed at her house
    # Calculate the total cost
    total_cost = cost_first_book + cost_second_third_books
    result = total_cost
    return result

print(solution())