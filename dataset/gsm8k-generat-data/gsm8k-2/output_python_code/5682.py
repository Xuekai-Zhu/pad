def solution():
    """Four runners ran a combined total of 195 miles last week. Katarina ran 51 miles. Tomas, Tyler, and Harriet all ran the same distance. How many miles did Harriet run?"""
    total_miles = 195
    katarina_miles = 51
    remaining_miles = total_miles - katarina_miles
    miles_per_runner = remaining_miles / 3
    harriet_miles = miles_per_runner
    result = harriet_miles
    return result

print(solution())