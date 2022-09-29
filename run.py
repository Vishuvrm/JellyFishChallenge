from operations import *
from base_functionalities import Result

class ResultantPos(Result):
    def apply(*args, ops, **kwargs):
       return ops.operation(*args, **kwargs)


if __name__ == "__main__":
  inputs = """53
11E RFRFRFRF
32N FRRFLLFFRRFLL
03W LLFFFLFLFL"""
  operations = GetMultipleJellyFishPos()
  ResultantPos.apply(inputs, ops=operations)
  # We can add more functionalities here in the similar way by importing from operations...
