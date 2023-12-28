class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f'Name: {self.name}, Age: {self.age}'

    def __format__(self, format_spec: str) -> str:
        print(format_spec)
        if format_spec == 'name':
            return self.name

        if format_spec == 'age':
            return str(self.age)
            
        if format_spec == 'both':
            return f'{self.name} {self.age}'

p = Person('Ian',57)
print(f'{p:name}')
print(f'{p:age}')
print(f'{p:both}')
