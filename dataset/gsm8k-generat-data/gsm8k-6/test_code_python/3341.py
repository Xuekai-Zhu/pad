def solution():
    # Calculate the total number of new coronavirus cases recorded by the state in three weeks
    week1_cases = 5000
    week2_cases = week1_cases / 2
    week3_cases = week2_cases + 2000
    total_cases = week1_cases + week2_cases + week3_cases
    result = total_cases
    return result

print(solution())