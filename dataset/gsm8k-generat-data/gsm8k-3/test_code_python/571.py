def solution():
    """Anthony and his friend Leonel read about the importance of keeping pets at home and decided to start adopting cats and dogs from the local rescue center. Anthony has 12 cats and dogs, 2/3 of which are cats. Leonel has half times as many cats as Anthony and seven more dogs than Anthony. How many animals in total do the two have?"""
    
    # Calculate the number of cats Anthony has
    cats_anthony = 2/3 * 12
    
    # Calculate the number of dogs Anthony has
    dogs_anthony = 12 - cats_anthony
    
    # Calculate the number of cats Leonel has
    cats_leonel = 1/2 * cats_anthony
    
    # Calculate the number of dogs Leonel has
    dogs_leonel = dogs_anthony + 7
    
    # Calculate the total number of animals
    total_animals = cats_anthony + dogs_anthony + cats_leonel + dogs_leonel
    
    # Display the total number of animals
    result = total_animals
    return result

print(solution())