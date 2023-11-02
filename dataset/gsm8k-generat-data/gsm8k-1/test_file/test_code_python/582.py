def solution():
    """Hannah needs to drink 100 ml of water for every 200 calories she burns. She spends 2 hours doing aerobics, which burns 500 calories/hour, and 1 hour running, which burns 600 calories/hour. How many ml of water does she need to drink?"""
    aerobics_duration = 2
    aerobics_calories_burned_per_hour = 500
    running_duration = 1
    running_calories_burned_per_hour = 600
    total_calories_burned = (aerobics_duration * aerobics_calories_burned_per_hour) + (running_duration * running_calories_burned_per_hour)
    water_needed_ml = (total_calories_burned / 200) * 100
    result = water_needed_ml
    return result

Question: Samantha's last name has three fewer letters than Bobbie's last name. If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie's. Jamie's full name is Jamie Grey. How many letters are in Samantha's last name?
Solution: 
def solution():
    """Samantha's last name has three fewer letters than Bobbie's last name. If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie's. Jamie's full name is Jamie Grey. How many letters are in Samantha's last name?"""
    jamie_last_name_length = len("Grey")
    bobbie_last_name_length = jamie_last_name_length * 2 + 2
    samantha_last_name_length = bobbie_last_name_length - 3
    result = samantha_last_name_length
    return result

print(solution())