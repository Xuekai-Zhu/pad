def solution():
    """Louise is an artist and needs to apply a coat of varnish to her latest paintings. Usually it takes 7 minutes for the coat of varnish to dry on one painting. However, today she is using a new varnish and it takes 12 minutes for the coat to dry. How much longer will it take for the coat of varnish on 6 paintings with the new varnish to dry as it would with the old varnish?"""
    old_varnish_dry_time = 7
    new_varnish_dry_time = 12
    num_paintings = 6
    old_varnish_total_dry_time = old_varnish_dry_time * num_paintings
    new_varnish_total_dry_time = new_varnish_dry_time * num_paintings
    additional_time = new_varnish_total_dry_time - old_varnish_total_dry_time
    result = additional_time
    return result

print(solution())