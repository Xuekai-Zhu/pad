def solution():
    """A bird watcher records the number of birds he sees each day. One Monday he sees 70 birds. On Tuesday he sees half as many birds as he did on Monday. On Wednesday he sees 8 more birds than he did on Tuesday. How many total birds did the bird watcher see from Monday to Wednesday?"""
    monday_birds = 70
    tuesday_birds = monday_birds / 2
    wednesday_birds = tuesday_birds + 8
    total_birds = monday_birds + tuesday_birds + wednesday_birds
    result = total_birds
    
    return result

print(solution())