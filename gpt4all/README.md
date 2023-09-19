# Experimentos sobre modelos GPT4All

## Introducción

Este documento registra el desarrollo de cuatro experimentos realizados sobre dos modelos LLM (Large Language Model) del proyecto GPT4All.

Los experimentos realizados consisten en operaciones de autocompletado de texto y sesiones de chat, ejecutadas con el objetivo general de registrar las respuestas obtenidas y los respectivos tiempos de respuesta de cada modelo utilizado.

La información obtenida en estos experimentos pueda ayudar objetivamente en la decisión de aplicar o no, los modelos GPT4All utilizados en los experimentos, en un determinado proyecto de desarrollo de software.

## Sobre los modelos LLM utilizados

Los modelos que se utilizan en los experimentos, registrados en este documento, pertenecen al proyecto GPT4All.

[GPT4All](https://github.com/nomic-ai/gpt4all) es un proyecto, y al mismo tiempo una biblioteca de código abierto (_open source_) Python, que tiene como objetivo el hacer posible ejecutar modelos LLM (Large Language Model) de manera local y utilizando únicamente la CPU de una computadora. Siempre y cuando la CPU soporte [instrucciones AVX o AVX2](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions) y cuente con una RAM de entre 4 y 16 GB.

La lista completa de modelos LLM que se pueden utilizar con GPT4All, a los cuales, en adelante, nos referimos como _modelos GPT4All_, se encuentran en el siguiente archivo JSON: [models.json](https://raw.githubusercontent.com/nomic-ai/gpt4all/main/gpt4all-chat/metadata/models.json)

De todos los modelos GPT4All se seleccionó a los siguientes dos modelos, en base a la configuracíon de hardware disponible para realizar los experimentos:

| Modelo                              | Tamaño en GB  | RAM requerida en GB |
|-------------------------------------|-------|---|
| orca-mini-3b.ggmlv3.q4_0.bin        |  1,79 | 4 |
| ggml-model-gpt4all-falcon-q4_0.bin  |  3,78 | 8 |

Fuente: [models.json](https://raw.githubusercontent.com/nomic-ai/gpt4all/main/gpt4all-chat/metadata/models.json)

### Directorio caché de modelos

Es importante observar que al ejecutar por primera vez
un código que utiliza un determinado modelo GPT4All dicho modelo es descargado automáticamente en un directorio caché: 
* `C:\Users\<Nombre-Usuario>\.cache\gpt4all`, en Windows, y
* `/home/<nombre-usuario>/.cache/gpt4all/`, en Fedora.

Al ejecutar el código que utiliza un determinado modelo GPT4All ya presente en el directorio caché, dicho modelo no será descargado nuevamente sino leído del directorio caché. 

## Sobre el entorno de ejecución utilizado

Para realizar los experimentos se utilizó la siguiente configuración de hardware y software:

* Hardware:
  * Procesador: Intel Core i3 de 64 bits
  * Memoria RAM: 8 GB
* Software:
  * Sistema operativo: 
    * Microsoft Windows 10 Pro
    * Fedora Workstation 38
  * Python 3.11.5.

## Sobre la ejecución de los experimentos

El código fuente utilizado para realizar los experimentos se encuentra en el archivo [`main.py`](main.py) de este repositorio.

Antes de realizar los experimentos, se ejecutaron los siguientes comandos, en el orden mostrado en la siguiente lista:
* [01-crear-entorno-virtual.bat](01-crear-entorno-virtual.bat)
* [02-instalar-paquetes.bat](02-instalar-paquetes.bat)

Observaciones:
+ Los anteriores comandos fueron escritos para ser ejecutados 
en el Símbolo del sistema (también llamdo _cmd_) del sistema operativo Windows.
+ A excepción del primer comando ([01-crear-entorno-virtual.bat](01-crear-entorno-virtual.bat)), todos los demás comandos que se presentan en este documento 
se pueden ejecutar sin modificación en la línea de comandos 
(también llamda _terminal_)
del sistema operativo Fedora.
* El comando [01-crear-entorno-virtual.bat](01-crear-entorno-virtual.bat) equivale a los siguientes comandos en el sistema operativo Fedora:
```bash
python -m venv .venv
source .venv/bin/activate
```

## Experimentos realizados

### Experimento: autocomplete-with-orca

* **Objetivo**: Autocompletar el texto `The capital of France is ` 
utilizando el modelo GPT4All `orca-mini-3b.ggmlv3.q4_0.bin`

* **Comando ejecutado**: [03-ejecutar-autocomplete-with-orca.bat](03-ejecutar-autocomplete-with-orca.bat)

* **Resultados obtenidos**:

| Operación       | Entrada | Salida |  Tiempo de respuesta en segundos |
|-------------------|---------|--------|----------------------:|
| Cargar modelo  | nombre del modelo: `orca-mini-3b.ggmlv3.q4_0.bin` | (modelo cargado en la RAM) | [*] `43,66`
| Autocompletar texto    | texto: `The capital of France is ` | `1. Paris` | `70,47` |

[*] El modelo ya estaba descargado en el [directorio caché de modelos](#directorio-caché-de-modelos) antes de ejecutar y registrar los datos de este experimento, como consecuencia de una ejecución anterior.

* **Conclusión**
  * Con la configuración de hardware y software utilizada, si el tiempo de respuesta al utilizar el modelo `orca-mini-3b.ggmlv3.q4_0.bin` es importante, se recomienda no utilizarlo, ya que es muy lento comparado con el tiempo de respuesta de [ChatGPT](https://chat.openai.com/), que en general es menor a un segundo.
  * Se recomienda ejecutar el experimento en una configuración de hardware y software con RAM de 16 GB o superior, para verificar si el tiempo de ejecución disminuye con respecto a los resultados registrados en este documento.

### Experimento: autocomplete-with-falcon

* **Objetivo**: Autocompletar el texto `The first computer was invented by ` 
utilizando el modelo GPT4All `orca-mini-3b.ggmlv3.q4_0.bin`

* **Comando ejecutado**: [03-ejecutar-autocomplete-with-orca.bat](03-ejecutar-autocomplete-with-orca.bat)

* **Resultados obtenidos**:

| Operación       | Entrada | Salida |  Tiempo de respuesta en segundos |
|-------------------|---------|--------|----------------------:|
| Cargar modelo  | nombre del modelo: `ggml-model-gpt4all-falcon-q4_0.bin` | (modelo cargado en la RAM) | [*] `122,96`
| Autocompletar texto    | texto: `The first computer was invented by ` | [**] `Babbage` | `222,22` |

[*] El modelo ya estaba descargado en el [directorio caché de modelos](#directorio-caché-de-modelos) antes de ejecutar y registrar los datos de este experimento, como consecuencia de una ejecución anterior.

[**] En algunas ejecuciones del experimento, el modelo autocompletaba el texto de entrada con textos como `Alan T` y `Ada`. 
Que el modelo devuelva respuestas, con significados diferentes, a una misma pregunta es un problema de los modelos LLM en general, llamado [_alucinación_](https://arxiv.org/abs/2202.03629).

* **Conclusión**
  * Con la configuración de hardware y software utilizada, si el tiempo de respuesta al utilizar el modelo `orca-mini-3b.ggmlv3.q4_0.bin` es importante, se recomienda no utilizarlo, ya que es muy lento comparado con el tiempo de respuesta de [ChatGPT](https://chat.openai.com/), que en general es menor a un segundo.
  * Se recomienda ejecutar el experimento en una configuración de hardware y software con RAM de 16 GB o superior, para verificar si el tiempo de ejecución disminuye con respecto a los resultados registrados en este documento.
  * Debido a un problema de los modelos LLM, en general, llamado [_alucinación_](https://arxiv.org/abs/2202.03629), se recomienda
  no tomar como verdaderas las respuestas obtenidas mediante este tipo de modelos sin comprobar adecuadamente la veracidad de las mismas.


### Experimento: chat-with-orca

* **Objetivo**: Ejecutar una sesión chat de prueba
utilizando el modelo GPT4All `orca-mini-3b.ggmlv3.q4_0.bin`

* **Comando ejecutado**: [05-ejecutar-chat-with-orca.bat](05-ejecutar-chat-with-orca.bat)

* **Resultados obtenidos**:

| Operación       | Entrada | Salida |  Tiempo de respuesta en segundos |
|-------------------|---------|--------|----------------------:|
| Cargar modelo  | nombre del modelo: `orca-mini-3b.ggmlv3.q4_0.bin` | (modelo cargado en la RAM) | [*] `62,15`
| 1er intercambio de mensajes    | texto: `hello` | texto: `Hello! How may I assist you today?` | `443,43` |
| 2do intercambio de mensajes    | texto: `write me a short poem` | texto:  `Sure, here's a short poem for you:` <br> `Beneath the autumn sky so blue,` <br> `The leaves fall down like rain.` <br> `A rustling carpet of gold and red,` <br> `As nature's beauty takes its fill.` <br> `The air is crisp and cool and clean,` <br> `And the world around us grows serene.` | `902,06` |
| 3er intercambio de mensajes    | texto: `thank you` | texto: `You're welcome! Is there anything else I can help you with?` | `307,06` |

[*] Nota: El modelo ya había sido descargado antes de registrar los resultados de este experimento.

* **Conclusión**
  * Con la configuración de hardware y software utilizada, si el tiempo de respuesta al utilizar el modelo `orca-mini-3b.ggmlv3.q4_0.bin` es importante, se recomienda no utilizarlo, ya que es muy lento comparado con el tiempo de respuesta de [ChatGPT](https://chat.openai.com/), que en general es menor a un segundo.
  * Se recomienda ejecutar el experimento en una configuración de hardware y software con RAM de 16 GB o superior, para verificar si el tiempo de ejecución disminuye con respecto a los resultados registrados en este documento.


### Experimento: chat-with-falcon

* **Objetivo**: Ejecutar una sesión chat de prueba
utilizando el modelo GPT4All `ggml-model-gpt4all-falcon-q4_0.bin`

* **Comando ejecutado**: [06-ejecutar-chat-with-falcon.bat](06-ejecutar-chat-with-falcon.bat)

* **Resultados obtenidos**:

| Operación       | Entrada | Salida |  Tiempo de respuesta en segundos |
|-------------------|---------|--------|----------------------:|
| Cargar modelo  | nombre del modelo: `ggml-model-gpt4all-falcon-q4_0.bin` | (modelo cargado en la RAM) | [*] `124,36`
| 1er intercambio de mensajes    | texto: `hello` | texto: `Hello! How can I help you today?` | `296.23` |
| 2do intercambio de mensajes    | texto: `write me a short poem` | texto:  `Here's a short poem for you:` <br> ` ` <br> `Raindrops on roses` <br>  ` ` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br>  `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raindrops on roses` <br> `Raind` | `3185,37` |
| 3er intercambio de mensajes    | texto: `thank you` | texto: `You're welcome! Is there anything else I can help you with?` | `192,36` |

[*] Nota: El modelo ya estaba descargado en el [directorio caché de modelos](#directorio-caché-de-modelos) antes de ejecutar y registrar los datos de este experimento, como consecuencia de una ejecución anterior.

* **Conclusión**
  * Con la configuración de hardware y software utilizada, si el tiempo de respuesta al utilizar el modelo `ggml-model-gpt4all-falcon-q4_0.bin` es importante, se recomienda no utilizarlo, ya que es muy lento comparado con el tiempo de respuesta de [ChatGPT](https://chat.openai.com/), que en general es menor a un segundo.
  * Se recomienda ejecutar el experimento en una configuración de hardware y software con RAM de 16 GB o superior, para verificar si el tiempo de ejecución disminuye con respecto a los resultados registrados en este documento.

## Conclusión
* El menor tiempo de respuesta registrado fue de `43,66` segundos, utilizando el modelo `orca-mini-3b.ggmlv3.q4_0.bin` en el experimento de autocompletado de texto con un máximo 3 tokens.
* El mayor tiempo de respuesta registrado fue de `3185,37` segundos (`53` minutos), utilizando el modelo `ggml-model-gpt4all-falcon-q4_0.bin` en el experimento de chat de prueba al solicitarle al modelo escribir un poema corto.
* Debido a estos resultados, se recomienda experimentar con una configuración de hardware y software diferente, con al menos 16 GB de RAM, y utilizando otros [modelos GPT4All](https://raw.githubusercontent.com/nomic-ai/gpt4all/main/gpt4all-chat/metadata/models.json) para obtener mayor información sobre el rendimiento de dichos modelos.