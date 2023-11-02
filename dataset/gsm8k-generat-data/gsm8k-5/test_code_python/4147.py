def solution():
    initial_stamps = 3000 # Tom has 3,000 stamps in his collection
    mike_gift = 17 # Mike gave Tom 17 stamps
    harry_gift = 10 + 2*mike_gift # Harry's gift is 10 more stamps than twice Mike's gift

    # Calculate the total number of stamps Tom now has
    total_stamps = initial_stamps + mike_gift + harry_gift
    result = total_stamps
    return result

print(solution())