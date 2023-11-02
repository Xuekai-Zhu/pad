def solution():
    cups_of_weak_coffee = 12  # Taylor makes 12 cups of weak coffee
    cups_of_strong_coffee = 12  # Taylor makes 12 cups of strong coffee
    tablespoons_per_cup_weak = 1  # Taylor uses 1 tablespoon of coffee per cup of water to make weak coffee
    tablespoons_per_cup_strong = tablespoons_per_cup_weak * 2  # Taylor doubles the amount to make strong coffee

    # Calculate the total tablespoons of coffee needed for weak and strong coffee
    total_tablespoons_weak = cups_of_weak_coffee * tablespoons_per_cup_weak
    total_tablespoons_strong = cups_of_strong_coffee * tablespoons_per_cup_strong

    # Calculate the total tablespoons of coffee needed for both weak and strong coffee
    total_tablespoons = total_tablespoons_weak + total_tablespoons_strong
    result = total_tablespoons
    return result

print(solution())