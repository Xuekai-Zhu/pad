def solution():
    """4/5 of the Easter eggs are blue and 1/5 are purple. 
    Half the purple eggs have five pieces of candy each, and 1/4 of the blue eggs do. 
    The rest of the eggs only have one piece of candy. 
    If Jerry opens one egg at random, what is the percentage chance he'll get 5 pieces of candy?"""
    
    # Define the proportion of eggs that are blue and purple
    BLUE_PROPORTION = 4/5
    PURPLE_PROPORTION = 1/5
    
    # Define the proportion of purple eggs with 5 pieces of candy and blue eggs with 1/4 chance of having 5 pieces of candy
    PURPLE_5_CANDY_PROPORTION = 1/2
    BLUE_5_CANDY_PROPORTION = 1/4
    
    # Calculate the probability that Jerry will get an egg with 5 pieces of candy
    purple_5_candy_probability = PURPLE_PROPORTION * PURPLE_5_CANDY_PROPORTION
    blue_5_candy_probability = BLUE_PROPORTION * BLUE_5_CANDY_PROPORTION
    one_candy_probability = 1 - purple_5_candy_probability - blue_5_candy_probability
    
    # Convert probability to percentage
    probability_percentage = (purple_5_candy_probability + blue_5_candy_probability) * 100
    
    # Display the probability as a percentage
    result = probability_percentage
    return result

print(solution())