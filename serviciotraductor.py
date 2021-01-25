impresoras = {}

def addimpresora(printerName, printer):
    impresoras[printerName] = printer
    print impresoras

def getimpresora(printerName):
    return impresoras[printerName]

def exist(printerName):
    print 'impresoras', impresoras
    return printerName in impresoras