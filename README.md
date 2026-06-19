->L12:Map Reduce

->Yarn (Yet Another Resource Manager) – pornește componentele ResourceManagerșiNodeManager; Yarn-ul este un framework pentru programarea job-urilor (jobscheduling)și gestionarea resurselor din cluster.

->Hadoop este un sistem de fișiere distribuit și totodată un sistem de procesare distribuităaunor seturi imense de date pe clustere folosind abordări paralele și distribuite

->Apache HDFS (Hadoop Distributed File System) 1 este un sistemde fișiere structurat peblocuri în care fiecare fișier este împărțit în blocuri de dimensiune pre-determinată, acesteafiindstocate într-un cluster cu una sau mai multe mașini de calcul. HDFS are oarhitecturămaster/slave

-> vezi ca fac efiguri la permisiuni de acces si la comanda de rulat, ai aici solutii:

chmod +x /home/hduser/exemplu_mapreduce/mapper.py 

chmod +x /home/hduser/exemplu_mapreduce/reducer.py

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming*.jar -input /user/hduser/input -output /user/hduser/output -mapper /home/hduser/exemplu_mapreduce/mapper.py -reducer /home/hduser/exemplu_mapreduce/reducer.py -file /home/hduser/exemplu_mapreduce/mapper.py -file /home/hduser/exemplu_mapreduce/reducer.py

->SURVIVAL KIT

su - hduser

start-all.sh

jps

mkdir ~/proiect_sortare

cd ~/proiect_sortare

mkdir input

cd input

nano date.txt

cd ..

touch mapper.py

touch reducer.py

chmod +x mapper.py reducer.py

hdfs dfs -rm -r /user/hduser/output_sortare

hdfs dfs -mkdir -p /user/hduser/input_sortare

hdfs dfs -put ~/proiect_sortare/input/* /user/hduser/input_sortare/

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming*.jar -input /user/hduser/input_sortare -output /user/hduser/output_sortare -mapper /home/hduser/proiect_sortare/mapper.py -reducer /home/hduser/proiect_sortare/reducer.py -file /home/hduser/proiect_sortare/mapper.py -file /home/hduser/proiect_sortare/reducer.py

hdfs dfs -ls /user/hduser/output_sortare

hdfs dfs -cat /user/hduser/output_sortare/part-00000

hdfs dfs -get /user/hduser/output_sortare/part-00000 ~/proiect_sortare/rezultat.txt

