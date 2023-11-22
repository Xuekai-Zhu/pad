def solution():
    
    # Define the amount of flour and milk needed in cups
    flour_cups = 3
    milk_cups = 1

    # Convert flour and milk amounts to bottles
    flour_bottles = flour_cups / 2
    milk_bottles = milk_cups / 2

    # Calculate the number of bags of flour and bottles of milk needed
    flour_bags = flour_bottles / 2
    milk_bags = milk_bottles / 2

    # Calculate the difference in bags of flour and bottles of milk
    difference = flour_bags - milk_bags

    # Display the difference in bags of flour and bottles of milk
    result = difference
    return result

print(solution())