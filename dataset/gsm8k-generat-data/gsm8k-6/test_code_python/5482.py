def solution():
    # Calculate the total number of glasses of water Rachel drinks in the week
    total_glasses = 2 + 4 + 3*4 # 2 glasses on Sunday + 4 glasses on Monday + 3 glasses every day for 4 days
    total_ounces = total_glasses * 10 # 1 glass of water is 10 ounces
    glasses_on_Saturday = (220 - total_ounces) / 10  # calculate the number of glasses Rachel should drink on Saturday to reach her goal

    result = glasses_on_Saturday
    return result

print(solution())