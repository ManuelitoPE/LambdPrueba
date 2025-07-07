import json

def lambda_handler(event, context):
    """
    Función Lambda simple que devuelve un mensaje "Hola Mundo".

    Parameters:
    ----------
    event: dict, required
        El evento de entrada a la función Lambda.
        Para un "Hola Mundo" básico, no se usa, pero es un parámetro obligatorio.

    context: object, required
        El objeto de contexto en tiempo de ejecución.
        También es un parámetro obligatorio y contiene información sobre la invocación,
        la función, y el ambiente de ejecución.

    Returns:
    ------
    dict
        Un diccionario que se serializa como JSON y se devuelve como respuesta.
    """
    print("¡Función Lambda invocadaaaaa!") # Opcional: para ver en CloudWatch Logs

    # El cuerpo de la respuesta debe ser una cadena JSON válida si se invoca vía API Gateway
    return {
        'statusCode': 200,
        'body': json.dumps('Hola Mundo desde Lambda!')
    }
