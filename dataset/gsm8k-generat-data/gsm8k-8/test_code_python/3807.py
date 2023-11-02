def solution():
    #Calculate the number of muffins needed each month
    muffins_per_month = 6 * 24

    #Calculate the number of muffin batches needed in 9 months
    batches_per_9_months = muffins_per_month * 9 / 6

    #Round up the number of batches to ensure enough muffins for all students
    result = math.ceil(batches_per_9_months)
    return result

print(solution())