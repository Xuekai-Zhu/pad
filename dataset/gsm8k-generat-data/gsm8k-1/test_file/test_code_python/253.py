def solution():
    """Each solid 10-foot section of a redwood tree weighs 400 pounds. Termites ate 30% of this redwood's wood. If the redwood is 200 feet tall, how much does it weigh?"""
    height = 200
    weight_per_section = 400
    num_sections = height / 10
    total_weight = num_sections * weight_per_section
    total_weight_after_loss = total_weight * (1 - 0.3)
    result = total_weight_after_loss
    return result

print(solution())