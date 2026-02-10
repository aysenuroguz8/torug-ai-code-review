# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.
def count_valid_emails(emails):

    if not emails:
        return 0
    
    count = 0
    
    for email in emails:

        if not isinstance(email, str):
            continue
 
        if not email:
            continue
        
        parts = email.split('@')
        
        if len(parts) != 2:
            continue
        
        local_part = parts[0]  # @ (kullanıcı adı)
        domain_part = parts[1]  # @ (domain)
        
        if not local_part:
            continue
        
        if not domain_part:
            continue
        
        if '.' not in domain_part:
            continue
        
        if domain_part.startswith('.') or domain_part.endswith('.'):
            continue
        
        count += 1
    
    return count