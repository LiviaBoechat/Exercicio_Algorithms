def study_schedule(permanence_period, target_time):

    if any(
        not isinstance(period_start, int) or not isinstance(period_end, int)
        for period_start, period_end in permanence_period
    ):
        return None

    if not target_time:
        return None

    counter = 0
    for period_start, period_end in permanence_period:
        if period_start <= target_time <= period_end:
            counter += 1

    return counter
