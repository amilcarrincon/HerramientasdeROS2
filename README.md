# EuRoC MAV Dataset
El EuRoC MAV Dataset se puede descargar desde su página oficial (https://projects.asl.ethz.ch/datasets/doku.php?id=kmavvisualinertialdatasets), donde puedes elegir entre secuencias de vuelo como V1_01_easy, V1_02_medium, V1_03_difficult, entre otras. Para obtenerlo, descarga el archivo zip correspondiente, descomprímelo y, si lo deseas, utiliza herramientas como euroc2bag para convertir los datos en formato rosbag, compatible con ROS. Este dataset es muy valioso porque contiene datos completos de sensores utilizados en robótica aérea: cámaras estéreo, IMU y datos de posición real (ground truth). Esto lo hace ideal para desarrollar, probar y validar algoritmos de localización, mapeo y control de movimiento en drones y vehículos aéreos autónomos.

# Pasos
1️Crea una carpeta para almacenar el dataset.
2️Descarga el archivo zip del dataset (por ejemplo, V1_01_easy).
3️Descomprime el archivo zip.
4️Clona y construye el repositorio euroc2bag para convertir los datos a rosbag.
5️Usa euroc2bag para convertir los datos descomprimidos a un archivo .bag reproducible en ROS 2.
