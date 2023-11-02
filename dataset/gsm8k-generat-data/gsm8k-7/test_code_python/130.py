def solution():
    starting_count = 180
    friends_count = 40
    brothers_count = 30

    # Calculate the total number of seashells given away
    given_away = friends_count + brothers_count

    # Calculate the remaining number of seashells
    remaining = starting_count - given_away

    # Calculate the number of seashells sold
    sold = remaining / 2

    # Calculate the final number of seashells left
    final_count = remaining - sold
    result = final_count
    return result

print(solution())