def solution():
    initial_age = 1  # The tree is 1 year old when it's planted
    initial_height = 5  # The tree is initially 5 feet tall
    growth_rate = 3  # The tree grows 3 feet per year
    target_height = 23  # We want to know when the tree will reach a height of 23 feet

    # Calculate the age of the tree when it reaches the target height
    age = (target_height - initial_height) / growth_rate + initial_age
    result = age
    return result

print(solution())