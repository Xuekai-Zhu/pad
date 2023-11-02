def solution():
    # Calculate the cost of transporting 80 bags of cement
    cost_80bags = 6000

    # Calculate the weight of one bag of cement
    weight_1bag = 50

    # Calculate the weight of one new bag of cement
    weight_newbag = (3/5) * weight_1bag

    # Calculate the total number of new bags of cement
    total_newbags = 3 * 80

    # Calculate the cost of transporting the new bags of cement
    cost_newbags = (total_newbags * weight_newbag / weight_1bag) * cost_80bags

    result = cost_newbags
    return result

print(solution())