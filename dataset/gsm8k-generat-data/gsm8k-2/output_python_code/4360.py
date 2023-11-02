def solution():
    """The tripodasaurus has three legs. In a flock of tripodasauruses, there is a total of 20 heads and legs. How many tripodasauruses are in the flock?"""
    total_legs = 20
    legs_per_tripodasaurus = 3
    total_tripodasauruses = total_legs // legs_per_tripodasaurus
    result = total_tripodasauruses
    return result

print(solution())