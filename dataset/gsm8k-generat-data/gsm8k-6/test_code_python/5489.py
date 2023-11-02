def solution():
    # Calculate how many models Kirsty could buy before the price increase
    budget_before = 30 * 0.45
    models_before = budget_before / 0.45

    # Calculate how many models Kirsty can buy with the new price
    budget_after = models_before * 0.5
    models_after = budget_after / 0.5

    result = models_after
    return result

print(solution())