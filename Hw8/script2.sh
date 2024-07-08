# 2. Вывести с помощью цикла while все четные числа от 0 до 100 включительно.
counter=0
while [ $counter -le 100 ]
do
    echo $counter
    ((counter += 2))
done