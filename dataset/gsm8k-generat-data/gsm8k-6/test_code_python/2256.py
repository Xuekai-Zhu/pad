def solution():
    # Calculate the total time Carson spends waiting in line
    total_wait_time = (30 * 4) + 60  # wait times for roller coaster and tilt-a-whirl, plus ride time for tilt-a-whirl

    # Calculate the total time Carson has left for riding the giant slide
    remaining_time = (4 * 60) - total_wait_time  # 4 hours (240 minutes) minus total wait time

    # Calculate the number of times Carson can ride the giant slide
    ride_time = 15 # ride time for giant slide
    rides_possible = remaining_time // ride_time # floor division because rides cannot be partial 
    
    result = rides_possible
    return result

print(solution())