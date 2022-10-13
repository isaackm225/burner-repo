import csv

def t() -> None:
        with open(r"D:\Programming\PYTHON\Envie-Bot\Reports\Delinquency Report\test1.csv", "r+", newline="") as test1, open(r"D:\Programming\PYTHON\Envie-Bot\Reports\Delinquency Report\test2.csv", "r", newline="") as test2:
            reader1 = csv.DictReader(test1,dialect="excel", delimiter=",", quotechar='"',quoting=csv.QUOTE_MINIMAL)
            reader2 = csv.DictReader(test2,dialect="excel", delimiter=",", quotechar='"',quoting=csv.QUOTE_MINIMAL)
            writer1 = csv.DictWriter(test1, fieldnames=reader1.fieldnames,dialect="excel", delimiter=",", quotechar='"',quoting=csv.QUOTE_MINIMAL)
            for set in reader2:
                print('='* 100)
                print('New set')
                print(set[reader2.fieldnames[0]]) #prints out each line using the first row as dictionnary key
                for num in reader1:
                    print(num[reader1.fieldnames[0]])
                    pass

t()