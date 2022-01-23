#!/bin/bash
# hbase creating tables
hbase shell hbase_create_database

# hdfs creating directory for storing data
hdfs dfs -mkdir /user
hdfs dfs -mkdir /user/bigdata
hdfs dfs -mkdir /user/bigdata/data

# preparing links to download (most popular webpages from 0 to 50000, for last 20 years)

mkdir /home/vagrant/bigdata/webpagesInputDir
python /home/vagrant/bigdata/scripts/generate_links.py 0 50000 20
