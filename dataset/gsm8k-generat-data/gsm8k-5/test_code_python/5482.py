def solution():
    total_glasses = (2 + 4) + (3 * 4)  # Rachel drinks 2 glasses on Sunday, 4 glasses on Monday, and 3 glasses each day for next 4 days
    total_ounces = total_glasses * 10  # 1 glass of water is equal to 10 ounces of water
    remaining_ounces = 220 - total_ounces  # Rachel wants to drink a total of 220 ounces of water in a week, and she has already consumed some

    # Calculate how many glasses Rachel needs to drink on Saturday to achieve her goal
    glasses_on_saturday = remaining_ounces / (3 * 5)  # Rachel drinks 3 glasses of water every day, and she has 5 days left in the week
    result = glasses_on_saturday
    return result

print(solution())