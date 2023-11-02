def solution():
    
    small_bag_price = 4
    medium_bag_price = 6
    large_bag_price = 12

    small_bag_balloons = 50
    medium_bag_balloons = 75
    large_bag_balloons = 200

    budget = 24

    max_balloons = 0

    for i in range(0, int(budget/small_bag_price)+1):
        for j in range(0, int((budget-i*small_bag_price)/medium_bag_price)+1):
            k = (budget - i*small_bag_price - j*medium_bag_price) / large_bag_price
            if k.is_integer():
                total_balloons = i*small_bag_balloons + j*medium_bag_balloons + k*large_bag_balloons
                max_balloons = max(max_balloons, total_balloons)

    result = max_balloons
    return result

print(solution())