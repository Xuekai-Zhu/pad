def solution():
    
    # Define the ages of Akbar, Alessandro, and Helene
    akbar_age = 3
    alessandro_age = 4
    helene_age = 2 * akbar_age

    # Calculate the total age of the children
    total_age = 20

    # Calculate the age of Wilfred
    wilfred_age = total_age - (akbar_age + alessandro_age + helene_age)

    # Display the age of Wilfred
    result = wilfred_age
    return result

print(solution())