def solution():
    first_60_days_food = 2 * 60  # The puppy needs to eat 2 ounces of special dog food per day during the first 60 days of life
    remaining_days_food = 4 * (365 - 60)  # The puppy needs to eat 4 ounces of special dog food per day for the remaining days until it can eat regular dog food
    total_food = first_60_days_food + remaining_days_food  # Calculate the total amount of dog food the puppy needs

    ounces_per_bag = 16 * 5  # Each bag of special dog food contains 5 pounds, and there are 16 ounces in a pound
    bags_needed = total_food / ounces_per_bag  # Calculate the number of bags the family needs to buy

    result = bags_needed
    return result

print(solution())