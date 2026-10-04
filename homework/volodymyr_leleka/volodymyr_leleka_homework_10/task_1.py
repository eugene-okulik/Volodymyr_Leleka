def finish_me(func):


    def wrapper():
        func()
        print("finished")
    return wrapper
@finish_me
def simple():
    print('Hello world!')
simple()
