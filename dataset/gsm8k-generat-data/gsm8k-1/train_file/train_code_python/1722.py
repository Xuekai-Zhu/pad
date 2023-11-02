def solution():
    """Emani has $30 more money than Howard. If Emani has $150, and they decide to combine and share the money equally, how much money does each get?"""
    emani_money = 150
    howard_money = emani_money - 30
    combined_money = emani_money + howard_money
    num_people = 2
    share_per_person = combined_money / num_people
    result = share_per_person
    return result

print(solution())