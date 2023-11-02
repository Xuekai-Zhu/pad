def solution():
    """James decides he needs to start eating more vegetables. He starts by eating a quarter pound of asparagus and a quarter pound of broccoli per day. After 2 weeks, he doubles that amount and adds 3 pounds of kale per week. How many pounds of vegetables does he eat a week after adding the kale?"""
    asparagus_per_day = 0.25
    broccoli_per_day = 0.25
    days_in_two_weeks = 14
    initial_veggie_amount = (asparagus_per_day + broccoli_per_day) * days_in_two_weeks
    doubled_amount = initial_veggie_amount * 2
    kale_per_week = 3
    total_veggie_amount = doubled_amount + kale_per_week
    result = total_veggie_amount
    return result

print(solution())