def super_func(*args, **kwargs):
#print a greeting for every name found in kwargs
    for name in kwargs.values():
      print("hello, welcome to vscode:", name)
#calculate the sum of all args
    return sum(args)
print(super_func(1,2,3,4,5, person1="sarika", person2 = "pranav"))
