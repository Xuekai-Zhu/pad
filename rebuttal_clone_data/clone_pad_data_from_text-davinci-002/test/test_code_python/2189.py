def solution():
     ground_beef_sold_Thursday = 210
     ground_beef_sold_Friday = 2 * ground_beef_sold_Thursday
     ground_beef_sold_Saturday = 130
     ground_beef_sold_Sunday = ground_beef_sold_Saturday / 2
     ground_beef_sold_total = ground_beef_sold_Thursday + ground_beef_sold_Friday + ground_beef_sold_Saturday + ground_beef_sold_Sunday
     original_plan = 500
     ground_beef_sold_beyond_plan = ground_beef_sold_total - original_plan
     result = ground_beef_sold_beyond_plan
     return result

print(solution())