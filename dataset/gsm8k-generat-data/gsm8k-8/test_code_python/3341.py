def solution():
    # Define the number of new cases in the first week
    week1_cases = 5000

    # Calculate the number of new cases in the second week
    week2_cases = week1_cases * 0.5

    # Calculate the number of new cases in the third week
    week3_cases = week2_cases + 2000

    # Calculate the total number of new cases over the three weeks
    total_cases = week1_cases + week2_cases + week3_cases
    result = total_cases
    return result

print(solution())