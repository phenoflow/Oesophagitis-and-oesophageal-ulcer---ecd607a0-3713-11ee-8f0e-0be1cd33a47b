# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"J101115","system":"readv2"},{"code":"J101300","system":"readv2"},{"code":"J101400","system":"readv2"},{"code":"J101500","system":"readv2"},{"code":"J101y00","system":"readv2"},{"code":"J101z00","system":"readv2"},{"code":"J102200","system":"readv2"},{"code":"J102400","system":"readv2"},{"code":"J10y300","system":"readv2"},{"code":"10060.0","system":"med"},{"code":"14760.0","system":"med"},{"code":"15579.0","system":"med"},{"code":"16450.0","system":"med"},{"code":"16605.0","system":"med"},{"code":"24021.0","system":"med"},{"code":"2489.0","system":"med"},{"code":"2535.0","system":"med"},{"code":"34836.0","system":"med"},{"code":"35037.0","system":"med"},{"code":"39323.0","system":"med"},{"code":"42150.0","system":"med"},{"code":"47694.0","system":"med"},{"code":"49926.0","system":"med"},{"code":"51013.0","system":"med"},{"code":"5283.0","system":"med"},{"code":"57039.0","system":"med"},{"code":"58603.0","system":"med"},{"code":"592.0","system":"med"},{"code":"7104.0","system":"med"},{"code":"94752.0","system":"med"},{"code":"98929.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('oesophagitis-and-oesophageal-ulcer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["oesophagitis-and-oesophageal-ulcer---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["oesophagitis-and-oesophageal-ulcer---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["oesophagitis-and-oesophageal-ulcer---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
