#!/bin/bash

# Check if the gzipped CSV file is provided as an argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <csv_file.gz>"
    exit 1
fi

gz_file="$1"

# Check if the file exists
if [ ! -f "$gz_file" ]; then
    echo "Error: File '$gz_file' not found."
    exit 1
fi

# Process the gzipped CSV file and filter data
gzip -dc "$gz_file" | awk -F',' 'BEGIN { OFS="," }
    NR==1 {
        # Print only the required headers
        print "new_id,old_id,img_path,img,true_BP,pred_BP,pred_BP_conf,true_SOD_G,BP_of_true_SOD_G,pred_SOD_G,pred_SOD_G_conf,true_SOD_M,BP_of_true_SOD_M"
    }
    NR>1 && ($15 == "head" || $16 == "head") && ($21+0 == 1.0) { 
        # Print only the required columns
        print $1,$2,$3,$4,$15,$16,$17,$18,$19,$20,$21,$22,$23
        #print $21
    }' > stg3heads.csv

echo "Filtered results saved to stg3heads.csv"
