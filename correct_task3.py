def average_valid_measurements(values):

    if not values:
        return 0
    
    total = 0
    valid_count = 0
    
    for v in values:
        if v is not None:
            try:
                numeric_value = float(v)
                total += numeric_value
                valid_count += 1
            except (ValueError, TypeError):

                continue
    
    if valid_count == 0:
        return 0
    
    return total / valid_count