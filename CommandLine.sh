arr=$(awk -F'\t' 'BEGIN {OFS = FS} { if (length($8) >  100 ) print $2} ' instagram_posts.csv | head -9)

for i in $arr
do :
    if [ $i == -1 ];
    then echo User was not found;
    else grep $i instagram_profiles.csv | awk '{print $1, $2, $3, $4}';
    fi
done