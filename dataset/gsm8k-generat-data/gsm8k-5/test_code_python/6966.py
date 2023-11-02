def solution():
    cost_unlimited_plan = 12  # Darnell pays $12 for the unlimited plan
    texts_per_month = 60  # Darnell sends 60 texts per month
    minutes_per_month = 60  # Darnell spends 60 minutes on the phone per month
    cost_alternative_plan = (texts_per_month // 30 * 1) + (minutes_per_month // 20 * 3)  # Calculate cost on alternative plan

    # Calculate how many dollars less Darnell would pay on the alternative plan
    savings = cost_unlimited_plan - cost_alternative_plan
    result = savings
    return result

print(solution())