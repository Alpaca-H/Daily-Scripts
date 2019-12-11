cat random_ip2.txt | while read line
do
	ansible router_table -m "raw" -a "system-view ;ip route-static $line 32 10.0.5.124 ;"
done
