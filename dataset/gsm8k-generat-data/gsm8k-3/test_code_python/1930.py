def solution():
    """The water pressure of a sink has a steady flow of 2 cups per 10 minutes for the first 30 minutes. It still flows at 2 cups per 10 minutes for the next 30 minutes after. For the next hour, the water pressure maximizes to 4 cups per 10 minutes and stops. Shawn now has to dump half of the water away. How much water is left?"""
    # Calculate the total amount of water flow in the first 30 minutes
    flow_1 = 2 * 3 # 2 cups every 10 minutes for 30 minutes

    # Calculate the total amount of water flow in the next 30 minutes
    flow_2 = 2 * 3 # 2 cups every 10 minutes for 30 minutes

    # Calculate the total amount of water flow in the next hour at maximum pressure
    flow_3 = 4 * 6 # 4 cups every 10 minutes for 60 minutes

    # Calculate the total amount of water flow
    total_flow = flow_1 + flow_2 + flow_3

    # Calculate how much water needs to be dumped
    water_to_dump = total_flow / 2

    # Calculate how much water is left
    water_left = total_flow - water_to_dump

    # Display the amount of water left
    result = water_left
    return result

print(solution())