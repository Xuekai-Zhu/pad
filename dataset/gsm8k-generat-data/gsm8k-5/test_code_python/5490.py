def solution():
    rabbits = 16  # Junior has 16 rabbits
    monday_toys = 6  # Junior bought 6 toys on Monday
    wednesday_toys = 2 * monday_toys  # Junior bought twice as many toys as he did on Monday on Wednesday
    friday_toys = 4 * monday_toys  # Junior bought four times as many toys as he did on Monday on Friday
    saturday_toys = wednesday_toys / 2  # Junior bought half as many toys as he did on Wednesday on Saturday
    total_toys = monday_toys + wednesday_toys + friday_toys + saturday_toys  # Calculate the total number of toys
    toys_per_rabbit = total_toys / rabbits  # Calculate the number of toys each rabbit would have
    result = toys_per_rabbit
    return result

print(solution())