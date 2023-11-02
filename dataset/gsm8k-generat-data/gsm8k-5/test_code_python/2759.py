def solution():
    biking_time = 30  # Ryan spends 30 minutes biking to work
    bus_time = 40  # The bus takes 10 minutes longer than biking
    friend_time = biking_time * (1/3)  # Ryan's friend cuts 2/3 off his biking time, so he only spends 1/3 of the time biking

    # Calculate the total time Ryan spends commuting to work each week
    total_time = biking_time + bus_time * 3 + friend_time

    # Convert the total time to minutes
    total_minutes = total_time * 60
    result = total_minutes
    return result

print(solution())