# face-recognition python
Para la ejecución de app.py construyendo la imágen:

```bash
  docker build -t face-recognition-app .
```
Luego

```bash
  docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --rm --name face-recognition-app face-recognition-app
```
