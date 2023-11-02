def solution():
    """A soccer team has three goalies and ten defenders. The team also has twice as many midfielders as defenders, and the rest of the players are strikers. If the team has 40 players, how many strikers are in the team?"""
    
    # Define the number of goalies and defenders
    goalies = 3
    defenders = 10
    
    # Calculate the number of midfielders
    midfielders = defenders * 2
    
    # Calculate the number of strikers
    strikers = 40 - (goalies + defenders + midfielders)
    
    # Display the number of strikers
    result = strikers
    return result

print(solution())