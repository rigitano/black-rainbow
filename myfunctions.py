import pyperclip

def bunda(a, b, c):
    """This function concatenates a, b and c and sends the result to the clipboard."""

    
    concatenated = a + b + c


    # Copy text to the clipboard
    pyperclip.copy(concatenated)

    # Retrieve text from the clipboard
    sent = pyperclip.paste()


    return sent + " sent to clipboard"


def clipboard_hello_world():
    """This function sends 'echo 'Hello World !'' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("echo 'Hello World !'")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_os_info():
    """This function sends 'uname -a' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("uname -a")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_cpu_info():
    """This function sends 'lscpu' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("lscpu")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_avalable_ram():
    """This function sends 'free -h' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("free -h")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_filesystems_and_disk_space():
    """This function sends 'df -h' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("df -h")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_folders_and_disk_space():
    """This function sends 'du -hd1 .' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("du -hd1 .")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_ip_and_mac():
    """This function sends 'echo -------Who am I on the network?------- && ip a && echo -------How do I reach other machines/networks?------- && ip route' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("echo -------Who am I on the network?------- && ip a && echo -------How do I reach other machines/networks?------- && ip route")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_make_executable(s_etapa):
    """
    The value of s_etapa was chosen in a dropdown menu in the frontend
    This function sends to the clipboard. one of the following commands, depending on the value of s_etapa: 
       '#!/bin/bash'
       '#!/bin/env python' this make sure the script will run with the python interpreter FROM THE ACTIVE ENVIRONMENT
       'chmod +x nomeDoArquivo' 
       'export PATH='/bla/bla/nomeDaPasta:$PATH'
    """
    
    # Copy text to the clipboard, depending on the value of s_etapa
    if s_etapa == "shebang - interpreter will be bash":
        pyperclip.copy("#!/bin/bash")

    elif s_etapa == "shebang - interpreter will be python":
        pyperclip.copy("#!/bin/env python")

    elif s_etapa == "chmod - make executable":
        pyperclip.copy("chmod +x nomeDoArquivo")

    elif s_etapa == "export - add folder to PATH to call it directly":

        pyperclip.copy("export PATH='/caminho/caminho/nomeDaPasta:$PATH'")

    else:
        raise ValueError("Invalid value for s_etapa")


    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_xxxxx():
    """This function sends 'xxxxxxx' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("xxxxxxx")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"
