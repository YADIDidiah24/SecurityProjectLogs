logger -t XssInjectionTest -p auth.notice "XSS Injection Test has started"
sleep 2
{ echo > output.txt; python XSStrike/xsstrike.py -u "http://127.0.0.1:9080/process"; } | tee -a output.txt
tail -n 5 output.txt >> /var/log/auth.log
logger -t XssInjectionTestFinished -p auth.notice "XSS Injection has finished"
