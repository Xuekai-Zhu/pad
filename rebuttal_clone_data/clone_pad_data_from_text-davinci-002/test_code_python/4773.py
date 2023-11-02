def solution():
    doctors = 11
    nurses = 18
    doctors_quit = 5
    nurses_quit = 2
    doctors_left = doctors - doctors_quit
    nurses_left = nurses - nurses_quit
    result = f"There are {doctors_left} doctors and {nurses_left} nurses left."
    return result

print(solution())