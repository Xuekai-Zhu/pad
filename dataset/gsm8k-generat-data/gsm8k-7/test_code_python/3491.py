def solution():
    num_guests = 24  # total number of house guests
    tablespoons_per_cup_weak = 1
    tablespoons_per_cup_strong = 2
    num_cups_weak = 12
    num_cups_strong = 12

    # Calculate the total number of tablespoons of coffee needed for weak coffee
    total_tablespoons_weak = num_guests / 2 * tablespoons_per_cup_weak * num_cups_weak

    # Calculate the total number of tablespoons of coffee needed for strong coffee
    total_tablespoons_strong = num_guests / 2 * tablespoons_per_cup_strong * num_cups_strong

    # Calculate the total number of tablespoons of coffee needed for both weak and strong coffee
    total_tablespoons = total_tablespoons_weak + total_tablespoons_strong
    result = total_tablespoons
    return result

print(solution())