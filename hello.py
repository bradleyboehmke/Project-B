def hello(name, yell = False):
    """Greeting function"""
    greeting = 'Hello ' + name
    if yell:
        return greeting.upper()
    else:
        return greeting
