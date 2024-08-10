import matplotlib
import matplotlib.pyplot as plt

def create_cube(white_face, green_face, blue_face, yellow_face, red_face, orange_face):
  """
  Creates a dictionary containing the colors of each face of the Rubik's cube.

  Args:
    white_face: A 3x3 list representing the colors of the white face.
    green_face: A 3x3 list representing the colors of the green face.
    blue_face: A 3x3 list representing the colors of the blue face.
    yellow_face: A 3x3 list representing the colors of the yellow face.
    red_face: A 3x3 list representing the colors of the red face.
    orange_face: A 3x3 list representing the colors of the orange face.

  Returns:
    A dictionary with keys 'w', 'g', 'b', 'y', 'r', and 'o', where each key maps to a 3x3 list representing the colors of the corresponding face.
  """
  cube = {
    'w': white_face,
    'g': green_face,
    'b': blue_face,
    'y': yellow_face,
    'r': red_face,
    'o': orange_face,
  }
  return cube

def draw_cube_face(ax, face_colors, x_offset, y_offset, face_size):
  """
  Draws a single face of the Rubik's cube on a Matplotlib axis.

  Args:
    ax: The Matplotlib axis to draw on.
    face_colors: A 3x3 list representing the colors of the face.
    x_offset: The x-offset of the face.
    y_offset: The y-offset of the face.
    face_size: The size of the face.
  """
  for i in range(3):
    for j in range(3):
      color = face_colors[i][j]
      x = x_offset + j * face_size
      y = y_offset + i * face_size
      ax.add_patch(matplotlib.patches.Rectangle(xy=(x, y), width=face_size, height=face_size, color=color))

def draw_rubik_cube(cube, figsize=(8, 8)):
  """
  Draws a Rubik's cube using Matplotlib.

  Args:
    cube: A dictionary containing the colors of each face of the Rubik's cube.
    figsize: The size of the figure to create.
  """
  fig, ax = plt.subplots(figsize=figsize)

  # Face sizes and offsets
  face_size = 0.25
  center_offset = 0.1

  # Draw the front faces
  draw_cube_face(ax, cube['w'], -center_offset, 1 - center_offset, face_size)
  draw_cube_face(ax, cube['g'], -center_offset, -center_offset, face_size)
  draw_cube_face(ax, cube['b'], 1 - center_offset, -center_offset, face_size)
  draw_cube_face(ax, cube['r'], 1 - center_offset, 1 - center_offset, face_size)

  # Draw the top face
  for i in range(3):
    x = -center_offset + i * face_size
    y = 1 + center_offset
    draw_cube_face(ax, [row[i] for row in cube['y']], x, y, face_size / 2)

  ax.set_aspect('equal')
  ax.set_xlim(-1.5, 1.5)
  ax.set_ylim(-1.5, 1.5)
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_xticks([])
  ax.set_yticks([])
  plt.title('Rubik\'s Cube')
  plt.tight_layout()
  plt.show()

# Example usage
white_face = [['w00','w01','w02'],
             ['w10','w11','w12'],
             ['w20','w21','w22']]

green_face = [['g00','g01','g02'],
             ['g10','g11','g12'],
             ['g20','g21','g22']]

blue_face  = [['b00','b01','b02'],
             ['b10','b11','b12'],
             ['b20','b21','b22']]

yellow_face = [['y00','y01','y02'],
              ['y10','y11','y12'],
              ['y20','y21','y22']]

red_face = [['r00','r01','r02'],
           ['r10','r11','r12'],
           ['r20','r21','r22']]

orange_face = [['o00','o01','o02'],
              ['o10','o11','o12'],
              ['o20','o21','o22']]
