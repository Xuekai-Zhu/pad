def solution():
    """Jaylen has 5 carrots and 2 cucumbers. Jaylen has twice as many bell peppers as Kristin. Jaylen has 3 less than half as many green beans as Kristin. If Kristin has 2 bell peppers and 20 green beans, how many vegetables does Jaylen have in total?"""
    # Define Jaylen's vegetable counts
    carrots = 5
    cucumbers = 2
    bell_peppers = 2*2 # twice as many as Kristin
    green_beans = (20/2) - 3 # half as many as Kristin, minus 3

    # Calculate the total vegetable count for Jaylen
    total_vegetables = carrots + cucumbers + bell_peppers + green_beans

    result = total_vegetables
    return result

print(solution())