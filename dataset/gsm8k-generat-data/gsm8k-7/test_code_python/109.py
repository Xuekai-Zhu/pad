def solution():
    total_nuggets = 100
    keely_nuggets = 0
    kendall_nuggets = 0

    # Calculate how many nuggets each person ate based on Alyssa's intake
    alyssa_nuggets = total_nuggets / 5
    keely_nuggets = alyssa_nuggets * 2
    kendall_nuggets = alyssa_nuggets * 2

    result = alyssa_nuggets
    return result

print(solution())