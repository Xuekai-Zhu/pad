def solution():
    """Aiden is making his famous steakhouse-seasoned meatballs for a neighborhood cookout.
    He adds two tablespoons of his secret steakhouse seasoning for every pound of ground beef he uses.
    He gets sixteen meatballs from each pound of meat.
    If he wants to make 80 meatballs for the cookout, how much of his secret seasoning will he need?"""
    seasoning_per_pound = 2
    meatballs_per_pound = 16
    total_meatballs = 80
    pounds_of_meat = total_meatballs / meatballs_per_pound
    seasoning_needed = pounds_of_meat * seasoning_per_pound
    result = seasoning_needed
    return result

print(solution())