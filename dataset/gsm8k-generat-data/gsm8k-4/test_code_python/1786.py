def solution():
    """4/5 of the Easter eggs are blue and 1/5 are purple. Half the purple eggs have five pieces of candy each, 
    and 1/4 of the blue eggs do. The rest of the eggs only have one piece of candy. 
    If Jerry opens one egg at random, what is the percentage chance he'll get 5 pieces of candy?"""
    
    # Define the probabilities of getting each type of egg
    blue_prob = 4/5
    purple_prob = 1/5
    
    # Define the probability of getting 5 pieces of candy for each type of egg
    blue_5prob = 1/4
    purple_5prob = 1/2
    
    # Calculate the probability of getting a blue egg with 5 pieces of candy
    blue_5 = blue_prob * blue_5prob
    
    # Calculate the probability of getting a purple egg with 5 pieces of candy
    purple_5 = purple_prob * purple_5prob
    
    # Calculate the probability of getting any egg with 5 pieces of candy
    total_5 = blue_5 + purple_5
    
    # Calculate the percentage chance of getting an egg with 5 pieces of candy
    percent_chance = total_5 * 100
    
    # Return the result
    result = percent_chance
    return result

print(solution())