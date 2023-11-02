def solution():
    """Hilary is collecting her toenails in a jar to gross out her sister. She can fit 100 toenails in the jar, unless they are from her two big toes, which are twice as big as the rest. She has already filled it with 20 big toenails and 40 regular toenails. How many regular toenails can she fit into the remainder of the jar?"""
    total_capacity = 100
    big_toe_capacity = 2
    big_toe_count = 2 * big_toe_capacity
    regular_count = 40
    filled_capacity = big_toe_count + regular_count
    remaining_capacity = total_capacity - filled_capacity
    remaining_regular_capacity = remaining_capacity / (1 + big_toe_capacity)
    result = remaining_regular_capacity
    return result

print(solution())