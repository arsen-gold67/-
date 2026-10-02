import colorama
import inspect

print("Атрибути та об'єкти colorama:")
print(dir(colorama))

print("\nДокументація:")
help(colorama)

print("\nЧлени модуля:")
for name, obj in inspect.getmembers(colorama):
    if not name.startswith("_"):
        print(name, "->", obj)