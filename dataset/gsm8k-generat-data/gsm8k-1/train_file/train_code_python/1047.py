def solution():
    """A water tower that serves four neighborhoods around it holds 1200 barrels of water and is filled to the top each week. If one neighborhood uses 150 barrels of water in a week, the second neighborhood uses twice as many barrels of water as the first neighborhood in a week, and the third neighborhood uses one hundred more barrels of water than the second neighborhood in a week, how many barrels are left for the fourth neighborhood?"""
    total_water = 1200
    first_neighborhood = 150
    second_neighborhood = first_neighborhood * 2
    third_neighborhood = second_neighborhood + 100
    total_used = first_neighborhood + second_neighborhood + third_neighborhood
    barrels_left = total_water - total_used
    result = barrels_left
    return result

print(solution())