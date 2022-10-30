arr=$(awk -F'\t' 'BEGIN {OFS = FS} { if (length($8) >  100 ) print $2} ' instagram_posts.csv | head -10)

for i in $arr
do :
    if [ $i == -1 ];
    then echo User was not found;
    else awk -F '\t' -v i=$i '$1 == i {print $1, $2, $3, $4}' instagram_profiles.csv;
    fi
done