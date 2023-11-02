def solution():
    """Mary wants to bake 10 apple pies for a charity event. Each pie needs 8 apples and she already harvested 50 apples from the trees in her garden. How many more apples does she need to buy to make all 10 pies?"""
    apples_per_pie = 8
    pies_to_bake = 10
    apples_already_have = 50
    total_apples_needed = apples_per_pie * pies_to_bake - apples_already_have
    result = total_apples_needed
    return result

print(solution())