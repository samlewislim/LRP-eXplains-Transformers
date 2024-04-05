import torch
import operator
from lxt.functional import CONSERVATION_CHECK_FLAG

class conservation_check(object):

    def __init__(self) -> None:
        pass
            
    def __enter__(self):
        CONSERVATION_CHECK_FLAG[0] = True

    def __exit__(self, type, value, traceback):
        CONSERVATION_CHECK_FLAG[0] = False

SYMBOLS = {
    'true': '\033[0;32;40m \u2713 \033[0m',
    'false': '\033[0;31;40m \u2717 \033[0m',
    'unknown': '\033[0;33;40m \u2047 \033[0m',
}

WHITELIST = [
    "transpose",
    "view",
    "unsqueeze",
    "reshape",

]

BLACKLIST = [
    "sum",
    "add",
    torch.sum,
    operator.add,
    
    operator.sub,

    "mul",
    operator.mul,

    "mean",
    torch.mean,

    "matmul",
    torch.matmul,

    "softmax",
    torch.softmax,
]
