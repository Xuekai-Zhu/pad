def solution():
    """James decides he needs to start eating more vegetables. He starts by eating a quarter pound of asparagus and a quarter pound of broccoli per day.
    After 2 weeks, he doubles that amount and adds 3 pounds of kale per week. How many pounds of vegetables does he eat a week after adding the kale?"""
    asparagus_per_day = 0.25
    broccoli_per_day = 0.25
    weeks_before_change = 2
    asparagus_and_broccoli_per_day = asparagus_per_day + broccoli_per_day
    asparagus_and_broccoli_per_week = asparagus_and_broccoli_per_day * 7 * weeks_before_change
    asparagus_and_broccoli_doubled_per_week = asparagus_and_broccoli_per_day * 7 * 2
    kale_per_week = 3
    total_veggies_per_week = asparagus_and_broccoli_doubled_per_week + kale_per_week
    result = total_veggies_per_week
    return result

print(solution())