def solution():
    """Reese joined a Pinterest group where members contributed an average of 10 pins per day. The group owner deleted older pins at the rate of 5 pins per week per person. If the group has 20 people and the total number of pins is 1000, how many pins would be there after Reese had been a member for a month?"""
    pins_per_day = 10
    pins_deleted_per_week = 5 * 20
    total_pins = 1000
    days_in_month = 30
    pins_contributed_by_reese = pins_per_day * days_in_month
    pins_deleted_by_group_owner = pins_deleted_per_week * (days_in_month // 7)
    total_pins_after_month = total_pins + pins_contributed_by_reese - pins_deleted_by_group_owner
    result = total_pins_after_month
    return result

print(solution())