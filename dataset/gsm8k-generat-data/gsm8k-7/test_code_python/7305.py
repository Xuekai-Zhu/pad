def solution():
    current_num_cats = 20
   
    # Before 20 new dogs were born, there were x cats and 0.5x dogs
    # After 20 new dogs were born, there are x cats and 0.5x + 20 dogs
    # Now there are 20 cats and 2x dogs
    # Setting the number of cats equal, we can solve for x:
    
    x = current_num_cats / 2   # x = half the number of cats currently
    num_dogs_before = 0.5 * x + 20
    num_dogs_now = 2 * current_num_cats
    
    num_cats_before = x
    result = num_cats_before
    return result

print(solution())