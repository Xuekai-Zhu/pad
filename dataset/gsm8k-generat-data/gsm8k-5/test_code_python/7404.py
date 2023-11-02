def solution():
    first_5_days = 5  # Tom charges $100 per day for the first 5 days
    after_5_days = 10 - first_5_days  # Tom charges $60 per day after the first 5 days
    cost = (first_5_days * 100) + (after_5_days * 60)  # Calculate the total cost of Tom's services
    result = cost
    return result

print(solution())