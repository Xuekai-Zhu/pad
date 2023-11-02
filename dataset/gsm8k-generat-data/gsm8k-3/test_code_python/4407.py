def solution():
    """Reese joined a Pinterest group where members contributed an average of 10 pins per day. The group owner deleted older pins at the rate of 5 pins per week per person. If the group has 20 people and the total number of pins is 1000, how many pins would be there after Reese had been a member for a month?"""
    # Calculate the number of pins added by the group per day
    pins_added = 20 * 10

    # Calculate the average number of pins deleted by one person per day
    pins_deleted_per_person_per_day = 5 / 7

    # Calculate the total number of pins deleted per day
    total_pins_deleted_per_day = pins_deleted_per_person_per_day * 20

    # Calculate the net number of pins added per day
    net_pins_added_per_day = pins_added - total_pins_deleted_per_day

    # Calculate the number of days that Reese has been a member
    days_as_member = 30

    # Calculate the total number of pins added by the group since Reese joined
    total_pins_added = net_pins_added_per_day * days_as_member

    # Calculate the current total number of pins in the group
    current_total_pins = 1000 - (pins_deleted_per_person_per_day * 20 * 30)

    # Calculate the total number of pins after Reese has been a member for a month
    total_pins = total_pins_added + current_total_pins

    # Display the total number of pins
    result = total_pins
    return result

print(solution())