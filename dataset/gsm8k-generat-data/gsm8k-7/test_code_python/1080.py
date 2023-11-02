def solution():
    percent_men = 0.7
    num_women = 180

    # Calculate the percentage of men
    percent_total_men = 1 - percent_men

    # Calculate the number of men
    num_men = num_women / percent_total_men * percent_men
    result = num_men
    return result

print(solution())