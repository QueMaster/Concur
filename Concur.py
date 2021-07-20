import time # import time module to access time.time(), time.sleep()
import queue #to access functions: queue.empty(), queue.get(),queue.Queue(),etc


#Lines 6 to 13 define task()
def task(name, queue):
    while not queue.empty():
        delay = queue.get()
        init_time = time.time() # start time
        print(f"Task: {name} running")
        time.sleep(delay) # system input/output delay simulated
        print(f"Task: {name} total elapsed time: {(time.time()-init_time):.2f}")
    yield # within while not queue.empty() loop,
          #context switch is made and control is handed back 
              #to the while loop in main()


def main():
    """
    This is the entry point function for the program- invokes function task()
    """
    # Create the queue of 'processes'
    process_queue = queue.Queue()

    # Put some 'processes' in the queue
    for process in [15,10,5, 2]:
        process_queue.put(process)

    tasks = [task("ProcessP1", process_queue), task("ProcessP2", process_queue)]

    # Run the tasks
    init_time = time.time()
    done = False
    while not done:
        for t in tasks:
            try:
                next(t) # gives control back to task(),
                        #and continues its execution 
                        #after the point where yield was called
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True # while loop ends when all tasks have been 
                            #completed and removed from tasks

    print(f"\nTotal elapsed time: {(time.time() - init_time):.2f}")

if __name__ == "__main__": 
     main()
