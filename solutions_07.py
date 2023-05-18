# Stage 1
# Anagramme

import itertools

def anagram(lettres):
    resultat = []
    permutations_lettres = [''.join(p) for p in itertools.permutations(lettres)]
    for p in permutations_lettres:
        if p.startswith('d'):
            resultat.append(p)
    return resultat

resultat = anagram('ezduo')
print(resultat)

# Stage 2
# Code César

def decrypt(texte, decal):
    res = ''
    for char in texte:
        if char.isalpha():
            if char.isupper():
                shifted_char = chr((ord(char) - decal - 65) % 26 + 65)
            else:
                shifted_char = chr((ord(char) - decal - 97) % 26 + 97)
            res += shifted_char
        else:
            res += char
    return res

texte = "Nxaanl m fau omymdmpq, eu fg z'qe bme adusuzmudq pq xm bxmzqfq pq fqe sqaxuqde, fg me egdqyqzf nqeauz p'mupq. V'mu yau yqyq qfq qzrqdyq uou bmd xq bmeeq qf v'mu pqoaghqdf oayyqzf eadfud pq oq xmnadmfaudq tgymuz. Vq hmue pazo f'uzpucgqd xqe qfmbqe m eguhdq: fagf p'mnadp, smdpq qz fqfq cgq fg hme pqhaud oaxxqofqd cgmfdq yadoqmgj p'gzq omdfq cgu hm qfdq zqoqeemudq bagd xm pqdzuqdq qfmbq pq faz qhmeuaz. Ymuzfqzmzf fg pqhdme pqodkbfqd gz yaf pq bmeeq zgyqducgq bagd bmeeqd xm bdqyuqdq lazq, qzegufq fg fdaghqdme gz oapq yadeq; ymue zq f'uzcguqfq bme v'mu xmueeq gzq zafq mhqo bagd f'mupqd m xq pqoapqd. Qf qzruz fg pqhdme rdmzotud xm badfq ruzmxq mhqo xm omdfq pazf fg mgdme dmeeqynxq xqe rdmsyqzfe. Qf hauxm, fg eqdme xundq muzeu qf zq fdmuzq bme mhmzf pq fq rmudq ombfgdqd pq zaghqmg !"
decal = 12
res = decrypt(texte, decal)
print(res)

# Stage 3
# Image 1

import csv
from PIL import Image

def export_rgb_to_csv(image_file, output_csv_file):
    img = Image.open(image_file).convert('RGBA')
    width, height = img.size

    with open(output_csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['X', 'Y', 'R', 'G', 'B'])

        for y in range(height):
            for x in range(width):
                r, g, b, a = img.getpixel((x, y))
                csv_writer.writerow([x, y, r, g, b])

    print(f"RGB values have been exported to {output_csv_file}.")

def display_original_image(image_file):
    img = Image.open(image_file)
    img.show()

def display_image_from_csv(csv_file):
    with open(csv_file, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)

        pixels = []
        for row in csv_reader:
            x, y, r, g, b = map(int, row)
            pixels.append((x, y, (r, g, b)))

        # Tri les pixels par leur coordonnées
        pixels.sort(key=lambda p: (p[1], p[0]))

        width = pixels[-1][0] + 1
        height = pixels[-1][1] + 1

        # Créé une image de la même taille que l'originale
        img = Image.new('RGB', (width, height))

        # Défini les pixels de la nouvelle image
        for x, y, color in pixels:
            img.putpixel((x, y), color)

        img.show()

csv_file = 'Tokotoro.csv'

display_image_from_csv(csv_file)

# Stage 4
# Mot de passe

mot_de_passe = 0
chaine = "sérieux"
for caractere in chaine:
    mot_de_passe += ord(caractere)
print(mot_de_passe)

# Stage 6
# Code Morse

morse_alph = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '-----': '0', '--..--': ',', '.-.-.-': '.', '..--..': '?', '-..-.': '/',
    '-....-': '-', '-.--.': '(', '-.--.-': ')', '.-.-.': '+', '-...-': '=',
    '.-..-.': '"', '.----.': "'", '-.--.': '{', '}': '-.-.--', ' ': '/'
}

def decrypt_morse(morse):
    morse_words = morse.strip().split('/')
    words = []
    for morse_word in morse_words:
        letters = morse_word.strip().split()
        word = ''
        for letter in letters:
            if letter in morse_alph:
                word += morse_alph[letter]
        words.append(word)
    return ' '.join(words)

morse = '.--- .----. .- .. / .-. . ..- ... ... .. / .- / -- .----. . -.-. .... .- .--. .--. .--. . .-. --..-- / ... .- ..- ...- . --.. -....- -- --- ..'
print(decrypt_morse(morse))

# Stage 5
# Image 2

import csv
from PIL import Image

