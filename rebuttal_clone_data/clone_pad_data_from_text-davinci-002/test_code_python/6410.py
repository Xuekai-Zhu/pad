def solution():
    num_lines = 5
    t_mobile_base_cost = 50
    t_mobile_additional_cost = 16
    t_mobile_total_cost = t_mobile_base_cost + (num_lines - 2) * t_mobile_additional_cost
    m_mobile_base_cost = 45
    m_mobile_additional_cost = 14
    m_mobile_total_cost = m_mobile_base_cost + (num_lines - 2) * m_mobile_additional_cost
    cost_difference = t_mobile_total_cost - m_mobile_total_cost
    result = cost_difference
    return result

print(solution())