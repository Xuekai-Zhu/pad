def solution():
    num_doctors = 11
    num_nurses = 18

    num_doctors_quit = 5
    num_nurses_quit = 2

    # Calculate the remaining number of doctors and nurses
    remaining_doctors = num_doctors - num_doctors_quit
    remaining_nurses = num_nurses - num_nurses_quit

    result = (remaining_doctors, remaining_nurses)
    return result

print(solution())