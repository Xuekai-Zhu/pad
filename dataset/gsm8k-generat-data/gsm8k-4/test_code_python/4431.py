def solution():
    """Jaylen has 5 carrots and 2 cucumbers. Jaylen has twice as many bell peppers as Kristin. Jaylen has 3 less than half as many green beans as Kristin. If Kristin has 2 bell peppers and 20 green beans, how many vegetables does Jaylen have in total?"""
    # Define the number of vegetables that Jaylen starts with
    jaylen_veggies = 0

    # Add the initial number of carrots and cucumbers 
    jaylen_veggies += 5 + 2

    # Calculate the number of bell peppers that Kristin has
    kristin_bell_peppers = 2

    # Calculate the number of bell peppers that Jaylen has
    jaylen_bell_peppers = kristin_bell_peppers * 2

    # Add the number of bell peppers to Jaylen's total
    jaylen_veggies += jaylen_bell_peppers

    # Calculate the number of green beans that Kristin has
    kristin_green_beans = 20

    # Calculate the number of green beans that Jaylen has
    jaylen_green_beans = (kristin_green_beans / 2) - 3

    # Add the number of green beans to Jaylen's total
    jaylen_veggies += jaylen_green_beans

    # Return the total number of vegetables that Jaylen has
    result = jaylen_veggies
    return result

print(solution())