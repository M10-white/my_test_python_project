
def hello(firstname="John", lastname="Doe"):
    if not isinstance(firstname, str) or not isinstance(lastname, str):
        raise TypeError("Le prénom et le nom doivent être des chaînes")
    return f"Hello, {firstname} {lastname}!"
