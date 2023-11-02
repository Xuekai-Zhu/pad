def solution():
    # Calculate the total number of animals before the birds were eaten
    total_animals = 6 + 6

    # Calculate the new number of monkeys (subtract 2 from the original number)
    new_monkeys = 6 - 2

    # Calculate the new total number of animals (subtract 2 birds and add 2 monkeys)
    new_total = new_monkeys + 4

    # Calculate the percentage of animals that are now monkeys
    percent_monkeys = (new_monkeys / new_total) * 100

    result = percent_monkeys
    return result

print(solution())