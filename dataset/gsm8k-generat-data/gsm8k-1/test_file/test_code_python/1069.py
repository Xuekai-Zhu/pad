def solution():
    """Mr. Robles buys 315 bananas, which is enough to feed his three monkeys for a week. One monkey eats 10 bananas each day. The second monkey eats 4 more bananas than the first monkey and the third monkey eats the rest of the bananas for the day. How many bananas does the third monkey eat each day?"""
    total_bananas = 315
    monkeys = 3
    daily_bananas = total_bananas / (monkeys * 7)
    first_monkey = 10
    second_monkey = first_monkey + 4
    third_monkey = daily_bananas - first_monkey - second_monkey
    result = third_monkey
    return result

print(solution())