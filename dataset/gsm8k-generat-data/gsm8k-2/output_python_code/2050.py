def solution():
    """Mary wants to bake 10 apple pies for a charity event. Each pie needs 8 apples and she already harvested 50 apples from the trees in her garden. How many more apples does she need to buy to make all 10 pies?"""
    apples_per_pie = 8
    total_pies = 10
    harvested_apples = 50
    total_apples_needed = apples_per_pie * total_pies
    remaining_apples_needed = total_apples_needed - harvested_apples
    result = remaining_apples_needed
    return result

print(solution())