import random
import constants
from casting.actor import Actor
from shared.point import Point


class Food(Actor):
    """
    A tasty item that snakes like to eat.
    
    The responsibility of Food is to select a random position and points that it's worth.
    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        "Constructs a new Food."
        super().__init__()
        self._points = 0
        self._lock = False
        self.set_text(constants.COIN_SYMBOL)
        self.set_color(constants.COIN_COLOR)
        self.reset()
        
    def reset(self):
        """Selects a random position and points that the food is worth."""
        if self._lock:
            self._points = 0
            self.reset_velocity()
        else:
            self._points = random.randint(1, 8)
            x = random.randint(1, constants.COLUMNS - 1)
            y = random.randint(1, constants.ROWS - 1)
            position = Point(x, y)
            position = position.scale(constants.CELL_SIZE)
            self.set_position(position)

    def lock(self):
        """
        Locks the food in the same place
        """
        self._lock = True
        
    def get_points(self):
        """Gets the points the food is worth.
        
        Returns:
            points (int): The points the food is worth.
        """
        return self._points

    def set_random_velocity(self):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Point): The given velocity.
        """
        i = random.randint(0 , 3)

        if i == 0:
            self._velocity = Point(-15, 0)
        elif i == 1:
            self._velocity = Point(15, 0)
        elif i == 2:
            self._velocity = Point(0, -15)
        elif i == 3:
            self._velocity = Point(0, 15)
        else:
            self.set_velocity = Point(0, 0)