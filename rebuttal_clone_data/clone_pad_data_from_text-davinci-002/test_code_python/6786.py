def solution():
     fingernail_growth_rate = 0.1
     world_record_length = 26
     Sandy_starting_length = 2
     Sandy_ending_length = world_record_length
     number_of_months = (Sandy_ending_length - Sandy_starting_length) / fingernail_growth_rate
     Sandy_age_in_months = 12 + number_of_months
     Sandy_age_in_years = Sandy_age_in_months / 12
     result = Sandy_age_in_years
     return result

print(solution())