import os
import pandas as pd
import xml.etree.ElementTree as ET


def convert_voc_to_csv(input_dir, output_csv):
    data = []  # Lista para almacenar las filas del CSV

    for filename in os.listdir(input_dir):
        if not filename.endswith('.xml'):
            continue  # Solo procesar archivos XML

        tree = ET.parse(os.path.join(input_dir, filename))
        root = tree.getroot()

        image_filename = root.find('filename').text

        # Procesar objetos en cada imagen
        for obj in root.findall('object'):
            category_name = obj.find('name').text
            bndbox = obj.find('bndbox')
            xmin = int(bndbox.find('xmin').text)
            ymin = int(bndbox.find('ymin').text)
            xmax = int(bndbox.find('xmax').text)
            ymax = int(bndbox.find('ymax').text)

            # Agregar datos a la lista
            data.append([image_filename, xmin, ymin,
                        xmax, ymax, category_name])

    # Crear un DataFrame de pandas y guardarlo como CSV
    df = pd.DataFrame(
        data, columns=['filename', 'xmin', 'ymin', 'xmax', 'ymax', 'class'])
    df.to_csv(output_csv, index=False)

    print(f"Archivo CSV guardado en {output_csv}")


# Ejemplo de uso
# Cambia esta ruta según tus necesidades
input_dir = 'dataset/data/boundingBoxes/'
output_csv = 'dataset/dataset.csv'
convert_voc_to_csv(input_dir, output_csv)
