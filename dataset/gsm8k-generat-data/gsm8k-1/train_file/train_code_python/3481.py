def solution():
    """Cersei bought 50 cotton candies. She gave her brother and sister 5 cotton candies each, then gave the remaining one-fourth of them to her cousin. If she ate 12 cotton candies, how many cotton candies are left?"""
    cotton_candies = 50
    candies_given = 2 * 5
    candies_remaining = cotton_candies - candies_given
    candies_given_cousin = candies_remaining / 4
    candies_remaining -= candies_given_cousin
    candies_remaining -= 12
    result = candies_remaining
    return result

print(solution())