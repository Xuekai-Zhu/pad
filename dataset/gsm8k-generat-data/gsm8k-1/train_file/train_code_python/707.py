def solution():
    """Robi Ney wants to fill a 120-liter tub. He is amused by letting the water run for 1 minute, then closing the water supply for 1 minute, and so on alternating opening and closing the water supply. But the cap at the bottom of the tub is not very airtight and lets 1 liter of water escape per minute. The flow rate of the tap is 12 liters per minute. How long does it take to fill the tub in minutes?"""
    tub_capacity = 120
    water_loss_rate = 1
    tap_flow_rate = 12
    net_flow_rate = tap_flow_rate - water_loss_rate
    time_to_fill = tub_capacity / net_flow_rate
    time_to_fill_in_minutes = time_to_fill * 2
    result = time_to_fill_in_minutes
    return result

print(solution())