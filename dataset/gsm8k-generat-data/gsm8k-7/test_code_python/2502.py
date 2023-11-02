def solution():
    total_hours = 100
    boring_percentage = 0.8
    expansion_hours = 30

    # Calculate the total hours of boring gameplay
    boring_hours = total_hours * boring_percentage

    # Calculate the total hours of enjoyable gameplay
    enjoyable_hours = total_hours - boring_hours + expansion_hours
    result = enjoyable_hours
    return result

print(solution())