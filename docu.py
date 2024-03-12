import os
from PyPDF2 import PdfReader, PdfWriter

# Función para recorrer una carpeta y procesar los archivos PDF
def procesar_carpeta(ruta_carpeta):
    # Obtener la lista de archivos en la carpeta
    archivos = os.listdir(ruta_carpeta)
    
    # Inicializar contador para el nombre consecutivo
    contador = 39
    
    # Recorrer cada archivo en la carpeta
    for archivo in archivos:
        if archivo.endswith('.pdf'):
            # Construir la ruta completa al archivo
            ruta_archivo = os.path.join(ruta_carpeta, archivo)
            
            # Abrir el archivo PDF
            with open(ruta_archivo, 'rb') as file:
                reader = PdfReader(file)
                writer = PdfWriter()
                
                # Recorrer cada página del PDF y agregarla al nuevo archivo
                for page in reader.pages:
                    writer.add_page(page)
                
                # Construir el nuevo nombre del archivo
                nuevo_nombre = f"{contador}.pdf"
                nuevo_ruta_archivo = os.path.join(ruta_carpeta, nuevo_nombre)
                
                # Guardar el nuevo archivo PDF con el nombre consecutivo
                with open(nuevo_ruta_archivo, 'wb') as nuevo_file:
                    writer.write(nuevo_file)
                
                contador += 1

# Ruta de la carpeta que quieres procesar
ruta_carpeta = 'C:\Python\IMPU 1'

# Llamar a la función para procesar la carpeta
procesar_carpeta(ruta_carpeta)
