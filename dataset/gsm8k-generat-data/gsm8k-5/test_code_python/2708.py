def solution():
    saved = 10  # Ofelia saved $10 in January
    target_month = "May"  # Ofelia wants to know how much she will save in May

    # Loop through each month and double the amount saved from the previous month
    for month in ["Feb", "Mar", "Apr", "May"]:
        saved *= 2
        if month == target_month:
            result = saved
            break  # Once we reach the target month, we can break out of the loop

    return result

print(solution())