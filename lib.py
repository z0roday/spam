from platform import node, system, release; Node, System, Release = node(), system(), release() 
from os import system, name; system('clear' if name == 'posix' else 'cls')
from re import match, sub
from threading import Thread, active_count
import urllib3; urllib3.disable_warnings()
from time import sleep
import webbrowser