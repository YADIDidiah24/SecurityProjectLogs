logger -t SqlInjectionTest -p auth.notice "Sql Injection Test has started and below are the results"
(echo > output.txt; sqlmap -u http://127.0.0.1:9080/process --level 3 --risk 3 --dbs) | tee -a output.txt
grep -E 'CRITICAL|WARNING' output.txt | sudo tee -a /var/log/auth.log
logger -t SqlInjectionTestFinished -p auth.notice "Sql Injection has Finished."
