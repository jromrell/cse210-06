import constants
from casting.cast import Cast
from casting.food import Food
from casting.score import Score
from casting.cycle import Cycle
from casting.timer import Timer
from scripting.script import Script
from scripting.control_actors_action import ControlActorsAction
from scripting.move_actors_action import MoveActorsAction
from scripting.handle_collisions_action import HandleCollisionsAction
from scripting.timer_action import TimerAction
from scripting.draw_actors_action import DrawActorsAction
from directing.director import Director
from services.keyboard_service import KeyboardService
from services.video_service import VideoService
from shared.color import Color
from shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("coin", Food())
    cast.add_actor("cycle1", Cycle(constants.RED, -5 * constants.CELL_SIZE))
    cast.add_actor("cycle2", Cycle(constants.BLUE, 5 * constants.CELL_SIZE))
    cast.add_actor("score1", Score('Player Red', Point(0,0)))
    cast.add_actor("score2", Score('Player Blue', Point(765,0)))
    cast.add_actor("timer", Timer(Point(430,0), 1, 30))
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("update", TimerAction(cast)) 
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)   
    director.start_game(cast, script)


if __name__ == "__main__":
    main()