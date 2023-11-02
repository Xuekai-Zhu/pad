def solution():
    richard_time = 22  # Richard takes 22 minutes to clean his room
    cory_time = richard_time + 3  # Cory takes 3 minutes longer than Richard
    blake_time = cory_time - 4  # Blake takes 4 minutes less than Cory
    rooms_cleaned = 2  # They clean their rooms twice a week

    # Calculate the total time they spend cleaning their rooms in a week
    total_time = (richard_time + cory_time + blake_time) * rooms_cleaned

    result = total_time
    return result

print(solution())