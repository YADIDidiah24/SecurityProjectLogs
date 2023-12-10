logger -t DotTraversal -p auth.notice "Dot Traversal(../) Test has started and below are the results"
cd dotdotpwn
{ echo > ../output.txt; sudo ./dotdotpwn.pl -m http -h 127.0.0.1; } | tee -a ../output.txt
cd ..
tail -n 5 output.txt >> /var/log/auth.log
logger -t DotTraversalFinished -p auth.notice "Dot Traversal(../) Test has finished"
