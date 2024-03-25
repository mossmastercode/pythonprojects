import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(0,0,"Welcome to the Speed typing test!")
    stdscr.addstr("\nPress any key to start!")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr,target,current,wpm=0):
    stdscr.addstr(target)

    for i,char in enumerate(current):
            stdscr.addstr(0,i,char,curses.color_pair(1))  


def wpm_tester(stdscr):
    target_text="Hello this typing speed game please enjoy writing!"
    current_text=[]
    
    while True:
        stdscr.clear()
        display_text(stdscr,target_text,current_text)
        stdscr.refresh()

        key=stdscr.getkey()

        if ord(key)==27:
            break
        if key in ('KEY_BACKSPACE','\b','\x7f'):
            if len(current_text)>0:
                current_text.pop()
        else:
            current_text.append(key)


def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)
    
    start_screen(stdscr)
    wpm_tester(stdscr)

wrapper(main)
