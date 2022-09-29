from abc import ABC, abstractmethod


class JellyFishOps(ABC):
    """Operations"""
    @abstractmethod
    def operation(self):
      pass

class GetDirectionRules(ABC):
  @property
  @abstractmethod
  def direction_rule(self):
      pass

class Result(ABC):
    '''Result'''
    @abstractmethod
    def apply(*args, ops, **kwargs):
        pass

__all__ = ["JellyFishOps", "GetDirectionRules"]