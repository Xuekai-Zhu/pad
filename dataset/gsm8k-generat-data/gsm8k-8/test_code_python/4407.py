def solution():
    # Calculate the number of days in a month
    days_in_month = 30

    # Calculate the total number of pins contributed by the members in a day
    pins_per_day = 10

    # Calculate the total number of pins contributed by the members in a month
    total_pins_by_members = pins_per_day * days_in_month * 20

    # Calculate the total number of pins deleted in a week by the owner
    pins_deleted_per_week = 5 * 20

    # Calculate the total number of pins deleted in a month by the owner
    pins_deleted_per_month = pins_deleted_per_week * 4

    # Calculate the final number of pins in the group after a month
    final_pins = total_pins_by_members - pins_deleted_per_month

    result = final_pins
    return result

print(solution())