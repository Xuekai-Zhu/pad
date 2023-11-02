def solution():
    """Reese joined a Pinterest group where members contributed an average of 10 pins per day. The group owner deleted older pins at the rate of 5 pins per week per person. If the group has 20 people and the total number of pins is 1000, how many pins would be there after Reese had been a member for a month?"""
    # Define the number of people in the group
    num_people = 20

    # Define the initial number of pins
    initial_pins = 1000

    # Define the number of days in a month
    days_in_month = 30

    # Calculate the total number of pins added by members in a day
    pins_added_per_person = 10 / num_people

    # Calculate the total number of pins added by members in a month
    total_pins_added = pins_added_per_person * num_people * days_in_month

    # Calculate the total number of pins deleted by the group owner in a week
    pins_deleted_per_person = 5
    total_pins_deleted = pins_deleted_per_person * num_people / 7 * days_in_month

    # Calculate the final number of pins after a month
    final_pins = initial_pins + total_pins_added - total_pins_deleted
    
    result = final_pins
    return result

print(solution())