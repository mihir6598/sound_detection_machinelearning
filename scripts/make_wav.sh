counter=1
for FILE in *; 
do 
    
    ffmpeg -i "$FILE" -vn "../public_dataset_wav/$counter.wav"
    counter=$((counter+1))
    echo $FILE; 
done