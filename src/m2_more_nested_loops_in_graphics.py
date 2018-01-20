"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Ryan Taylor.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------
    new_rectangle = rectangle.clone()

    for k in range(n + 1):
        # new_rectangle = rectangle.clone()

        # for j in range(k):
        #     next_rectangle = new_rectangle.clone()
        #
        #     corner_1x = new_rectangle.corner_1.x + (new_rectangle.get_width() * j)
        #     corner_2x = new_rectangle.corner_2.x + (new_rectangle.get_width() * j)
        #
        #     next_rectangle.corner_1.x = corner_1x
        #     next_rectangle.corner_2.x = corner_2x
        #
        #     next_rectangle.attach_to(window)
        #     window.render(0.05)

        corner1x = rectangle.corner_1.x - ((rectangle.get_width() / 2) * k)
        corner1y = rectangle.corner_1.y - (rectangle.get_height() * k)
        corner2x = rectangle.corner_2.x - ((rectangle.get_width() / 2) * k)
        corner2y = rectangle.corner_2.y - (rectangle.get_height() * k)

        corner1 = rg.Point(corner1x, corner1y)
        corner2 = rg.Point(corner2x, corner2y)

        new_rectangle.corner_1 = corner1
        new_rectangle.corner_2 = corner2

        new_rectangle.attach_to(window)

        for j in range(k):
            next_rectangle = new_rectangle.clone()

            corner_1x = new_rectangle.corner_1.x + (new_rectangle.get_width() * j)
            corner_2x = new_rectangle.corner_2.x + (new_rectangle.get_width() * j)

            next_rectangle.corner_1.x = corner_1x
            next_rectangle.corner_2.x = corner_2x

            next_rectangle.attach_to(window)
            window.render(0.05)

        window.render(0.05)


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
