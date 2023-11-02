def solution():
    stadium_capacity = 60000
    seats_sold = stadium_capacity * 0.75
    num_fans_stayed_home = 5000

    # Calculate the actual number of fans that attended the show
    num_fans_attended = seats_sold - num_fans_stayed_home
    result = num_fans_attended
    return result

print(solution())