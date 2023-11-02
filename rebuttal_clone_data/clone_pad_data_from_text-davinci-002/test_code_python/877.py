def solution():
    kimberly_strawberries = 8 * 3 + 15
    brother_strawberries = 3 * 3 + 15
    parents_strawberries = kimberly_strawberries - brother_strawberries - 93
    total_strawberries = kimberly_strawberries + brother_strawberries + parents_strawberries
    strawberries_per_person = total_strawberries / 3
    result = strawberries_per_person
    return result

print(solution())