def solution():
    # Define the attendance of a Metallica concert and the highest panda population estimate
    metallica_attendance = 10000
    panda_population_estimate = 3000
    # Check if the panda population is greater than the Metallica concert attendance
    if panda_population_estimate > metallica_attendance:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())