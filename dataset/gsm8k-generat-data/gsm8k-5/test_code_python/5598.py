def solution():
    mary_towels = 24  # Mary has 24 towels
    mary_weight = mary_towels * 2.5  # Each of Mary's towels weighs 2.5 pounds
    total_weight = 60  # The total weight of their towels is 60 pounds
    frances_towels = mary_towels / 4  # Frances has one-fourth the number of towels that Mary has
    frances_weight = (total_weight * 16) - (mary_weight * 16)  # Convert to ounces and subtract Mary's weight

    # Convert Frances's weight to pounds and round to two decimal places
    frances_weight_pounds = round((frances_weight / 16), 2)
    result = frances_weight_pounds
    return result

print(solution())