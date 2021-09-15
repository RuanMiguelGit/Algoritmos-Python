def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    len_string = len(word)
    if word == "":
        return False
    if word[len_string::-1] == word:
        return True
    return False


print(is_palindrome_iterative("ANNA"))
