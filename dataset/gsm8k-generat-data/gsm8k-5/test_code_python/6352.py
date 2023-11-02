def solution():
    chairs = 18  # Mary has 18 chairs
    tables = 6  # Mary has 6 tables
    stools = 4  # Mary has 4 stools
    sticks_per_chair = 6
    sticks_per_table = 9
    sticks_per_stool = 2

    # Calculate the total number of sticks of wood Mary has
    total_sticks = (chairs * sticks_per_chair) + (tables * sticks_per_table) + (stools * sticks_per_stool)

    # Calculate the total number of hours Mary can stay warm
    hours_of_warmth = total_sticks / 5
    result = hours_of_warmth
    return result

print(solution())