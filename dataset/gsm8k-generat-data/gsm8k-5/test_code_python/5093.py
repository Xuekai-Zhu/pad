def solution():
    # Let x be the number of times Maurice had ridden before his visit
    # Then the total number of times Matt rode during the two weeks is 3x

    # Maurice rode 8 times with Matt, so x + 8 is the total number of times he rode during the visit
    # Matt rode 16 + x + 8 = 24 + x times during the two weeks in total

    # Since Matt rides regularly, he rides at least twice a week on average
    # Therefore, he would ride 28 times in two weeks, assuming he did not ride with Maurice
    # So we have: 24 + x + 8 = 3x + 28

    # Solving for x, we get:
    # 2x = 4 + 8
    # x = 6

    result = 6
    return result

print(solution())