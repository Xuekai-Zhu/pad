def solution():
    oldest_age = 20  # Eldest child is currently 20 years old
    age_difference = 5  # Each sibling is born 5 years apart

    # Calculate the ages of the other two siblings
    middle_age = oldest_age - age_difference  # 20 - 5 = 15
    youngest_age = middle_age - age_difference  # 15 - 5 = 10

    # Calculate the total of the three siblings' ages in 10 years
    total_age_in_10_years = (oldest_age + 10) + (middle_age + 10) + (youngest_age + 10)  

    result = total_age_in_10_years
    return result

print(solution())