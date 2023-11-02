def solution():
    """Solomon bought 20 marbles from his friend Johanna and added them to a store that had 50. 
    If his father also gave him 2/5 times as many marbles as he bought from Johanna, 
    and each marble weighs 2kgs, calculate the total weight of marbles Solomon has in the store."""
    marbles_from_johanna = 20
    marbles_in_store = 50
    marbles_from_father = (2/5) * marbles_from_johanna
    total_marbles = marbles_from_johanna + marbles_in_store + marbles_from_father
    marble_weight = 2
    
    total_weight = total_marbles * marble_weight
    result = total_weight
    
    return result

print(solution())