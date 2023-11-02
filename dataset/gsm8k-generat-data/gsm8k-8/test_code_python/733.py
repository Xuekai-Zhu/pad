def solution():
    # Calculate the number of seashells Leo collected
    leo_collected = 59 - 11 - 24

    # Calculate the number of seashells Leo gave away
    given_away = leo_collected / 4

    # Calculate the new total number of seashells
    new_total = 59 - leo_collected + (leo_collected - given_away)

    result = new_total
    return result

print(solution())