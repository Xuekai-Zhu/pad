def solution():
    pins_per_day = 10
    pins_per_week_per_person = 5
    total_people = 20
    total_pins = 1000
    pins_added_per_week = total_people * pins_per_day
    pins_removed_per_week = total_people * pins_per_week_per_person
    total_pins_after_one_month = total_pins + (pins_added_per_week - pins_removed_per_week)
    result = total_pins_after_one_month
    return result

print(solution())