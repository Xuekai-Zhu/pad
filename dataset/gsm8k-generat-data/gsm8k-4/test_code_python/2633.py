def solution():
    """A bird watcher records the number of birds he sees each day. One Monday he sees 70 birds. On Tuesday he sees half as many birds as he did on Monday. On Wednesday he sees 8 more birds than he did on Tuesday. How many total birds did the bird watcher see from Monday to Wednesday?"""
    # Define the number of birds seen on Monday
    birds_monday = 70

    # Calculate the number of birds seen on Tuesday
    birds_tuesday = birds_monday / 2

    # Calculate the number of birds seen on Wednesday
    birds_wednesday = birds_tuesday + 8

    # Calculate the total number of birds seen from Monday to Wednesday
    total_birds = birds_monday + birds_tuesday + birds_wednesday

    # return the result
    result = total_birds
    return result

print(solution())