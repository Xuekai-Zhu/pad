def solution():
    # Calculate the total number of pins deleted per week by the group owner
    total_deleted_pins = 5 * 7 * 20  # 5 pins deleted per week per person, and there are 20 people in the group

    # Calculate the net number of pins added to the group per day
    net_pins_added_per_day = 10 - (total_deleted_pins / 30)  # 30 days in a month

    # Calculate the total number of pins added by Reese after being a member for a month
    total_pins_added_by_Reese = 30 * net_pins_added_per_day

    # Calculate the total number of pins in the group after Reese has been a member for a month
    total_pins_after_Reese = 1000 + total_pins_added_by_Reese

    result = total_pins_after_Reese
    return result

print(solution())