def solution():
    # given
    male_percentage = 40
    female_percentage = 60
    male_striped_percentage = 25
    male_baby_percentage = 4
    male_adult_percentage = 60
    # calculate
    total_turtles = 100
    male_turtles = total_turtles * (male_percentage / 100)
    striped_male_turtles = male_turtles * (male_striped_percentage / 100)
    baby_ striped_male_turtles = striped_male_turtles * (male_baby_percentage / 100)
    adult_ striped_male_turtles = striped_male_turtles * (male_adult_percentage / 100)
    # output
    result = male_turtles + female_turtles + baby_striped_male_turtles + adult_striped_male_turtles
    return result

print(solution())