def solution():
    slices_per_loaf = 15  # A loaf of bread has 15 slices
    loaves_bought = 4  # Ten friends bought 4 loaves of bread
    friends = 10  # There are 10 friends

    # Calculate the total number of slices of bread
    total_slices = slices_per_loaf * loaves_bought

    # Calculate the number of slices of bread that each friend ate
    slices_per_friend = total_slices / friends
    result = slices_per_friend
    return result

print(solution())