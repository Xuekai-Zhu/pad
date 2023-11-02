def solution():
    total_orchards = 16  # The citrus grove has 16 orchards in total
    lemon_orchards = 8  # 8 orchards will be used for lemons
    orange_orchards = lemon_orchards / 2  # Half as many orchards as lemons will be used for oranges
    remaining_orchards = total_orchards - lemon_orchards - orange_orchards  # The remaining orchards will be used for limes and grapefruits
    grapefruit_orchards = remaining_orchards / 2  # The remaining orchards will be split evenly between limes and grapefruits
    result = grapefruit_orchards
    return result

print(solution())