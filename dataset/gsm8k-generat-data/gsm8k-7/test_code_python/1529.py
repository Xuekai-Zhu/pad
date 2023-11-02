def solution():
    total_population = 5000
    num_males = 2000
    num_females = total_population - num_males
    percent_glasses_wearing_females = 30

    # Calculate the number of females who wear glasses
    num_glasses_wearing_females = num_females * (percent_glasses_wearing_females / 100)

    result = num_glasses_wearing_females
    return result

print(solution())