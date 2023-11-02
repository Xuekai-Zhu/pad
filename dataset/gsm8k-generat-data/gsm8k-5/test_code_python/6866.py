def solution():
    # Number of mallard ducks already in the park
    ducks_in_park = 25

    # Number of geese already in the park
    geese_in_park = (2 * ducks_in_park) - 10

    # Total number of ducks in the park after the new flock arrives
    total_ducks = ducks_in_park + 4

    # Number of geese that leave the park
    geese_leaving_park = 15 - 5

    # Subtract the number of geese leaving from the current number in the park
    geese_in_park_after_leaving = geese_in_park - geese_leaving_park

    # Calculate the final difference in the number of geese and ducks
    geese_remaining = geese_in_park_after_leaving
    ducks_remaining = total_ducks - geese_remaining
    result = geese_remaining - ducks_remaining
    return result

print(solution())