
###################################
### image from argv
### convert in ascii art
### create html, matrix, xml?
###################################

from sys import argv
from typing import Tuple, NewType
import numpy as np
import cv2

CHARACTERS = (' ', '.', '°', '*', 'o', 'O', '#', '@')
MAX_INTENSITY = 255*4
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ASCII Art</title>
</head>
<body>
    <div style="background-color: black; color: white; line-height: 10px">
        <pre>{}</pre>
    </div>
</body>
</html>
"""

def main() -> None:
    #apro img
    img_name = argv[1]
    img = cv2.imread(img_name,-1)

    #conversione
    ascii = '' #store dell'img convertita in stringa
    rows = len(img) #righe, altezza
    cols = len(img[0]) #colonne, larghezza
    #per ogni riga...
    for row in range(rows):
        #...ogni pixel...
        for col in range(cols):
            #...calcolo intensità pixel nella scala di grigi e scelgo carattere corrispondente...
            intensity = (sum(img[row, col]) / MAX_INTENSITY)
            ascii += CHARACTERS[round(intensity * len(CHARACTERS))]
        #...aggiungo un a capo a fine riga
        ascii += '\n'

    #stampa a schermo
    print(ascii)

    #stampa in html
    html = open(img_name + '.htm', 'w')
    html.write(HTML_TEMPLATE.format(ascii))

if __name__ == '__main__':
    main()