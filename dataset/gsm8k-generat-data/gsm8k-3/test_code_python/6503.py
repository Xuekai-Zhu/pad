def solution():
    """Carla went to the zoo and counted 12 zebras in their enclosure. She then visited the camels and learned that there were only half as many camels as there were zebras. Next, she visited the monkeys and counted 4 times the number of monkeys as camels. Finally, she saw some giraffes and counted only 2 giraffes. How many more monkeys than giraffes did Carla see?"""
    
    # Define the number of zebras and calculate the number of camels
    zebras = 12
    camels = zebras // 2
    
    # Calculate the number of monkeys and giraffes
    monkeys = camels * 4
    giraffes = 2
    
    # Calculate the difference between the number of monkeys and giraffes
    difference = monkeys - giraffes
    
    # Display the difference
    result = difference
    return result

print(solution())