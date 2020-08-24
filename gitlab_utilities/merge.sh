for d in *;do #
              cd $d
               #It merges all the tex files and saves with the corresponding repository names in Merged directory
              perl ../latexpand  --empty-comments *.tex >../Merged/$d.'tex'
             
	      cd ..
       		
	       if [[ ! -d "$d"=="Merged" ]]; then
                     rm -rf $d
		   # echo $d	
               fi
 

done
~            

