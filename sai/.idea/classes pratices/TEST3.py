import logging
logging.basicConfig(filename="division.file", level=logging.INFO ,format='%(asctime)s %(message)s')
def div(a,b):

  logging.info("The the two values are  %s and %s" , a,b)
  try:
    d=a/b
    logging.info('division done')
    logging.info('division of code is %s',d)
    return d
  except Exception as e:

    logging.exception(e)
div(10,100)




