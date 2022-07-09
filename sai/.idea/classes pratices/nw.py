import logging as lg
lg.basicConfig(filename='ss.log ', level=lg.INFO,format='%(asctime)s %(message)s')

try:

    with open('divisi.log','r'):


        lg.info('we read successfully')
except Exception as e:

    lg.critical('this is situation')
    lg.exception(e)





