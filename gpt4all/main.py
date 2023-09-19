#
# Fuente: https://docs.gpt4all.io/index.html
#

import sys
import timeit

from gpt4all import GPT4All


def execute_timed(function: function, start_message: str, print_function_ouput:bool=False):
    '''
    Ejecuta una función cronometrando su tiempo ejecución en segundos.

    Parámtros:
    - `function`: la función a ejecutar
    - `start_message`: el mensaje a imprimir antes de ejecutar la función
    - `print_function_output`: si es True entonces imprime el valor devuelto por la función,
    caso contrario, no ejecuta dicha acción

    Devuelve:
    - el mismo valor devuelto al ejecutar la función `function`
    '''
    print("[ TIMER START ] {}".format(start_message))

    start = timeit.default_timer()
    output = function()
    stop = timeit.default_timer()

    if print_function_ouput:
        print(output)

    print("[  TIMER END  ] Execution time: {:.2f} seconds".format(stop - start))
    return output


def autocomplete_with_model(model, text, max_tokens=3):
    '''
    Autocompleta un texto utilizando un modelo GPT4All.

    Los modelos GPT4All que se pueden utilizar con esta función
    se encuentran en los campos `filename` 
    del siguiente documento JSON: 
    https://raw.githubusercontent.com/nomic-ai/gpt4all/main/gpt4all-chat/metadata/models.json

    Parámetros:
    - `model`: el nombre del modelo a utilizar
    - `text`: el texto a autocompletar
    - `max_tokens`: la cantidad máxima de tokens en el texto que se utilizará para autocompletar `text`
    
    Devuelve:
    - no devuelve valor alguno
    '''
    msg = "Loading model..."
    model = execute_timed(lambda: GPT4All(model), msg)
    msg = text
    execute_timed(lambda: model.generate(text, max_tokens), msg, True)


def chat_with_model(model):
    '''
    Ejecuta un ejemplo de chat utilizando un modelo GPT4All dado.

    Los modelos GPT4All que se pueden utilizar con esta función
    se encuentran en los campos `filename` 
    del siguiente documento JSON: 
    https://raw.githubusercontent.com/nomic-ai/gpt4all/main/gpt4all-chat/metadata/models.json

    Parámetros:
    - `model`: el nombre del modelo a utilizar

    Devuelve:
    - no devuelve valor alguno
    '''
    msg = "Loading model..."
    model = execute_timed(lambda: GPT4All(model), msg)

    with model.chat_session():
        msg = "hello"
        execute_timed(lambda: model.generate(prompt=msg, temp=0), msg, True)

        msg = "write me a short poem"
        execute_timed(lambda: model.generate(prompt=msg, temp=0), msg, True)

        msg = "thank you"
        execute_timed(lambda: model.generate(prompt=msg, temp=0), msg, True)

        print()
        print("model.current_chat_session:")
        print(model.current_chat_session)


def autocomplete_with_orca():
    autocomplete_with_model(
        model = "orca-mini-3b.ggmlv3.q4_0.bin",
        text  = "The capital of France is "
    )

def autocomplete_with_falcon():
    autocomplete_with_model(
        model = "ggml-model-gpt4all-falcon-q4_0.bin",
        text  = "The first computer was invented by "
    )

def chat_with_orca():
    chat_with_model("orca-mini-3b.ggmlv3.q4_0.bin")

def chat_with_falcon():
    chat_with_model("ggml-model-gpt4all-falcon-q4_0.bin")

def print_help():
    print("Forma correcta de ejecutar:")
    print()
    print("  python main.py <opción>")
    print()
    print("Donde <opción> puede ser una de las siguientes:")
    print("  autocomplete-with-orca")
    print("  autocomplete-with-falcon")
    print("  chat-with-orca")
    print("  chat-with-falcon")
    print()
    print("Ejemplo de ejecución:")
    print()
    print("  python main.py autocomplete-with-orca")
    print()

def main(argv):
    if (len(argv) == 1):
        print_help()
        return

    match argv[1]:
        case "autocomplete-with-orca":
            autocomplete_with_orca()
        case "autocomplete-with-falcon":
            autocomplete_with_falcon()
        case "chat-with-orca":
            chat_with_orca()
        case "chat-with-falcon":
            chat_with_falcon()
        case _:
            print_help()

if __name__ == "__main__":
    main(sys.argv)
