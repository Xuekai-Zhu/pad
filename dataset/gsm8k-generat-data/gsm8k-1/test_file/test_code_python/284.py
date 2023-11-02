def solution():
    """A landscaping company is delivering flagstones to a customer’s yard. Each flagstone weighs 75 pounds. If the delivery trucks can carry a total weight of 2000 pounds, how many trucks will be needed to transport 80 flagstones in one trip?"""
    weight_per_flagstone = 75
    total_weight = weight_per_flagstone * 80
    truck_capacity = 2000
    num_trucks = total_weight // truck_capacity + (1 if total_weight % truck_capacity != 0 else 0)
    result = num_trucks
    return result

print(solution())