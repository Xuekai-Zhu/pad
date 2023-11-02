def solution():
    # Define ticket prices
    student_price = 6
    adult_price = 8

    # Define number of tickets sold
    num_students = 20
    num_adults = 12

    # Calculate total amount sold
    total_sold = (num_students * student_price) + (num_adults * adult_price)
    result = total_sold
    return result

print(solution())