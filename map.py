class Map:
  _instance = None
  _initialized = False
  
  def __new__(cls):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self):
    if not Map._initialized:
      self._map = []
      self._revealed = []
      self.load_map(1)
      Map._initialized = True
      
  def load_map(self, map_num):
    self._map.clear()
    self._revealed.clear()
    file = open(f'map{map_num}.txt', 'r')
    for line in file.readlines():
      map_row = []
      rev_row = []
      for letter in line:
        map_row.append(letter)
        rev_row.append(False)
      self._map.append(map_row)
      self._revealed.append(rev_row)
  
  def __getitem__(self, row):
    return self._map[row]

  def __len__(self):
    return len(self._map)

  def show_map(self, loc):
    map_str = ""
    
    for r in range(5):
      for c in range(5):
        if r == loc[0] and c == loc[1]:
          map_str += '*'
        elif self._revealed[r][c]:
          map_str += self._map[r][c]
        else:
             map_str += 'x'
      map_str += '\n'
    return map_str
    
  def reveal(self, loc):
    self._revealed[loc[0]][loc[1]] = True

  def remove_at_loc(self, loc):
    self._map[loc[0]][loc[1]] = 'n'