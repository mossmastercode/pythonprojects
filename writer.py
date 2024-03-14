import curses
from curses import wrapper
def main(stdscr):
     stdscr.clear()
     stdscr.addstr("Hello Coders!")
     stdscr.refresh()
wrapper(main)