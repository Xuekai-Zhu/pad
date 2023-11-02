def solution():
    population = 5000
    males = 2000
    females = population - males
    percent_wearing_glasses = 30
    glasses_wearing_females = females * (percent_wearing_glasses / 100)
    result = glasses_wearing_females
    return result

print(solution())