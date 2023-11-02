def solution():
    asparagus_per_day = 0.25  # James eats a quarter pound of asparagus per day
    broccoli_per_day = 0.25  # James eats a quarter pound of broccoli per day
    kale_per_week = 3  # James adds 3 pounds of kale per week
    weeks = 2  # James doubles his asparagus and broccoli intake after 2 weeks

    # Calculate the total asparagus and broccoli intake for the first 2 weeks
    total_ab_intake = (asparagus_per_day + broccoli_per_day) * 7 * 2

    # Calculate the new asparagus and broccoli intake after 2 weeks
    new_ab_intake = total_ab_intake * 2

    # Calculate the total vegetable intake per week
    total_veggie_intake = new_ab_intake + (kale_per_week * 1.0)

    result = total_veggie_intake
    return result

print(solution())