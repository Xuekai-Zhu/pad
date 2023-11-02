def solution():
    # Calculate the number of batches required to make 60 bags of jerky
    total_bags = 60
    existing_bags = 20
    bags_required = total_bags - existing_bags
    batches_required = bags_required / 10

    # Calculate the number of nights needed to make the required number of batches
    nights_required = batches_required

    result = nights_required
    return result

print(solution())