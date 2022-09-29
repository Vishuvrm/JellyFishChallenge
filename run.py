from operations import GetMultipleJellyFishPos, GetFinalPosition
from base_functionalities import Result

class ResultantPositions(Result):
    def apply(*args, operation, using, **kwargs):
       return operation().operation(*args, ops=using, **kwargs)


if __name__ == "__main__":
  inputs = """53
11E RFRFRFRF
32N FRRFLLFFRRFLL
03W LLFFFLFLFL"""
  # To show the final result using GetMultipleJellyFishPos when each fish position is being calculated by GetFinalPosition
  ResultantPositions.apply(inputs, operation=GetMultipleJellyFishPos, using=GetFinalPosition)
  # We can add more functionalities here in the similar way by importing them from operations module...
