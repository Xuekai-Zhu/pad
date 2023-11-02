def solution():
    # Calculate the total number of sours in Sally's bag
    cherry_sours = 32
    lemon_sours = (5/4) * (4/9) * cherry_sours  # ratio of cherry to lemon sours is 4:5, and lemon sours make up 4/9 of the total sours
    orange_sours = 0.25 * (cherry_sours + lemon_sours)  # orange sours make up 25% of the total sours
    total_sours = cherry_sours + lemon_sours + orange_sours
    result = total_sours
    return result

print(solution())