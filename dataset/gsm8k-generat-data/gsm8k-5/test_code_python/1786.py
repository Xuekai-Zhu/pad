def solution():
    blue_eggs = 4 / 5  # 4/5 of the Easter eggs are blue
    purple_eggs = 1 / 5  # 1/5 of the Easter eggs are purple
    purple_candy_eggs = purple_eggs / 2  # Half of the purple eggs have 5 pieces of candy
    blue_candy_eggs = blue_eggs / 4  # 1/4 of the blue eggs have 5 pieces of candy
    one_candy_eggs = 1 - (purple_candy_eggs + blue_candy_eggs)  # Remaining eggs have one piece of candy

    # Calculate the probability of getting an egg with 5 pieces of candy
    prob_5_candy = (purple_candy_eggs + blue_candy_eggs) * 0.5  # The probability of 5 pieces of candy is 0.5

    result = prob_5_candy * 100  # Convert probability to percentage
    return result

print(solution())