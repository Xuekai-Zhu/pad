def solution():
    """Ten boys brought 15 popsicle sticks each. Twelve girls brought 12 popsicle sticks each. How many fewer popsicle sticks did the girls bring than the boys?"""
    # Define the number of boys, girls, and popsicle sticks per boy and girl
    num_boys = 10
    num_girls = 12
    sticks_per_boy = 15
    sticks_per_girl = 12

    # Calculate the total number of popsicle sticks brought by the boys and girls
    total_sticks_boys = num_boys * sticks_per_boy
    total_sticks_girls = num_girls * sticks_per_girl

    # Calculate the difference in the number of popsicle sticks brought by the girls and the boys
    difference = total_sticks_boys - total_sticks_girls

    # Display the difference in the number of popsicle sticks
    result = difference
    return result

print(solution())