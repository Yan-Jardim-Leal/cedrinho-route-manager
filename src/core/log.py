__verbose = False
__verbose_level = 1

debug = [
    0 = "[s]", # server
    1 = "[i]", # info
    2 = "[W]", # warn
    3 = "[*]" # error
]

def log(message, level : int = 1):

    if level == 0:
        print(debug[0], " ", message)
        return

    if __verbose and __verbose_level >= level:
        print(debug[__verbose_level], " ", message)

def setVerbose(is_verbose : bool):
    __verbose = is_verbose

def setLevel(verbose_level : int):
    __verbose_level = verbose_level