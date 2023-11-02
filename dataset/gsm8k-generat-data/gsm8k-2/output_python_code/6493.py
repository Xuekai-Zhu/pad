def solution():
    """Donna is trying to figure out if her truck is over a particular bridge's weight limit. The bridge can hold 20,000 pounds. Donna's empty truck weighs 12,000 pounds. She's carrying 20 crates of soda that each weigh 50 pounds, 3 dryers that each weigh 3000 pounds, and twice as much weight in fresh produce as in soda. How much does Donna's fully loaded truck weigh?"""
    bridge_limit = 20000
    empty_weight = 12000
    soda_weight = 20 * 50
    dryer_weight = 3 * 3000
    produce_weight = 2 * soda_weight
    full_weight = empty_weight + soda_weight + dryer_weight + produce_weight
    result = full_weight
    return result

print(solution())