def solution():
    """In a week, Mortdecai collects 8 dozen  eggs every Tuesday and Thursday, and he delivers 3 dozen  eggs to the market and 5 dozen eggs to the mall. He then uses 4 dozen eggs to make a pie every Saturday. Mortdecai donates the remaining eggs to the charity by Sunday. How many  eggs does he donate to the charity?"""
    # Define the total number of dozens of eggs collected in a week
    total_dozen = 8 + 8

    # Calculate the number of dozens of eggs delivered to the market and mall
    delivered_dozen = 3 + 5

    # Calculate the number of dozens of eggs used to make a pie
    pie_dozen = 4

    # Calculate the total number of dozens of eggs used
    used_dozen = delivered_dozen + pie_dozen

    # Calculate the number of dozens of eggs donated to charity
    donated_dozen = total_dozen - used_dozen

    # Calculate the total number of eggs donated
    donated_eggs = donated_dozen * 12

    # return the result
    result = donated_eggs
    return result

print(solution())