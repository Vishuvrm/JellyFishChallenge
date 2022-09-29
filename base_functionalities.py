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

class Result(ABC):
    """Result for any operation"""
    @abstractmethod
    def apply(*args, ops, **kwargs):
        pass

__all__ = ["JellyFishOps", "GetDirectionRules"]