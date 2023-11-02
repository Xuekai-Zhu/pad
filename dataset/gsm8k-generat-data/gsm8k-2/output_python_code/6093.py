def solution():
    """Walter goes to the zoo, where he spends a certain amount of time looking at the seals, eight times as long looking at the penguins, and 13 minutes looking at the elephants. If he spent 2 hours and 10 minutes at the zoo, how many minutes did he spent looking at the seals?"""
    total_time = 2*60 + 10
    elephant_time = 13
    penguin_time = 8 * elephant_time
    seal_time = total_time - elephant_time - penguin_time
    result = seal_time
    return result

print(solution())