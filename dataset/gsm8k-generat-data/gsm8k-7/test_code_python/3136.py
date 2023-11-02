def solution():
    small_bag_price = 4.0
    small_bag_balloons = 50

    medium_bag_price = 6.0
    medium_bag_balloons = 75

    large_bag_price = 12.0
    large_bag_balloons = 200

    total_money = 24.0

    # Calculate the number of small bags Mark can buy
    num_small_bags = int(total_money / small_bag_price)

    # Calculate the number of medium bags Mark can buy
    num_medium_bags = int(total_money / medium_bag_price)

    # Calculate the number of large bags Mark can buy
    num_large_bags = int(total_money / large_bag_price)

    # Calculate the total number of balloons that Mark can buy
    num_balloons = 0
    for i in range(num_small_bags+1):
        for j in range(num_medium_bags+1):
            for k in range(num_large_bags+1):
                if i*small_bag_balloons + j*medium_bag_balloons + k*large_bag_balloons <= total_money:
                    num_balloons = max(num_balloons, i*small_bag_balloons + j*medium_bag_balloons + k*large_bag_balloons)
    result = num_balloons
    return result

print(solution())