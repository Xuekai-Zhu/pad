def solution():
    num_pugs_initial = 4  # There are initially 4 pugs working together
    time_initial = 45  # They can clean the house in 45 minutes
    num_pugs_final = 15  # There will be 15 pugs working together
    time_final = (num_pugs_initial * time_initial) / num_pugs_final  # Calculate the time for 15 pugs to clean the house

    result = time_final
    return result

print(solution())