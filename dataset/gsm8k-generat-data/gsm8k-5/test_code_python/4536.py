def solution():
    cartoons_time = 120  # John watches cartoons for 2 hours
    chore_ratio = 8 / 10  # For every 10 minutes of cartoons, John has to do 8 minutes of chores
    chores_time = cartoons_time * chore_ratio  # Calculate the total time John has to spend on chores

    result = chores_time
    return result

print(solution())