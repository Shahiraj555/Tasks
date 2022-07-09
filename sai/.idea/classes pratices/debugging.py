import logging as lg
lg.basicConfig(filename='test.log', level=lg.INFO,format='%(asctime)s,%(message)s')
lg.info('this is my first info code')
lg.warning('this is warning sign')
lg.error('this is error')
lg.critical('this is crtical')
l=[1,2,4,5,6,3]
for i in l:
    if i==5:
        lg.info(i)
        lg.warning('2 has appear')
lg.shutdown()