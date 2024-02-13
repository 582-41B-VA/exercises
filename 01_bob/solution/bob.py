def reply(address):
    address = address.rstrip()

    is_question = address.endswith("?")
    is_shout = address.isupper()

    if not address:
        return "Fine. Be that way!"
    if is_question and is_shout:
        return "Calm down, I know what I'm doing!"
    if is_question:
        return "Sure"
    if is_shout:
        return "Whoa, chill out!"

    return "Whatever."

# When a Python module is imported, __name__ is set to the module's name
# (in this case, "bob"). However, When a module is executed from the
# command line, its name is automatically set to __main__.
#
# The if statement below allows us to define statements to be executed
# only if the module is run from the command line. Testing the module
# would be difficult otherwise.
if __name__ == "__main__":
    while True:
        i = input("What to say to Bob: ")
        r = reply(i)
        print(r)
