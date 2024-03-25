import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(0,0,"Welcome to the Speed typing test!")
    stdscr.addstr("\nPress any key to start!")
    stdscr.refresh()
    stdscr.getkey()

def wpm_tester(stdscr):
    target_text="Hello this typing speed game please enjoy writing!"
    current_text=[]
    
    while True:
        key=stdscr.getkey()

        if ord(key)==27:
            break
        current_text.append(key)
        stdscr.clear()
        stdscr.addstr(target_text)
        

        for char in current_text:
            stdscr.addstr(char,curses.color_pair(1))    
        stdscr.refresh()

def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)
    
    start_screen(stdscr)
    wpm_tester(stdscr)

wrapper(main)
