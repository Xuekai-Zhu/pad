def solution():
    # Define the ratio of Xavier's miles to Katie's miles
    xavier_to_katie_ratio = 3

    # Define the ratio of Katie's miles to Cole's miles
    katie_to_cole_ratio = 4

    # Calculate Cole's miles
    cole_miles = xavier_to_katie_ratio * katie_to_cole_ratio * (84 / xavier_to_katie_ratio)
    result = cole_miles
    return result

print(solution())