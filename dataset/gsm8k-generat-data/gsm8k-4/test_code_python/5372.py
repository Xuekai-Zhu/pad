def solution():
    """Annalise was sent by her mother to the store to buy 10 boxes of Kleenex Ultra Soft Facial Tissues. If each box has 20 packs of tissues and each pack contain 100 tissues sold at five cents each, calculate the total amount of money Annalise spent to buy the ten boxes."""
    # Define the number of boxes and packs of tissues
    boxes = 10
    packs_per_box = 20
    tissues_per_pack = 100

    # Calculate the total number of tissues
    total_tissues = boxes * packs_per_box * tissues_per_pack

    # Calculate the total cost
    total_cost = total_tissues * 0.05

    # return the result
    result = total_cost
    return result

print(solution())