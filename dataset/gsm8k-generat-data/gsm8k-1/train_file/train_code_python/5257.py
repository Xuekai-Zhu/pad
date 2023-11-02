def solution():
    """Jim decides he wants to practice for a marathon coming up. He starts off by running 5 miles every day for 30 days straight. He then pushes himself to run 10 miles a day for the next 30 days. Finally, as marathon day gets closer Jim runs 20 miles a day for 30 days straight. How many miles does Jim run in total during the 90 days?"""
    miles_first_month = 5 * 30
    miles_second_month = 10 * 30
    miles_third_month = 20 * 30
    total_miles = miles_first_month + miles_second_month + miles_third_month
    result = total_miles
    return result

print(solution())