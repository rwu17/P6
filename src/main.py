from readWriteFiles import ReadWriteLogFiles as rwlf
from robocupclient import RunServerMonitor as rsm
from commentator import Commentator
from time import sleep


if __name__ == "__main__":

    # Run shells
    rsm = rsm()
    rsm.runShells()

    sleep(5) # wait for network to setup

    rwlf = rwlf()
    rwlf.multiThreadRWFiles()
    
    commentator = Commentator(rwlf)
    while True:
        commentator.commentate()
