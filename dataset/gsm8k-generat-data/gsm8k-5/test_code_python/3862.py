def solution():
    adults_per_hour = 4  # Doctor Lindsay sees 4 adult patients every hour
    children_per_hour = 3  # Doctor Lindsay sees 3 child patients every hour
    hours_per_day = 8  # Doctor Lindsay works 8 hours per day

    # Calculate the total number of adult patients seen in a day
    total_adults = adults_per_hour * hours_per_day

    # Calculate the total number of child patients seen in a day
    total_children = children_per_hour * hours_per_day

    # Calculate the total revenue from adult patients
    adult_revenue = total_adults * 50  # $50 is the cost for an adult's office visit

    # Calculate the total revenue from child patients
    child_revenue = total_children * 25  # $25 is the cost for a child's office visit

    # Add the revenues from adult and child patients to get the total revenue
    total_revenue = adult_revenue + child_revenue
    result = total_revenue
    return result

print(solution())