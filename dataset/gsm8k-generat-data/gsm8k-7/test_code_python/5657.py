def solution():
    num_weeks_in_decade = 520 # 10 years x 52 weeks per year
    mice_per_week = 1/4 # one mouse per 4 weeks

    # Calculate the total number of mice that Gina's snake will eat
    total_mice = num_weeks_in_decade * mice_per_week

    result = total_mice
    return result

print(solution())