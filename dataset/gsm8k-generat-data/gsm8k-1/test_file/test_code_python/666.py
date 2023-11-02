def solution():
    """Robert had 3 pounds of candy, Cindy had 5 pounds of candy, and Aaron had 4 pounds of candy after Halloween. If they decide to pool and share their candy equally with each other, how much candy would each of them have?"""
    robert_candy = 3
    cindy_candy = 5
    aaron_candy = 4
    total_candy = robert_candy + cindy_candy + aaron_candy
    candies_per_person = total_candy / 3
    result = candies_per_person
    return result

print(solution())