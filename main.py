from tkinter import *
import math

# window setup ->>

top = Tk()
top.geometry('350x400')

frame = Frame(top, bg='dimgray')
frame.pack(fill=BOTH, expand=YES)

textField = Frame(frame)
textField.pack(fill=X, expand=YES)

buttonField = Frame(frame, bg='blue')
buttonField.pack(fill=BOTH, expand=YES)

exp_str = StringVar()
exp = Label(textField, bg=frame['bg'], anchor='ne', textvariable=exp_str,
            fg='lightgrey', font='Helvetica 10')
exp_str.set('')
exp.pack(side=TOP, fill=BOTH, expand=YES, ipady=5)

entry_str = StringVar()
entry = Entry(textField, relief=FLAT, bg='dimgray', fg='snow',
              justify='right', textvariable=entry_str, font="Ariel 23")
entry.pack(side=TOP, fill=BOTH, expand=YES)
entry_str.set('0')

# window setup end
# functions start


def configure_button(i, j):
    b.configure(width=6, bg='black', fg='white', relief=FLAT)
    b.grid(row=i, column=j, sticky='nsew')
    b.bind('<Enter>', lambda c: c.widget.configure(bg='grey'))
    b.bind('<Leave>', lambda c: c.widget.configure(bg='black'))


def add_text(text):
    if int(float(entry_str.get())) is 0:
        entry_str.set('')
    entry_str.set(entry_str.get() + str(text))


def func(obj):
    if isinstance(obj, int):
        add_text(obj)
        return

    if obj in f_list:
        f_list[obj]()
        return
    else:
        exp_str.set(exp_str.get() + entry_str.get() + obj)
        entry_str.set('0')


def eval_exp(reset=TRUE):
    s = exp_str.get()
    if s == '':
        s = '0'
    e = entry_str.get()
    se = s
    for i in range(len(s)):
        if s[i] == 'X':
            se = s[:i] + '*' + s[i+1:]
    if s[-1] in ['+', '-', 'X', '/']:
        if e == 0:
            r = eval(s[:-1])
        else:
            r = eval(se + e)
    else:
        r = eval(se)
    entry_str.set(r)
    if reset:
        exp_str.set('')
    return float(entry_str.get())


def sign_rev():
    exp_str.set(f'-({exp_str.get()}+{entry_str.get()})')
    eval_exp()


def clear():
    entry_str.set('0')
    exp_str.set('')


def recp():
    exp_str.set(f'(1/({entry_str.get()}))')
    eval_exp()


def bind_funcs():
    for i in range(0, 10):
        top.bind(i, lambda e=i: func(int(e.char)))

    top.bind("<Return>", lambda i: eval_exp())
    top.bind('/', lambda i='/': func('/'))
    top.bind('x', lambda i='x': func('X'))
    top.bind('+', lambda i='+': func('+'))
    top.bind('-', lambda i='-': func('-'))
    top.bind('*', lambda i='*': func('X'))
    top.bind('sq()', lambda i='sq': func('sq()'))
    top.bind(f'x\N{SUPERSCRIPT TWO}', lambda i='*': func(f'x\N{SUPERSCRIPT TWO}'))
    top.bind(f'\N{SUPERSCRIPT ONE}/x', lambda i='1/x': func(f'\N{SUPERSCRIPT ONE}/x'))
    top.bind('CE', NONE)
    top.bind('C', lambda i=0: func('C'))
    top.bind('BackSpace',
             lambda i=0: exp_str.set(exp_str.get()[:-1]) if len(entry_str.get()) is not 1 else entry_str.set('0'))
    top.bind('X', lambda i='x': func('X'))
    
    
# functions end constants start


buttonText = [['%', 'sq()', f'x\N{SUPERSCRIPT TWO}', f'\N{SUPERSCRIPT ONE}/x'],
              ['CE', 'C', '<-', '/'],
              [7, 8, 9, 'X'],
              [4, 5, 6, '-'],
              [1, 2, 3, '+'],
              ['+-', 0, '.', '=']]

f_list = {'%': NONE,
          'sq()': lambda: entry_str.set(math.sqrt(float(entry_str.get()))),
          f'x\N{SUPERSCRIPT TWO}': lambda: entry_str.set(float(entry_str.get())**2),
          f'\N{SUPERSCRIPT ONE}/x': recp,
          'CE': NONE,
          'C': lambda i=0: clear(),
          '<-': lambda i=0: entry_str.set(entry_str.get()[:-1]) if len(entry_str.get()) is not 1 else entry_str.set(
              '0'),
          '+-': sign_rev,
          '=': eval_exp}

buttons = [[Button(buttonField, text=f'{t}', command=lambda d=t: func(d)) for t in b] for b in buttonText]

bind_funcs()

# constants end Code section begin

for i, rw in enumerate(buttons):
    Grid.rowconfigure(buttonField, i, weight=1)
    for j, b in enumerate(rw):
        Grid.columnconfigure(buttonField, j, weight=1)
        configure_button(i, j)

top.mainloop()
