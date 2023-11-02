def solution():
    """One dandelion seed floated onto Mrs. Middleton's lawn, landed on good soil, and began to grow. After one month, the dandelion plant had grown to full size and developed a flower. At the end of the second month, the flower turned to 50 fluffy, white seeds, which blew onto the lawn. Only half of these seeds landed onto good soil, germinated, and began to grow, just as the first seed had done. If each of these new seedling plants produces the same number of seeds in the same amount of time as the original plant, what is the total number of seeds that these newest plants will produce in two months' time?"""
    # Initialize the total number of seeds
    total_seeds = 0
    
    # Calculate the number of seeds produced by the original plant
    original_seeds = 50
    
    # Calculate the number of new plants that can grow from the germinated seeds
    new_plants = (original_seeds / 2)
    
    # Calculate the number of seeds produced by each new plant
    new_seeds = 50
    
    # Calculate the total number of seeds produced by all the new plants after two months
    total_seeds = new_plants * new_seeds
    
    # Return the result
    result = total_seeds
    return result

print(solution())