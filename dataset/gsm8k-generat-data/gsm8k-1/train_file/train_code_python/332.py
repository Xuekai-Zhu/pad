def solution():
    """Kantana loves chocolate. Every Saturday she goes to the candy store and buys 2 chocolates for herself and 1 for her sister. This last Saturday she picked up an additional 10 chocolates as a birthday gift for her friend Charlie. How many chocolates did Kantana end up buying for the month?"""
    chocolates_per_week = 3
    weeks_per_month = 4
    additional_chocolates = 10
    total_chocolates = (chocolates_per_week * weeks_per_month) + additional_chocolates
    result = total_chocolates
    return result

print(solution())