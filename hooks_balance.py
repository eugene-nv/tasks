def is_balanced(hooks):
    opening_hooks = '([{'
    closing_hooks = ')]}'

    stack = []

    for hook in hooks:
        if hook in opening_hooks:
            stack.append(hook)
        elif hook in closing_hooks:
            if hook == ')' and '(' in stack:
                stack.remove('(')
            elif hook == ']' and '[' in stack:
                stack.remove('[')
            elif hook == '}' and '{' in stack:
                stack.remove('{')
            else:
                stack.append(hook)

        else:
            stack.append(hook)
    if stack:
        return 'Not balance'
    else:
        return 'Is balance'
