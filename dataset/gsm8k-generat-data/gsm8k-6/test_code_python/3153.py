def solution():
    # Calculate the total number of animals outside Carolyn's window
    total_animals = 6 + 6  # 6 monkeys and 6 birds initially

    # Calculate the new number of monkeys after 2 of them eat one bird each
    new_monkeys = 6 + 2  # 2 of the monkeys each eat one bird, so there are now 2 more monkeys

    # Calculate the percentage of animals that are now monkeys
    percent_monkeys = (new_monkeys / total_animals) * 100
    result = percent_monkeys
    return result

print(solution())