from abc import ABC, abstractmethod


class JellyFishOps(ABC):
    """Operations which are needed to be performed on the jellyfish"""
    @abstractmethod
    def operation(self):
      pass

class GetDirectionRules(ABC):
  """Direction rules which can be unique for each operation"""
  @property
  @abstractmethod
  def direction_rule(self):
      pass

class FetchInputsFromStdIn(ABC):
  """Fetches inputs from the StdIn"""
  @abstractmethod
  def get_inputs(self, inp):
    pass

class Result(ABC):
    """Result for a main operation using some specific inner functionality"""
    @abstractmethod
    def apply(*args, operation, using, **kwargs):
        pass

__all__ = ["JellyFishOps", "GetDirectionRules", "FetchInputsFromStdIn"]