def solution():
    thor = x
    jake = x + 10
    quincy = 200
    # since Quincy sold ten times as many as Thor, then we can calculate
    # the number of stuffed animals Thor sold as follows:
    thor = quincy / 10
    # Calculate the number of stuffed animals Jake sold
    jake = thor + 10
    # Calculate the difference in the number of stuffed animals Quincy and Jake sold
    diff = quincy - jake
    result = diff
    return result

print(solution())