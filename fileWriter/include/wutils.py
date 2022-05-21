
from datetime import datetime

def writeResult(path, js):
    file = open(path,'a')
    stamp = datetime.now()
    file.write("--------"+stamp.strftime('%Y-%m-%d %H:%M:%S')+"--------\n")
    
    for result in js["results"]:
        joy = result['joy']
        sorrow = result['sorrow']
        anger = result['anger']
        surprise = result['surprise']
        file_name = result['fileName']
        file.write("For file: "+file_name + "\n")
        file.write("---------Results---------\n")
        file.write("Felicidad: "+str(joy)+"\n")
        file.write("Tristesa: "+str(sorrow)+"\n")
        file.write("Enojo: "+str(anger)+"\n")
        file.write("Sorpresa: "+str(surprise)+"\n")
        file.write("-----------End-----------\n")
    file.close()


