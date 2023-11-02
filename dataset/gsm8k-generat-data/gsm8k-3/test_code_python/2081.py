def solution():
    """Cassidy is grounded for 14 days for lying about her report card, plus 3 extra days for each grade below a B. If Cassidy got four grades below a B, how long is she grounded for?"""
    # Define the number of days Cassidy is grounded for lying
    base_days = 14

    # Define the number of grades below a B
    grades_below_b = 4

    # Calculate the additional days Cassidy is grounded for her grades
    additional_days = grades_below_b * 3

    # Calculate the total number of days Cassidy is grounded
    total_days = base_days + additional_days

    # Display the total number of days Cassidy is grounded
    result = total_days
    return result

print(solution())