def solution():
    """John is working as an IT specialist. He repairs broken computers. One day he had to fix 20 computers. 20% of them were unfixable, and 40% of them needed to wait a few days for spare parts to come. The rest John was able to fix right away. How many computers John was able to fix right away?"""
    total_computers = 20
    unfixable = total_computers * 0.2
    waiting_for_parts = total_computers * 0.4
    fix_right_away = total_computers - unfixable - waiting_for_parts
    result = fix_right_away
    return result

print(solution())