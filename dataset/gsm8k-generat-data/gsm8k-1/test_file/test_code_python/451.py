def solution():
    """Bob needs to buy potting soil to fill the raised beds in his vegetable garden. He has 10 raised beds, and each bed is 2 feet wide by 8 feet long by 2 feet tall. Each bag of potting soil holds 2 cubic feet of soil and costs $12. How much will the potting soil cost him?"""
    num_beds = 10
    length = 8
    width = 2
    height = 2
    volume_per_bed = length * width * height
    total_volume = num_beds * volume_per_bed
    bags_needed = total_volume / 2
    cost_per_bag = 12
    total_cost = bags_needed * cost_per_bag
    result = total_cost
    return result

print(solution())