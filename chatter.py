import pygame
import time
import pygame.mixer
import numpy as np

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chatter Display")

PALETTE = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "gray": (128, 128, 128),
    "red": (255, 0, 0),
    "dark_red": (139, 0, 0),
    "light_red": (255, 102, 102),
    "green": (0, 255, 0),
    "dark_green": (0, 100, 0),
    "light_green": (144, 238, 144),
    "blue": (0, 0, 255),
    "dark_blue": (0, 0, 139),
    "light_blue": (173, 216, 230),
    "cyan": (0, 255, 255),
    "dark_cyan": (0, 139, 139),
    "light_cyan": (224, 255, 255),
    "yellow": (255, 255, 0),
    "dark_yellow": (204, 204, 0),
    "light_yellow": (255, 255, 153),
}


for color_name, rgb in PALETTE.items():
    globals()[color_name] = rgb
def graphics(x, y, color):
    """
    Set a pixel at (x, y) to a specific color (RGB).
    Args:
    - x (int): X coordinate on the screen.
    - y (int): Y coordinate on the screen.
    - color (tuple): A tuple of RGB values (r, g, b).
    """
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        screen.set_at((x, y), color)

def display_screen():
    """
    Update the screen to reflect the current graphics drawn.
    """
    pygame.display.update()

def display_line(x1, y1, x2, y2, color):
    """
    Draw a line from (x1, y1) to (x2, y2) with the given color.
    Args:
    - x1, y1 (int): Starting point of the line.
    - x2, y2 (int): Ending point of the line.
    - color (tuple): A tuple of RGB values for the line color.
    """
    pygame.draw.line(screen, color, (x1, y1), (x2, y2))

def audio(frequency, duration):
    """
    Play a sound at a specific frequency for a given duration.
    Args:
    - frequency (int): The frequency of the sound in Hz.
    - duration (float): The duration of the sound in seconds.
    """
    sample_rate = 44100
    amplitude = 32767
    samples_count = int(sample_rate * duration)


    t = np.linspace(0, duration, samples_count, endpoint=False)
    waveform = (amplitude * np.sin(2 * np.pi * frequency * t)).astype(np.int16)

    stereo_waveform = np.column_stack((waveform, waveform))

    sound = pygame.mixer.Sound(stereo_waveform)
    sound.play()
    pygame.time.delay(int(duration * 1000))
    sound.stop()


def input():
    """
    Check for any key press and return the name of the key pressed.
    Returns:
    - (str): The name of the key pressed (e.g., 'a', 'space', etc.).
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return None
        if event.type == pygame.KEYDOWN:
            return pygame.key.name(event.key)
    return ""

def clear(color):
    screen.fill(color)

def get_mouse_position():
    """
    Get the current mouse position (X, Y).
    Returns:
    - (tuple): A tuple containing the current mouse position (X, Y).
    """
    return pygame.mouse.get_pos()

def get_mouse_state():
    """
    Get the state of the mouse (clicking and scrolling).
    Returns:
    - (dict): A dictionary with keys:
        - 'left_click': Boolean indicating if the left mouse button was clicked.
        - 'right_click': Boolean indicating if the right mouse button was clicked.
        - 'scroll_up': Boolean indicating if the scroll wheel was scrolled up.
        - 'scroll_down': Boolean indicating if the scroll wheel was scrolled down.
    """
    mouse_state = {
        'left_click': False,
        'right_click': False,
        'scroll_up': False,
        'scroll_down': False
    }

    # Check mouse button states
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # Left button pressed
        mouse_state['left_click'] = True
    if mouse_buttons[2]:  # Right button pressed
        mouse_state['right_click'] = True

    # Check for scroll wheel events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up
                mouse_state['scroll_up'] = True
            elif event.button == 5:  # Scroll down
                mouse_state['scroll_down'] = True

    return mouse_state


