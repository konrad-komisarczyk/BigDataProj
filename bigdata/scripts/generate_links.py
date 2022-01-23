import pandas as pd
import sys

webpages_list = pd.read_csv("/home/vagrant/bigdata/scripts/data/webpages_list.csv", header=None)[1]

min_webpage = int(sys.argv[1])
max_webpage = int(sys.argv[2])
chunk_size = 50
years_back = int(sys.argv[3])

for i in range(min_webpage, max_webpage, chunk_size):
    with open("/home/vagrant/bigdata/webpagesInputDir/chunk" + str(i), "w") as f:
        s = ""
        for webpage in webpages_list[i:(i + chunk_size)]:
            for year in range(2022 - years_back, 2022):
                s += "https://web.archive.org/web/" + str(year) + "0701010101/" + webpage + "\n"
        f.write(s)
