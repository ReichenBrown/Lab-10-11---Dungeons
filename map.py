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
      file = open('map.txt', 'r')
      for line in file.readlines():
        map_row = []
        rev_row = []
        for letter in line:
          map_row.append(letter)
          rev_row.append(False)
        self._map.append(map_row)
        self._revealed.append(rev_row)

      Map._initialized = True
      

  def __getitem__(self, row):
    return self._map[row]

  def __len__(self):
    return len(self._map)

  def show_map(self, loc):
    map = ''
    for row in range(len(self._map)-1):
      for col in range(len(self._map[row])-1):
        if [row, col] == loc:
          map += '*'
        elif self._revealed[row][col]:
          map += self._map[row][col]
        else:
          map += 'x'
      map += '\n'
    
    return map
    
  def reveal(self, loc):
    self._revealed[loc[0]][loc[1]] = True

  def remove_at_loc(self, loc):
    self._map[loc[0]][loc[1]] = 'n'