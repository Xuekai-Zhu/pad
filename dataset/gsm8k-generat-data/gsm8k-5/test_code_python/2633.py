def solution():
    monday_birds = 70  # The bird watcher saw 70 birds on Monday
    tuesday_birds = monday_birds / 2  # The bird watcher saw half as many birds on Tuesday
    wednesday_birds = tuesday_birds + 8  # The bird watcher saw 8 more birds than he did on Tuesday

    # Calculate the total number of birds seen from Monday to Wednesday
    total_birds = monday_birds + tuesday_birds + wednesday_birds
    result = total_birds
    return result

print(solution())