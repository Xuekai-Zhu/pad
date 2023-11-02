def solution():
    """The hospital has 11 doctors and 18 nurses. If 5 doctors and 2 nurses quit, how many doctors and nurses are left?"""
    initial_doctors = 11
    initial_nurses = 18
    doctors_quit = 5
    nurses_quit = 2
    remaining_doctors = initial_doctors - doctors_quit
    remaining_nurses = initial_nurses - nurses_quit
    result = (remaining_doctors, remaining_nurses)
    return result

print(solution())