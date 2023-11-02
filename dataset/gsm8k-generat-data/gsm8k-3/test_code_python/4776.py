def solution():
    """Next year, there will be twice as many people going to the fair as are going this year, and the number of people who went to the fair last year was 200 less than those going next year. If the number of people going to the fair this year is 600, calculate the number of people at the fair in the three years."""
    # Define the number of people going to the fair this year
    current_year = 600

    # Calculate the number of people going to the fair next year and last year
    next_year = current_year * 2
    last_year = next_year - 200

    # Calculate the total number of people at the fair in the three years
    total_people = current_year + next_year + last_year

    # Display the total number of people
    result = total_people
    return result

print(solution())