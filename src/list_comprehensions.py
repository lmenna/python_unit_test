
def create_cubes_comprehension(num_cubes):
  cubes = [i ** 3 for i in range(num_cubes)]
  return(cubes)

def create_cubes_loop(num_cubes):
  cubes = []
  for i in range(num_cubes):
    cubes.append(i**3)
  return(cubes)

def create_odd_cubes(max_num):
  return([i ** 3 for i in range(max_num) if i % 2 != 0])

