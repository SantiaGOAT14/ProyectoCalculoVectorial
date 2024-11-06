Para hacer uso del programa se debe instalar la librería simpy, para ello usa el comando en terminal:
pip install simpy
Para correr el programa, ejecuta en terminal el comando:
python maximos.py
Para este programa en Python, maximizaremos el volumen de una caja con la restricción de que el material utilizado para fabricar las caras es limitado. 
Esto implica que el área superficial total de la caja estará acotada, lo cual nos permite establecer una ecuación de restricción en función de las dimensiones de la caja.
El programa hará lo siguiente:

Definir el volumen 
𝑉=𝑥⋅𝑦⋅ℎ como función objetivo.
Usar la restricción de área para expresar 
ℎ en términos de 
𝑥 y 𝑦.
Reemplazar 
ℎ en la función de volumen para obtener una función en términos de 𝑥 y 𝑦 únicamente.
Calcular las derivadas parciales de 𝑉 con respecto a 𝑥 y 𝑦, igualarlas a cero, y resolver el sistema resultante para encontrar los valores de 𝑥 y 𝑦 que maximizan el volumen.
Calcular el valor de ℎ usando los valores obtenidos de 𝑥 y 𝑦.
Imprimir los valores óptimos de 𝑥, 𝑦, y ℎ que maximizan el volumen.
