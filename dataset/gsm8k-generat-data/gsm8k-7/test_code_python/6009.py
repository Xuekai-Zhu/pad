def solution():
    red_flowers = 12
    pink_flowers = 18
    yellow_flowers = 20
    orange_flowers = 8

    # Calculate the number of red roses Lorelei picks for her vase
    red_roses = int(0.5 * red_flowers)

    # Calculate the number of pink roses Lorelei picks for her vase
    pink_roses = int(0.5 * pink_flowers)

    # Calculate the number of yellow roses Lorelei picks for her vase
    yellow_roses = int(0.25 * yellow_flowers)

    # Calculate the number of orange roses Lorelei picks for her vase
    orange_roses = int(0.25 * orange_flowers)

    # Calculate the total number of roses in Lorelei's vase
    total_roses = red_roses + pink_roses + yellow_roses + orange_roses
    
    result = total_roses 
    return result

print(solution())