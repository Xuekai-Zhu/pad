def solution():
    """The hospital has 11 doctors and 18 nurses. If 5 doctors and 2 nurses quit, how many doctors and nurses are left?"""
    initial_doctors = 11
    initial_nurses = 18
    quitting_doctors = 5
    quitting_nurses = 2
    remaining_doctors = initial_doctors - quitting_doctors
    remaining_nurses = initial_nurses - quitting_nurses
    result = (remaining_doctors, remaining_nurses)
    return result

print(solution())