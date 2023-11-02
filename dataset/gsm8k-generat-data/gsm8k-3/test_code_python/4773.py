def solution():
    """The hospital has 11 doctors and 18 nurses. If 5 doctors and 2 nurses quit, how many doctors and nurses are left?"""
    # Define the original number of doctors and nurses
    original_doctors = 11
    original_nurses = 18

    # Define the number of doctors and nurses who quit
    quitting_doctors = 5
    quitting_nurses = 2

    # Calculate the remaining number of doctors and nurses
    remaining_doctors = original_doctors - quitting_doctors
    remaining_nurses = original_nurses - quitting_nurses

    # Display the remaining number of doctors and nurses
    result = (remaining_doctors, remaining_nurses)
    return result

print(solution())