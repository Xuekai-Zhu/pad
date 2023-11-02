def solution():
    """Reese joined a Pinterest group where members contributed an average of 10 pins per day. The group owner deleted older pins at the rate of 5 pins per week per person. If the group has 20 people and the total number of pins is 1000, how many pins would be there after Reese had been a member for a month?"""
    pins_per_day = 10
    group_size = 20
    total_pins = 1000
    days_in_month = 30
    pins_added = pins_per_day * group_size * days_in_month
    pins_deleted = 5 * group_size * (days_in_month / 7)
    final_pins = total_pins + pins_added - pins_deleted
    result = final_pins
    return result

print(solution())