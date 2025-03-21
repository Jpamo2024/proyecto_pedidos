import pandas as pd

#Esta es la modificacion para la tercera version

# Ruta del archivo TXT
archivo_txt = 'pedidos.txt'

try:
    # Leer el archivo TXT
    data = pd.read_csv(archivo_txt, delimiter='|')
    
    # Guardar los datos en un archivo CSV temporal
    archivo_csv = 'clientes.csv'
    data.to_csv(archivo_csv, index=False)
    
    print(f"Datos leídos y guardados PARA LA TERCERA VERSION en {archivo_csv}")
except Exception as e:
    print(f"Error al leer el archivo: {e}")
