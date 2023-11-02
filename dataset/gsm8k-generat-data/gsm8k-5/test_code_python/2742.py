def solution():
    total_candies = 300  # Henley bought 300 candies
    sour_candies = int(total_candies * 0.4)  # 40% of the candies are sour
    good_candies = total_candies - sour_candies  # The remaining candies are good

    # Each person gets an equal share of the good candies
    share_per_person = good_candies // 3

    return share_per_person

print(solution())