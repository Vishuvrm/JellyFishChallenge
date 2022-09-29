from operations import *
from base_functionalities import Result

class ResultantPos(Result):
    def apply(*args, operation, **kwargs):
       return operation.operation(*args, **kwargs)


if __name__ == "__main__":
  inputs = """53
11E RFRFRFRF
32N FRRFLLFFRRFLL
03W LLFFFLFLFL"""
  get_multi_pos = GetMultipleJellyFishPos()
  ResultantPos.apply(inputs, operation=get_multi_pos)
  # We can add more functionalities here in the similar way by importing them from operations module...
