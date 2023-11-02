def solution():
    # Calculate the total number of people looking for Easter eggs
    num_people = 2 + 10 + 1 + 7  # 2 kids + 10 friends + 1 host + 7 additional adults

    # Calculate the total number of Easter eggs
    eggs = 15 * 12  # 15 baskets, with 12 eggs in each basket

    # Calculate the number of eggs each person gets
    eggs_per_person = eggs // num_people  # use integer division to get a whole number
    result = eggs_per_person
    return result

print(solution())