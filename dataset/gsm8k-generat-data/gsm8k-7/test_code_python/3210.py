def solution():
    total_chargers = 24
    laptop_chargers = 5 * phone_chargers

    # Define equation
    phone_chargers + laptop_chargers = total_chargers

    # Substitute laptop_chargers with its formula
    phone_chargers + (5 * phone_chargers) = total_chargers

    # Simplify and solve for phone_chargers
    6 * phone_chargers = total_chargers
    phone_chargers = total_chargers / 6
    result = phone_chargers
    return result

print(solution())