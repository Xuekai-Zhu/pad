def solution():
    """Cersei bought 50 cotton candies. She gave her brother and sister 5 cotton candies each, then gave the remaining one-fourth of them to her cousin. If she ate 12 cotton candies, how many cotton candies are left?"""
    total_cotton_candies = 50
    candies_given_to_siblings = 2 * 5
    remaining_candies = total_cotton_candies - candies_given_to_siblings
    candies_given_to_cousin = remaining_candies // 4
    remaining_candies = remaining_candies - candies_given_to_cousin - 12
    result = remaining_candies
    return result

print(solution())