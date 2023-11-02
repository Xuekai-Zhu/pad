def solution():
    greta_food = 20/10  # Greta eats 1/10th of the amount Penelope eats
    milton_food = greta_food/100  # Milton eats 1/100th of the amount Greta eats
    elmer_food = milton_food * 4000  # Elmer eats 4000 times more than Milton
    
    difference = elmer_food - 20  # Calculate the difference between Elmer's and Penelope's food
    
    result = difference
    return result

print(solution())