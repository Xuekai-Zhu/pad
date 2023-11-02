def solution():
    william_visits = 2 # William goes to the library 2 times per week
    jason_visits = 4 * william_visits # Jason goes to the library 4 times more than William
    weeks = 4 # Jason goes to the library for 4 weeks

    # Calculate the total number of times Jason goes to the library in 4 weeks
    total_visits = jason_visits * weeks
    result = total_visits
    return result

print(solution())