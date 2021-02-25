# def absolute_value(num):
#     if num >= 0:
#         return num
#     else:
#         return -num

# print(absolute_value(-2))

def greet(*names):
    #greets all peeps
    print(type(names))
    for name in names:
        print("Hello "+name)

greet("Monica", "Luke", "Steve", "John")