
# Auction Messaging

Este proyecto presenta la implementación y evaluación de tres técnicas de integración de sistemas: Publicador/Subscriptor, Colas y REST, siguiendo el ejemplo de integración de Mark Richards, et al. Se desarrollaron y probaron tres proyectos, cada uno con una técnica diferente, y se midió su desempeño en términos de desempeño.

## ¿Cómo usar este proyecto?

El código fuente del proyecto puede ser clonado directamente desde git, o descargando la última publicación disponible en [Releases](https://github.com/NicolasMonta1807/auction-messaging/releases).

### Dependencias

* Docker
* Python 3.12

### Ejecución

Dentro de la raiz del proyecto se encuentra un script de bash que se encarga de construir las imágenes de los contenedores de cada implementación dada.

Se debe dar permisos de ejecución antes de ejecutarlo:

```bash
chmod +x run.sh
./run.sh
```

### Pruebas
Para mayor información acerca de las pruebas realizadas para el análisis de Trade-Offs de cada mecanismo de comunicación, vea el [Documento de diseño](https://github.com/NicolasMonta1807/auction-messaging/blob/main/docs/auction-messaging%20-%20Design.pdf).



