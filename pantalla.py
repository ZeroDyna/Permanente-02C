import curses

from ui.keyboard import Keyboard
from ui.screen import Screen
from ui.status_bar import draw_status_bar


def main(stdscr: 'curses._CursesWindow'):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)

    curses.curs_set(0)
    stdscr.nodelay(True)

    items = [
        ['7', '8', '9', '/'],
        ['4', '5', '6', '^'],
        ['1', '2', '3', '-'],
        ['0', 'x', 'y', '+'],
    ]
    keyboard = Keyboard(stdscr, items)
    screen = Screen(stdscr, keyboard.width)
    
    while True:
        stdscr.erase()
        stdscr.attron(curses.A_BOLD | curses.color_pair(1))
        keyboard.draw()
        screen.draw()

        draw_status_bar(stdscr)

        key = stdscr.getch()
        if key == curses.KEY_UP:
            keyboard.move_vertically(step=-1)
        elif key == curses.KEY_DOWN:
            keyboard.move_vertically(step=1)
        elif key == curses.KEY_LEFT:
            keyboard.move_horizontally(step=-1)
        elif key == curses.KEY_RIGHT:
            keyboard.move_horizontally(step=1)
        elif key == ord('\n'):
            character = keyboard.get_key()
            
            screen.set_content(screen_content)
        elif key == ord('q'):
            break
if __name__ == '__main__':
    curses.wrapper(main)

