class UnnecessaryError(Exception):
    pass

def i_just_throw_an_exception():
    raise UnnecessaryError("Please provide an integer number")
