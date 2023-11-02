def solution():
    total_apples_picked = 40 + 28  # Total apples picked by Maggie and Kelsey
    average_apples_picked = 30  # The average apples picked by the three of them
    total_people = 3  # The total number of people picking apples

    # Calculate the number of apples picked by Layla
    layla_picked = (average_apples_picked * total_people) - total_apples_picked
    result = layla_picked
    return result

print(solution())