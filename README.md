🟢📚 Para hacer uso del programa se debe instalar la librería simpy, para ello usa el comando en terminal:
pip install simpy
Para correr el programa, ejecuta en terminal el comando:
python programa.py 📚🟢


🟣 Para este programa en Python, maximizaremos el volumen de una caja con la restricción de que el material utilizado para fabricar las caras es limitado. 
Esto implica que el área superficial total de la caja estará acotada, lo cual nos permite establecer una ecuación de restricción en función de las dimensiones de la caja. 📦

El programa hará lo siguiente:


🔹 Definir el volumen 
𝑉=𝑥⋅𝑦⋅ℎ como la función objetivo a maximizar.


🔹 Usar la restricción de área 2⋅(𝑥⋅𝑦+𝑥⋅ℎ+𝑦⋅ℎ)=𝐴𝑡𝑜𝑡𝑎𝑙 para expresar ℎ en términos de 𝑥, 𝑦, y 𝐴𝑡𝑜𝑡𝑎𝑙​.


🔹 Reemplazar 
ℎ en la función de volumen para obtener una función 𝑉 en términos de 𝑥, 𝑦 y 𝐴𝑡𝑜𝑡𝑎𝑙​ únicamente.

🔹 Calcular las derivadas parciales de 𝑉 respecto a 𝑥 y 𝑦, igualarlas a cero y resolver el sistema de ecuaciones resultante para encontrar los valores de 𝑥 y 𝑦 que maximizan el volumen.


🔹 Calcular el valor de ℎ usando los valores obtenidos de 𝑥 y 𝑦, y verificar que 𝑥, 𝑦 y ℎ sean todos positivos.

🔹 Imprimir los valores óptimos de 𝑥, 𝑦 y ℎ que maximizan el volumen, junto con el volumen máximo alcanzado, todo en las unidades seleccionadas por el usuario.

🔹 Permitir al usuario repetir el cálculo ingresando diferentes valores de 𝐴𝑡𝑜𝑡𝑎𝑙​ y unidades hasta que decida terminar el programa.
