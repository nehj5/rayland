#!/usr/bin/env python3
from multiprocessing import Process, Pipe
from concurrent.futures import ProcessPoolExecutor
from pyray import *
from raylib import *
from math import cos, sin, pi
from os import popen
from time import sleep
     
                   
# communicate with os, need to has child_connToOs as param

#if tick > cooldown_aw:
    #cooldown_aw = tick+10
    #child_connToOS.send("firefox")
   
# convertion
def ffi_int(int):
    variable = ffi.new('int *', int)
    return variable


def lerp(a: float, b: float, t: float) -> float:
    """Linear interpolate on the scale given by a to b, using t as the point on that scale.
    Examples
    --------
        50 == lerp(0, 100, 0.5)
        4.2 == lerp(1, 5, 0.8)
    """
    return (1 - t) * a + t * b

def easeInOutSine(t):

    return t * t * (3.0 - 2.0 * t)























































def runInParallel(*fns): # used for multiprocessing func
  proc = []
  for fn in fns:
    p = Process(target=fn)
    p.start()
    proc.append(p)
  for p in proc:
    p.join()


def run_cpu_tasks_in_parallel(tasks):
    with ProcessPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            running_task.result()
