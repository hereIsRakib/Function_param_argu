def say_hello(name, emoji):
    print(f'hello {name} {emoji}')


# for positional argument

say_hello('Rakib', '😊')

# keyword argumetns

say_hello(name='rakib',emoji='😊')
say_hello(emoji='😊',name='rakib') # but this a bad practice to change the positon

#we can also define the default value for the parameter so if the user doesnt put any value it does not error
def say_hello2(name='', emoji=''):
    print(f'hello {name} {emoji}')

say_hello2()
