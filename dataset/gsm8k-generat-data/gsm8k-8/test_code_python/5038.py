def solution():
    # Define the number of peanuts in the jar
    peanuts_in_jar = 148

    # Calculate the number of peanuts Brock ate
    brock_ate = peanuts_in_jar / 4

    # Calculate the remaining number of peanuts
    remaining_peanuts = peanuts_in_jar - brock_ate - 29
    result = remaining_peanuts
    return result

print(solution())