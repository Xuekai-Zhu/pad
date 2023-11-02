def solution():
    """Four children are playing together—Akbar, Alessandro, Helene, and Wilfred. Helene is twice as old as the average age of the group, and the total age of the children is 20. If Akbar is 3 years old and Alessandro is 4 years old, calculate the age of Wilfred."""
    total_age = 20
    akbar_age = 3
    alessandro_age = 4

    # Determine the total age of Helene and Wilfred
    helene_age = 2 * ((total_age - akbar_age - alessandro_age) / 2)
    wilfred_age = total_age - akbar_age - alessandro_age - helene_age
    result = wilfred_age
    return result

print(solution())