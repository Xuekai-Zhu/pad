def solution():
    pins_per_person_per_day = 10  # On average, each person contributes 10 pins per day
    num_people = 20  # The group has 20 people
    total_pins = 1000  # The total number of pins is 1000
    num_weeks = 4  # Reese has been a member for 4 weeks or 28 days

    # Calculate the number of pins contributed by the group per day
    total_pins_per_day = pins_per_person_per_day * num_people

    # Calculate the number of pins deleted per day
    pins_deleted_per_day = 5 * num_people

    # Calculate the net change in pins per day
    net_pins_per_day = total_pins_per_day - pins_deleted_per_day

    # Calculate the number of pins after Reese has been a member for a month
    num_pins = total_pins + (net_pins_per_day * num_weeks * 7)

    result = num_pins
    return result

print(solution())