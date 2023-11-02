def solution():
    # Define the initial number of doctors and nurses
    initial_doctors = 11
    initial_nurses = 18

    # Subtract the number of doctors and nurses who quit
    remaining_doctors = initial_doctors - 5
    remaining_nurses = initial_nurses - 2

    # Calculate the total number of remaining doctors and nurses
    total_remaining = remaining_doctors + remaining_nurses
    result = total_remaining
    return result

print(solution())