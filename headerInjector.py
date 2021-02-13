import requests
import getopt, sys
import queue
import threading

FILENAME = ""
ALL_HEADERS = [
    'Host',
    'X-Host',
    'X-Forwarded-Host',
    'X-Forwarded-Server',
    'X-HTTP-Host-Override',
    'Forwarded'
]

class myThread(threading.Thread):
    def __init__(self, urlQueue):
        threading.Thread.__init__(self)
        self.queue = urlQueue

    def run(self):
        opsInjection(self.queue) # FILL HERE

def getArgs():
    argumentList = sys.argv[1:]
    # Options
    options = "hf:"
    
    # Long options
    long_options = ["Help", "File"]    
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        
        # checking each argument
        for currentArgument, currentValue in arguments:
    
            if currentArgument in ("-h", "--Help"):
                print("Usage: Header Injection")
                print("-----------------------")
                print("-h or --Help for usage")
                print("-f or --File domains.txt for test list of domains")
                print(" ")
                sys.exit()
                
            elif currentArgument in ("-f", "--File"):
                global FILENAME
                FILENAME = currentValue
                
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))   

def readFile():
    file1 = open(FILENAME, 'r')
    lines = file1.readlines()
    return lines

def createThreads(threadCount, urlQueue, threads):
    for idx in range(threadCount):
        thread = myThread(urlQueue)
        thread.start()
        threads.append(thread)

def opsInjection(urlQueue):
    while True:
        if urlQueue.empty():
            return
        try:
            url = urlQueue.get()
            for h in ALL_HEADERS:
                headers = {h: 'xheader0reflectionx.com'}
                r = requests.get(url.strip(), headers=headers, timeout=1)
                if 'xheader0reflectionx.com' in r.text:
                    print(url.strip() + " -> " + h)
        except:
            pass
            #print("con error " + url.strip())

        urlQueue.task_done()

def main():
    getArgs()
    lines = readFile()
    threadCount = 25
    
    urlQueue = queue.Queue()
    threads = []
    
    for line in lines:
        urlQueue.put(line) 

    createThreads(threadCount, urlQueue, threads)

   

    for t in threads:
        t.join()

main()
