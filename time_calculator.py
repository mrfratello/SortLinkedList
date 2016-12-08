from importlib import import_module
import random
import time
import timeit
import sys

N = 100

class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()
         
    def __exit__(self, type, value, traceback):
        self.end = time.time()
        self.secs = self.end - self._startTime
        self.msecs = self.secs * 1000  # millisecs
        print('elapsed time: %f ms' % self.msecs)
        
        #print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))


print('>>> START <<<')
print(sys.argv)


if len(sys.argv) == 5 or len(sys.argv) == 7:
    path = None
    object_name = None
    object_method = None
    for i in range(1, len(sys.argv)):
        try:
            if sys.argv[i] == '-path':
                path = sys.argv[i+1]
            if sys.argv[i] == '-object_name':
                object_name = sys.argv[i+1]
            if sys.argv[i] == '-object_method':
                object_method = sys.argv[i+1]
        except IndexError as err:
            sys.exit(str(err))
    if path and object_name and object_method:
        try:
            module = import_module(path)
            obj = module.__dict__[object_name]
            instance = obj()
            if object_name == "SinglyLinkedList":
                for t in random.sample(range(1, N + 1), N):
                    instance.add(t)
            method = getattr(instance, object_method)
            with Profiler() as p:
                method()
                #print(timeit.timeit("singky_linked_list.sort_2()", setup="from __main__ import singky_linked_list", number=1))
            # print(instance)
        except Exception as err:
            print(str(err))
else:
    print("Введите путь к модулю и имя функции")
