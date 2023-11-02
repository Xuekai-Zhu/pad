def solution():
    days_per_week = 5  # Kelly puts string cheeses in her kids lunches 5 days per week
    total_weeks = 4  # Kelly wants to know how many packages of string cheese she needs for 4 weeks
    oldest_child_amount = 2  # Kelly's oldest child wants 2 string cheeses in their lunch
    youngest_child_amount = 1  # Kelly's youngest child wants 1 string cheese in their lunch
    package_size = 30  # Each package of string cheese contains 30 string cheeses

    # Calculate the total number of string cheeses needed for both kids in 4 weeks
    total_string_cheeses = (oldest_child_amount + youngest_child_amount) * days_per_week * total_weeks

    # Calculate the total number of packages of string cheese needed
    total_packages = total_string_cheeses // package_size + (1 if total_string_cheeses % package_size > 0 else 0)
    result = total_packages
    return result

print(solution())