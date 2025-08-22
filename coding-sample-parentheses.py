def isValid(string):
    arr = list(string)
    stack = []
    for el in arr:
        if (el == "(" or el == "[" or el == "{"):
            stack.append(el)
            print(stack)
        if ((el == ")" and stack[-1] == "(") 
            or (el == "]" and stack[-1] == "]") 
            or (el == "}" and stack[-1] == "{")):
            stack.pop()
            print(stack)
    return True

print("Should return true: " + str(isValid("({[]})")))
print("Should return false: " + str(isValid("[)(")))
