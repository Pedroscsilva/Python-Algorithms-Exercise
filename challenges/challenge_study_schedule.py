def study_schedule(permanence_period, target_time=None):
    if target_time is None:
        return None

    users_amount = 0
    for period in permanence_period:
        if not isinstance(period[0], int) or not isinstance(period[1], int):
            return None
        if period[0] <= target_time <= period[1]:
            users_amount += 1

    return users_amount
