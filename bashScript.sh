cd /home/kali/volatility3 
python3 vol.py -f cridex.vmem windows.pslist|tail -n +5|wc -l >features.txt
python3 vol.py -f cridex.vmem windows.pslist | awk '{print $2}' | tail -n +5 | sort | uniq | wc -l>>features.txt
python3 vol.py -f cridex.vmem windows.pslist| awk '{print $5}' |tail -n +5 | awk '{s+=$1} END {print s/NR}'>>features.txt
nh=$(python3 vol.py -f cridex.vmem windows.handles|tail -n +5|wc -l);np=$(python3 vol.py -f cridex.vmem windows.pslist |tail -n +5| wc -l);echo " $nh $np "|awk '{printf "%.2f\n",$1/$2}' >>features.txt
python3 vol.py -f cridex.vmem windows.dlllist|tail -n +5|wc -l >>features.txt
np=$(python3 vol.py -f cridex.vmem windows.pslist |tail -n +5| wc -l);dll=$(python3 vol.py -f cridex.vmem windows.dlllist |tail -n +5| wc -l);echo " $dll $np "|awk '{printf "%.2f\n",$1/$2}' >>features.txt
python3 vol.py -f cridex.vmem windows.handles|tail -n +5|wc -l >>features.txt
python3 vol.py -f cridex.vmem windows.handles| awk '{print $5}' |grep File |tail -n +5|wc -l >>features.txt
python3 vol.py -f cridex.vmem windows.handles| awk '{print $5}' |grep Event |tail -n +5|wc -l >>features.txt
python3 vol.py -f cridex.vmem windows.handles| awk '{print $5}' |grep Desktop |tail -n +5|wc -l >>features.txt
python3 vol.py -f cridex.vmem windows.handles| awk '{print $5}' |grep Key |tail -n +5|wc -l >>features.txt
python3 vol.py -f cridex.vmem windows.handles| awk '{print $5}' |grep Thread |tail -n +5|wc -l>>features.txt
python3 vol.py -f cridex.vmem windows.handles| awk '{print $5}' |grep Directory |tail -n +5|wc -l>>features.txt
python3 vol.py -f cridex.vmem windows.handles| awk '{print $5}' |grep Semaphore |tail -n +5|wc -l >>features.txt
python3 vol.py -f cridex.vmem windows.handles| awk '{print $5}' |grep Timer |tail -n +5|wc -l >>features.txt
python3 vol.py -f cridex.vmem windows.handles| awk '{print $5}' |grep Section |tail -n +5|wc -l >>features.txt
python3 vol.py -f cridex.vmem windows.handles| awk '{print $5}' |grep Mutant |tail -n +5|wc -l >>features.txt
python3 vol.py -f cridex.vmem windows.ldrmodules| awk '{print $4}'| grep -e "False"  | wc -l >>features.txt
python3 vol.py -f cridex.vmem windows.ldrmodules| awk '{print $5}'| grep -e "False"  | wc -l>>features.txt
python3 vol.py -f cridex.vmem windows.ldrmodules| awk '{print $6}'| grep -e "False"  | wc -l>>features.txt
python3 vol.py -f cridex.vmem windows.malfind|grep ".exe"|wc -l>>features.txt
python3 vol.py -f cridex.vmem windows.modules|awk '{print $4}'|tail -n +5|sort|uniq|wc -l>>features.txt  
mv features.txt /home/kali/volatility
cd ..
