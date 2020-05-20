def balance_parentheses(parentheses):
    stack = []
    if (len(parentheses)%2 != 0):
        return False
    open_parenthese = ('(','{','[')
    for i in parentheses:
        if i in open_parenthese:
            stack.append(i)
        else:
            top = stack.pop()
            if i == ')':
                if top != '(':
                    return False
            if i == '}':
                if top != '{':
                    return False
            if i == ']':
                if top != '[':
                    return False
            
    if len(stack) == 0:
        return True
    else:
        return False
    
    
    
print(balance_parentheses('[(])') )
print(balance_parentheses('[()]{}{[()()]()}'))