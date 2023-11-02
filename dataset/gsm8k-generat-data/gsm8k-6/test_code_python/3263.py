def solution():
    # Calculate the total number of candy canes
    candy_canes = 2 + 3*4  # 2 from parents, 3 each from 4 teachers
    allowance_candy = candy_canes * (1/7)  # candy canes bought with allowance
    total_candy = candy_canes + allowance_candy  # total candy canes
    cavities = total_candy // 4  # number of cavities, assumes a cavity for every 4 candy canes eaten
    result = cavities
    return result

print(solution())