def export_rgb_to_csv(image_file, output_csv_file):
    img = Image.open(image_file).convert('RGBA')
    width, height = img.size

    with open(output_csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['X', 'Y', 'R', 'G', 'B'])

        for y in range(height):
            for x in range(width):
                r, g, b, a = img.getpixel((x, y))
                csv_writer.writerow([x, y, r, g, b])

    print(f"RGB values have been exported to {output_csv_file}.")

def display_original_image(image_file):
    img = Image.open(image_file)
    img.show()

def display_image_from_csv(csv_file):
    with open(csv_file, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)

        pixels = []
        for row in csv_reader:
            x, y, r, g, b = map(int, row)
            pixels.append((x, y, (r, g, b)))

        pixels.sort(key=lambda p: (p[1], p[0]))

        width = pixels[-1][0] + 1
        height = pixels[-1][1] + 1

        img = Image.new('RGB', (width, height))

        for x, y, color in pixels:
            img.putpixel((x, y), color)

        img.show()

if __name__ == '__main__':
    csv_file = 'Tokopisco.csv'

    display_image_from_csv(csv_file)

# Stage 7
# Image 3

import csv
from PIL import Image

def export_rgb_to_csv(image_file, output_csv_file):
    img = Image.open(image_file).convert('RGBA')
    width, height = img.size

    with open(output_csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['X', 'Y', 'R', 'G', 'B'])

        for y in range(height):
            for x in range(width):
                r, g, b, a = img.getpixel((x, y))
                csv_writer.writerow([x, y, r, g, b])

    print(f"RGB values have been exported to {output_csv_file}.")

def display_original_image(image_file):
    img = Image.open(image_file)
    img.show()

def display_image_from_csv(csv_file):
    with open(csv_file, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)

        pixels = []
        for row in csv_reader:
            x, y, r, g, b = map(int, row)
            pixels.append((x, y, (r, g, b)))

        pixels.sort(key=lambda p: (p[1], p[0]))

        width = pixels[-1][0] + 1
        height = pixels[-1][1] + 1

        img = Image.new('RGB', (width, height))

        for x, y, color in pixels:
            img.putpixel((x, y), color)

        img.show()

if __name__ == '__main__':
    csv_file = 'Tokorico.csv'

    display_image_from_csv(csv_file)

# Stage 8
# Image 4
import csv
from PIL import Image

def export_rgb_to_csv(image_file, output_csv_file):
    img = Image.open(image_file).convert('RGBA')
    width, height = img.size

    with open(output_csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['X', 'Y', 'R', 'G', 'B'])

        for y in range(height):
            for x in range(width):
                r, g, b, a = img.getpixel((x, y))
                csv_writer.writerow([x, y, r, g, b])

    print(f"RGB values have been exported to {output_csv_file}.")

def display_original_image(image_file):
    img = Image.open(image_file)
    img.show()

def display_image_from_csv(csv_file):
    with open(csv_file, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)

        pixels = []
        for row in csv_reader:
            x, y, r, g, b = map(int, row)
            pixels.append((x, y, (r, g, b)))

        pixels.sort(key=lambda p: (p[1], p[0]))

        width = pixels[-1][0] + 1
        height = pixels[-1][1] + 1

        img = Image.new('RGB', (width, height))

        for x, y, color in pixels:
            img.putpixel((x, y), color)

        img.show()

if __name__ == '__main__':
    csv_file = 'Tokopiyon.csv'

    display_image_from_csv(csv_file)


# Stage 9

# Import de la bibliothèque PIL (Python Imaging Library)
from PIL import Image

def stitch_images(images, output_image_path):
    # Ouvrir les images
    img_files = [Image.open(image_path) for image_path in images]

    # Calcul des dimensions finales de l'image
    width = img_files[0].width + img_files[1].width
    height = img_files[0].height + img_files[2].height

    # Création d'un canvas vierge qui accueillera l'image finale
    stitched_image = Image.new('RGB', (width, height))

    # Collage des images sur le canvas aux coordonnées appropriées
    stitched_image.paste(img_files[0], (0, 0))
    stitched_image.paste(img_files[1], (img_files[0].width, 0))
    stitched_image.paste(img_files[2], (0, img_files[0].height))
    stitched_image.paste(img_files[3], (img_files[0].width, img_files[0].height))

    # Sauvegarde de l'image finale dans le dossier actuel
    stitched_image.save(output_image_path)

# Exemple d'usage de la fonction dans un dossier avec l'arborescence suivante:
# C:.
# │   main.py
# │   stitched_image.png <-- Image finale
# │
# └───images
#         Carte1.jpg
#         Carte2.jpg
#         Carte3.jpg
#         Carte4.jpg
image_paths = ['images/Carte1.jpg', 'images/Carte2.jpg', 'images/Carte3.jpg', 'images/Carte4.jpg']
output_image = 'image_assemblee.png'
stitch_images(image_paths, output_image)