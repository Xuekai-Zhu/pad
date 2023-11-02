def solution():
    cards_per_student = 10  # Carl gives each student 10 index cards
    students_per_class = 30  # Each of Carl's classes has 30 students
    periods_per_day = 6  # Carl teaches 6 periods a day

    # Calculate the total number of index cards Carl needs to buy
    total_cards = cards_per_student * students_per_class * periods_per_day

    # Calculate the number of packs of index cards Carl needs to buy, rounding up to the nearest whole pack
    packs = (total_cards + 49) // 50  # Using integer division and adding 49 ensures we round up to the nearest whole pack

    # Calculate the total cost of the index cards
    cost = packs * 3  # A 50 pack of index cards costs $3

    result = cost
    return result

print(solution())