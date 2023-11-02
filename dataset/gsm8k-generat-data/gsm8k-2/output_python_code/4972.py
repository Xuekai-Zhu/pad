def solution():
    """James catches 3 kinds of fish. He catches 200 pounds of trout, 50% more pounds of salmon, and twice as much Tuna. How many pounds of fish did he catch?"""
    trout_pounds = 200
    salmon_pounds = trout_pounds * 1.5
    tuna_pounds = trout_pounds * 2
    total_pounds = trout_pounds + salmon_pounds + tuna_pounds
    result = total_pounds
    return result

print(solution())