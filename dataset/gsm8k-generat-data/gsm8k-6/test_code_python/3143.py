def solution():
    # Calculate the total number of candies that Amy has
    chocolate_bars = 5
    M_and_Ms = 7 * chocolate_bars
    marshmallows = 6 * M_and_Ms
    total_candies = chocolate_bars + M_and_Ms + marshmallows

    # Calculate the number of baskets that Amy can fill
    baskets_filled = total_candies // 10

    result = baskets_filled
    return result

print(solution())