def solution():
    """Stephanie is moving into a new apartment. She needs to figure out how many pieces of silverware she should purchase. She needs spoons, butter knives, steak knives, and forks. For herself she figures 5 of each would be sufficient. But in case she has guests, she wants to have 10 extra pieces of each type. Then she realizes that if everything is clean at the same time, that she will have too many of everything and not enough room to fit them in her kitchen silverware drawer. So she decides to purchase 4 fewer spoons, 4 fewer butter knives, 5 fewer steak knives, and 3 fewer forks. How many pieces total of all the silverware is Stephanie going to buy?"""
    num_types = 4  # number of types of silverware
    num_each = 5  # number of each type Stephanie wants for herself
    num_extra = 10  # number of each type Stephanie wants for guests
    num_fewer = [4, 4, 5, 3]  # number fewer Stephanie decides to purchase

    # calculate how much Stephanie will need to buy of each type
    total_each = []
    for i in range(num_types):
        total_each.append(num_each + num_extra - num_fewer[i])

    # calculate the total number of pieces of silverware Stephanie will buy
    total_silverware = sum(total_each) * num_types

    result = total_silverware
    return result

print(solution())