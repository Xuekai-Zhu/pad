def solution():
    """Max likes to collect model trains. He asks for one for every birthday of his, and asks for two each Christmas. Max always gets the gifts he asks for, and asks for these same gifts every year for 5 years. At the end of the 5 years, his parents give him double the number of trains he already has. How many trains does Max have now?"""
    birthdays_per_year = 1
    christmases_per_year = 2
    number_of_years = 5
    trains_per_birthday = 1
    trains_per_christmas = 2
    total_trains_received = (birthdays_per_year * trains_per_birthday * number_of_years) + (christmases_per_year * trains_per_christmas * number_of_years)
    final_number_of_trains = total_trains_received * 2
    result = final_number_of_trains
    return result

print(solution())