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
cd volatility
./vol -f cridex.vmem --profile=Win7SP1x64 psxview|awk '{print $4}'|grep 'False'|wc -l >>features.txt
./vol -f cridex.vmem --profile=Win7SP1x64 psxview|awk '{print $2}'|grep '*'|wc -l >>features.txt
./vol -f cridex.vmem --profile=Win7SP1x64 psxview|awk '{print $6}'|grep 'False'|wc -l >>features.txt
./vol -f cridex.vmem --profile=Win7SP1x64 psxview|awk '{print $7}'|grep 'False'|wc -l>>features.txt
./vol -f cridex.vmem --profile=Win7SP1x64 psxview|awk '{print $8}'|grep 'False'|wc -l>>features.txt
./vol -f cridex.vmem --profile=Win7SP1x64 psxview|awk '{print $9}'|grep 'False'|wc -l>>features.txt
./vol -f cridex.vmem --profile=Win7SP1x64 psxview|awk '{print $10}'|grep "False"|wc -l>>features.txt
np=$(./vol -f cridex.vmem --profile=Win7SP1x64 psxview |awk '{print $4}'|grep 'True'|wc -l);dll=$(./vol -f cridex.vmem --profile=Win7SP1x64 psxview |tail -n +3|wc -l);echo " $dll $np "|awk '{printf "%f\n",$2/$1}' >>features.txt
np=$(./vol -f cridex.vmem --profile=Win7SP1x64 psxview |awk '{print $2}'|grep -v '*'|wc -l);dll=$(./vol -f cridex.vmem --profile=Win7SP1x64 psxview |tail -n +3|wc -l);echo " $dll $np "|awk '{printf "%f\n",$2/$1}' >>features.txt
np=$(./vol -f cridex.vmem --profile=Win7SP1x64 psxview |awk '{print $6}'|grep 'True'|wc -l);dll=$(./vol -f cridex.vmem --profile=Win7SP1x64 psxview |tail -n +3|wc -l);echo " $dll $np "|awk '{printf "%f\n",$2/$1}' >>features.txt
np=$(./vol -f cridex.vmem --profile=Win7SP1x64 psxview |awk '{print $7}'|grep 'True'|wc -l);dll=$(./vol -f cridex.vmem --profile=Win7SP1x64 psxview |tail -n +3|wc -l);echo " $dll $np "|awk '{printf "%f\n",$2/$1}' >>features.txt
np=$(./vol -f cridex.vmem --profile=Win7SP1x64 psxview |awk '{print $8}'|grep 'True'|wc -l);dll=$(./vol -f cridex.vmem --profile=Win7SP1x64 psxview |tail -n +3|wc -l);echo " $dll $np "|awk '{printf "%f\n",$2/$1}' >>features.txt
np=$(./vol -f cridex.vmem --profile=Win7SP1x64 psxview |awk '{print $9}'|grep 'True'|wc -l);dll=$(./vol -f cridex.vmem --profile=Win7SP1x64 psxview |tail -n +3|wc -l);echo " $dll $np "|awk '{printf "%f\n",$2/$1}' >>features.txt
np=$(./vol -f cridex.vmem --profile=Win7SP1x64 psxview |awk '{print $10}'|grep 'True'|wc -l);dll=$(./vol -f cridex.vmem --profile=Win7SP1x64 psxview |tail -n +3|wc -l);echo " $dll $np "|awk '{printf "%f\n",$2/$1}' >>features.txt
mv features.txt /home/kali/volatility3
cd ..
cd volatility3
python3 vol.py -f cridex.vmem windows.svcscan | awk '{print $7}' | tail -n +5 | sort | uniq | wc -l>>features.txt
python3 vol.py -f cridex.vmem windows.svcscan |awk '{print $6}'|grep "KERNEL_DRIVER"|wc -l>>features.txt
python3 vol.py -f cridex.vmem windows.svcscan |awk '{print $6}'|grep "OWN_PROCESS"|grep -v "INTERACTIVE_PROCESS"|wc -l>>features.txt
python3 vol.py -f cridex.vmem windows.svcscan |awk '{print $6}'|grep "SHARE_PROCESS"|wc -l>>features.txt
python3 vol.py -f cridex.vmem windows.svcscan |awk '{print $5}'|grep "RUNNING"|wc -l>>features.txt
python3 vol.py -f cridex.vmem windows.svcscan |awk '{print $6}'|grep "INTERACTIVE_PROCESS"|wc -l >>features.txt
python3 vol.py -f cridex.vmem windows.callbacks|tail -n +5|wc -l >>features.txt
python3 vol.py -f cridex.vmem windows.callbacks|awk '$3 == "ntoskrnl" {print}'|wc -l>>features.txt
