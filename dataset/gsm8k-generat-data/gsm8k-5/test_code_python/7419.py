def solution():
    total_candies = 66  # Tapanga and Corey have 66 candies together
    tapanga_extra = 8  # Tapanga has 8 more candies than Corey
    
    # Set up a system of equations to solve for Corey's candies (x)
    # x + (x + tapanga_extra) = total_candies
    # 2x + tapanga_extra = total_candies
    # 2x = total_candies - tapanga_extra
    # x = (total_candies - tapanga_extra) / 2
    corey_candies = (total_candies - tapanga_extra) / 2
    result = corey_candies
    return result

print(solution())