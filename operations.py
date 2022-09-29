from base_functionalities import *

class GetFinalPosition(JellyFishOps, GetDirectionRules):
  """Returns the final position of the jelly fish in the tank"""
  def __init__(self):
    self.__blocked_grids = set()

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
      X_lim, Y_lim = tank_coord
      (X, Y, dir), rule = jelly_fish_data

      msg = ""
      for r in rule:
        if str(X)+str(Y)+dir+r in self.__blocked_grids:
          return str(X)+str(Y)+dir
        if r != 'F':
          dir = self.direction_rule[dir + r]
        elif r == 'F':
          if dir == 'N':
            if Y+1 > Y_lim:
              msg = "LOST"
              self.__blocked_grids.add(str(X)+str(Y)+dir+r)
              break
            Y += 1
          elif dir == 'S':
            if Y-1 < 0:
              msg = "LOST"
              self.__blocked_grids.add(str(X)+str(Y)+dir+r)
              break
            Y -= 1
          elif dir == 'E':
            if X+1 > X_lim:
              msg = "LOST"
              self.__blocked_grids.add(str(X)+str(Y)+dir+r)
              break
            X += 1
          elif dir == 'W':
            if X-1 < 0:
              msg = "LOST"
              self.__blocked_grids.add(str(X)+str(Y)+dir+r)
              break
            X -= 1
  
      return str(X)+str(Y)+dir+msg

class FetchInputs(FetchInputsFromStdIn):
  """Takes multiple inputs from the StdIn and returns the extracted data from the inputs"""
  def get_inputs(self, inp):
    tank_coord, *jelly_fish_data = inp.splitlines()
    X_lim, Y_lim = int(tank_coord[0]), int(tank_coord[1])

    i = 0
    for j_data in jelly_fish_data:
      (X, Y, dir), rule = j_data.split(" ")
      X = int(X)
      Y = int(Y)
      jelly_fish_data[i] = ((X, Y, dir), rule)
      i += 1

    tank_coord = X_lim, Y_lim

    return tank_coord, jelly_fish_data

class GetMultipleJellyFishPos(JellyFishOps, FetchInputs):
  """Get final positions for multiple jelly fishes inside the tank"""

  def operation(self, inputs, ops):
    final_pos = ops()
    tank_coord, jelly_fish_data = self.get_inputs(inputs)

    for j_data in jelly_fish_data:
      print(final_pos.operation(tank_coord, j_data))
