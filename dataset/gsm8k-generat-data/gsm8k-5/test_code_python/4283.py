def solution():
    eddie_daily_pies = 3  # Eddie can bake 3 pies a day
    sister_daily_pies = 6  # Eddie's sister can bake 6 pies a day
    mother_daily_pies = 8  # Eddie's mother can bake 8 pies a day
    days = 7  # They want to know how many pies they'll bake in 7 days

    # Calculate the total number of pies each person can bake in 7 days
    eddie_total_pies = eddie_daily_pies * days
    sister_total_pies = sister_daily_pies * days
    mother_total_pies = mother_daily_pies * days

    # Calculate the total number of pies all three of them can bake in 7 days
    total_pies = eddie_total_pies + sister_total_pies + mother_total_pies
    result = total_pies
    return result

print(solution())