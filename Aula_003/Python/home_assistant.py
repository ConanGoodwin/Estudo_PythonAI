# home_assistant.py


# set brightness and/or color_temperature of light
def set_light_state(brightness: int, color_temperature: str) -> dict:
    """
    Ajusta a luminosidade e a temperatura de cor das luzes.
    """
    # simula o ajuste de luzes
    return {"brightness": brightness, "color_temperature": color_temperature}


# intruder alert
def intruder_alert() -> dict:
    """
    Envia um alerta de intrusão.
    """
    # simula o envio de um alerta
    return {"alert": "Intruder alert activated"}


# start music
def start_music(energetic: bool, loud: bool, tempo: int) -> dict:
    """
    Inicia a reprodução de música com as características especificadas.
    """
    # simula o início da reprodução de música
    return {"energetic": energetic, "loud": loud, "tempo": tempo}


# good morning
def good_morning() -> dict:
    """
    Envia uma mensagem de bom dia.
    """
    # simula o envio de uma mensagem de bom dia
    return {"message": "Good morning!"}


__all__ = ["set_light_state", "intruder_alert", "start_music", "good_morning"]
