def solution():
    initial_bottles = 4 + 4  # Martha had 4 bottles of juice in the fridge and 4 in the pantry
    bought_bottles = 5  # Martha bought 5 more bottles of juice during the week
    used_bottles = 3  # Martha and her family drank 3 bottles of juice during the week

    # Calculate the total number of bottles left
    total_bottles = initial_bottles + bought_bottles - used_bottles
    result = total_bottles
    return result

print(solution())