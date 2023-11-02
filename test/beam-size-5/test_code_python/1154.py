def solution():
    bottles_per_day = 4200
    daily_energy_coverage = 0.2
    num_people = 2300

    # Calculate the total number of bottles produced by all people in a day
    total_bottles_per_day = bottles_per_day * num_people

    # Calculate the total number of bottles produced by all juices in 2300 people
    total_bottles_for_2300 = total_bottles_per_day * num_people

    # Calculate the total number of bottles that can be produced with 100% of the daily energy demand
    total_bottles_for_100_energy = total_bottles_for_2300 * daily_energy_coverage

    # Calculate the number of bottles needed to produce to reach 100% of the daily energy requirement
    bottles_needed = total_bottles_for_100_energy - total_bottles_for_2300
    result = bottles_needed
    return result

print(solution())