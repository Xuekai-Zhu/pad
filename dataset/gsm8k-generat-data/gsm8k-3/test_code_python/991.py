def solution():
    """There are six unicorns in the Enchanted Forest. Everywhere a unicorn steps, four flowers spring into bloom. The six unicorns are going to walk all the way across the forest side-by-side, a journey of 9 kilometers. If each unicorn moves 3 meters forward with each step, how many flowers bloom because of this trip?"""
    # Define the number of unicorns and the distance they will travel
    NUM_UNICORNS = 6
    DISTANCE = 9000  # 9 kilometers = 9000 meters

    # Define the number of flowers that bloom with each step of a unicorn
    FLOWERS_PER_STEP = 4

    # Define the distance each unicorn moves per step
    MOVE_PER_STEP = 3

    # Calculate the number of steps each unicorn takes to travel 9 kilometers
    num_steps = int(DISTANCE / (NUM_UNICORNS * MOVE_PER_STEP))

    # Calculate the total number of flowers that bloom during the journey
    total_flowers = NUM_UNICORNS * num_steps * FLOWERS_PER_STEP

    # Display the total number of flowers that bloom
    result = total_flowers
    return result

print(solution())