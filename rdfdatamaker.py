import csv

#open csv file for reading
#fp = open ('OrolProg.csv', 'r', newline='', encoding='utf-8')
with open ('OrolProg.csv', 'r', newline='', encoding='utf-8') as ifp:
    with open ('rdfdata.csv', 'w', newline='') as ofp:
        ir = csv.reader(ifp)
        writer = csv.writer(ofp)

        header = next(ir)
        # iterate over table rows in csv file

        for i, row in enumerate(ir):
            for j, item in enumerate(row):
                #writer.writerow([i+1, header[j],item])
                #writer.writerow([''+str(i), header[j], 'http://dilab77.ionio.gr/sw/p14psar/myvocab#'+str(item)])
                if j==0 or j==1 or j==2:
                    #print(i+1, header[j], 'l:'+str(item))
                    writer.writerow(['b:'+str(i+1), 'http://dilab77.ionio.gr/sw/p14psar/myvocab#'+str(header[j].replace('/', '%2f').replace(' ', '%20')), ''+str(item.replace(' ', '%20'))])
                if j==3 or j==4 or j==5:
                    #print(i+1, header[j], 'u:'+str(item))
                    #item = item.replace(' ', '%20')
                    #item = item.replace('/', '%2f')
                    writer.writerow(['b:'+str(i+1), 'http://dilab77.ionio.gr/sw/p14psar/myvocab#'+str(header[j].replace('/', '%2f').replace(' ', '%20')), 'http://dilab77.ionio.gr/sw/p14psar/resource/'+str(item.replace(' ', '%20'))])
                #print(i+1, header[j],item)
                #print(i+1, header[j],item)
                #print(i+1, row)
                #print('Την {}, και ώρα {} έχετε το μάθημα {} με τον/ην {} στo/η {}.'.format(day, time, row[3], row[5], row[4]))
