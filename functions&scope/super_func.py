def super_func(*args, **kwargs):
    for name in kwargs.values():
      print("hello, welcome to vscode:", name)
    return sum(args)
print(super_func(1,2,3,4,5, person1="sarika", person2 = "pranav"))
