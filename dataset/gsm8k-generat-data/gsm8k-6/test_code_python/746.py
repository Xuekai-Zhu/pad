def solution():
    # Calculate the total ratio of the money shared
    total_ratio = 2 + 1 + 3  

    # Calculate the amount of money shared
    total_money = 50 / (1/total_ratio)  # Since Amy got 1 part of 6, total_ratio = 6

    # Calculate the amount of money Sandra got
    sandra_money = (2/total_ratio) * total_money
    result = sandra_money
    return result

print(solution())