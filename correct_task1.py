# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
def calculate_average_order_value(orders):

    if not orders:
        return 0
    
    total = 0
    valid_count = 0
    
    for order in orders:
        
        if not isinstance(order, dict):
            continue
        
        if order.get("status") != "cancelled":
            amount = order.get("amount", 0)
            
            if isinstance(amount, (int, float)) and amount >= 0:
                total += amount
                valid_count += 1
  
    if valid_count == 0:
        return 0
    
    return total / valid_count
