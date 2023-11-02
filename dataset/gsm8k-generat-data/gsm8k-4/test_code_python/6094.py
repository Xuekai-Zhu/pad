def solution():
    """Walter goes to the zoo, where he spends a certain amount of time looking at the seals, eight times as long looking at the penguins, and 13 minutes looking at the elephants. If he spent 2 hours and 10 minutes at the zoo, how many minutes did he spent looking at the seals?"""
    # Define the time spent looking at the elephants
    elephant_time = 13
    
    # Define the total time spent at the zoo in minutes
    total_time = 130
    
    # Define the time spent looking at the penguins relative to the seals
    penguin_seal_ratio = 8
    
    # Calculate the total time spent looking at the seals and penguins
    seal_penguin_time = total_time - (elephant_time + 2 * 60)
    
    # Calculate the time spent looking at the seals
    seal_time = seal_penguin_time / (penguin_seal_ratio + 1)
    
    result = seal_time
    return result

print(solution())