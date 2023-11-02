def solution():
    pins_per_day = 10
    pins_deleted_per_week_per_person = 5
    num_people = 20
    total_pins = 1000
    days_in_month = 30

    # Calculate the total number of pins deleted per week for the entire group
    total_deleted_per_week = pins_deleted_per_week_per_person * num_people

    # Calculate the total number of days Reese has been a member
    num_days = days_in_month

    # Calculate the total number of pins contributed by the group during Reese's membership
    total_pins_contributed = num_days * pins_per_day * num_people

    # Calculate the total number of pins deleted during Reese's membership
    total_pins_deleted = (num_days / 7) * total_deleted_per_week

    # Calculate the total number of pins after Reese's membership
    total_pins_after_membership = total_pins + total_pins_contributed - total_pins_deleted
    result = total_pins_after_membership
    return result

print(solution())