wget -q "https://drive.usercontent.google.com/download?id=1DtLuSPNR_D9eUD1YEO8ZgjJYV8rWjwLl&export=download&authuser=0&confirm=t&uuid=9899a54b-2a8e-4d75-a5f6-80bd0be178b3&at=AIrpjvNAzJqIkTyvd171DaYO5_W8:1737638733162" -O images.zip
unzip "images.zip"

clear

python main.py -p images/N38.jpeg
python main.py -p images/N107.jpeg
python main.py -p images/N116.jpeg
python main.py -p images/N201.jpeg
python main.py -p images/N202.jpeg
python main.py -p images/N241.jpeg


