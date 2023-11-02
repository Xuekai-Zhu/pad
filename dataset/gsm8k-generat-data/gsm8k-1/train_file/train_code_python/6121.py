def solution():
    """Ella has 4 bags with 20 apples in each bag and six bags with 25 apples in each bag. If Ella sells 200 apples, how many apples does Ella has left?"""
    num_bags_20 = 4
    num_bags_25 = 6
    apples_per_bag_20 = 20
    apples_per_bag_25 = 25
    total_apples = (num_bags_20 * apples_per_bag_20) + (num_bags_25 * apples_per_bag_25)
    sold_apples = 200
    remaining_apples = total_apples - sold_apples
    result = remaining_apples
    return result

print(solution())