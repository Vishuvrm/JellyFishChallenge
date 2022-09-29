from base_functionalities import *

class GetFinalPosition(JellyFishOps, GetDirectionRules):
  """Returns the final position of the jelly fish in the tank"""
  def __init__(self):
    self.blocked_grids = set()

  @property
  def direction_rule(self):
    return {
              "ER": 'S',
              "SR": 'W',
              "WR": 'N',
              "NR": 'E',
              "EL": 'N',
              "NL": 'W',
              "WL": 'S',
              "SL": 'E'
            }
  
  def operation(self, tank_coord, jelly_fish_data):
      X_lim, Y_lim = int(tank_coord[0]), int(tank_coord[1])
      (X, Y, dir), rule = jelly_fish_data.split(" ")
      X = int(X)
      Y = int(Y)
      msg = ""
      for r in rule:
        if str(X)+str(Y)+dir+r in self.blocked_grids:
          return str(X)+str(Y)+dir
        if r != 'F':
          dir = self.direction_rule[dir + r]
        elif r == 'F':
          if dir == 'N':
            if Y+1 > Y_lim:
              msg = "LOST"
              self.blocked_grids.add(str(X)+str(Y)+dir+r)
              break
            Y += 1
          elif dir == 'S':
            if Y-1 < 0:
              msg = "LOST"
              self.blocked_grids.add(str(X)+str(Y)+dir+r)
              break
            Y -= 1
          elif dir == 'E':
            if X+1 > X_lim:
              msg = "LOST"
              self.blocked_grids.add(str(X)+str(Y)+dir+r)
              break
            X += 1
          elif dir == 'W':
            if X-1 < 0:
              msg = "LOST"
              self.blocked_grids.add(str(X)+str(Y)+dir+r)
              break
            X -= 1
  
      return str(X)+str(Y)+dir+msg

class GetMultipleJellyFishPos(JellyFishOps):
  """Get final positions for multiple jelly fishes inside the tank"""
  def operation(self, inputs):
    final_pos = GetFinalPosition()
    tank_coord, *jelly_fish_data = inputs.splitlines()

    for j_data in jelly_fish_data:
      print(final_pos.operation(tank_coord, j_data))


__all__ = ["GetMultipleJellyFishPos"]