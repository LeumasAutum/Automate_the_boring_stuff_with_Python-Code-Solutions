# Comma Code
# Say you have a list value like this:
# spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument and returns 
# a string with all the items separated by a comma and a space, with and
# inserted before the last item. For example, passing the previous spam list to 
# the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.
# Lists 103


#coma code
def comma_code(list_value):
    if len(list_value) == 0:
        return ""
    if len(list_value) == 1:
        return list_value[0]
    return ", ".join(list_value[:-1]) + " and " + list_value[-1]

spam = ['apples', 'bananas', 'tofu', 'cats']
result = comma_code(spam)
print(result)

