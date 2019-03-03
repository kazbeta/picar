import sys,tty,termios
class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def get():
    inkey = _Getch()
    while(1):
        k=inkey()
        state = 0
        #        if k!='':break
    if k=='\x1b[A':
            state = 1
            print("up"),
            print(state)
    elif k=='\x1b[B':
            state = -1
            print("down")
            print(state)
    elif k=='\x1b[C':
            state = 2
            print("right")
            print(state)
    elif k=='\x1b[D':
            state = 3
            print("left")
            print(state)
#    elif k==',':
#            print("<")
#    elif k=='.':
#            print(">")
    else:
            print("not an arrow key!")

def main():
    for i in range(0,20):
        get()

if __name__=='__main__':
    main()
