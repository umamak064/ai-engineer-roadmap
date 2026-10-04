def token_counter(text):
   
    total_char=len(text)
    token_count=total_char//4
    return token_count

print(token_counter("hello worls"))