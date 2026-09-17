class Here:
    def __init__(self, name,age):
        self.name = name
        self.age = age
hero1 = Here("Cat", 3)
hero2 = Here("dog", 5)
hero3 = Here("hamster", 1)

print(hero1.name, hero1.age)
print(hero2.name, hero2.age)
print(hero3.name, hero3.age)