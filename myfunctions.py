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


def clipboard_see_content_of_path_variable():
    """This function sends 'echo "$PATH" | tr ':' '\n'' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("echo \"$PATH\" | tr ':' '\\n'")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



# xxx execute, monitor execution, kill execution




def clipboard_python_location():
    """This function sends 'which python' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("which python")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_modules_location():
    """This function sends to the clipboard a huge coomand to see modules are instaled to and imported from ."""
    
    # Copy text to the clipboard
    pyperclip.copy("python -c \"import sys,sysconfig; print('\\nINSTALL\\n\\n',sysconfig.get_paths()['purelib']); print('\\nIMPORT'); print('\\n'.join(sys.path))\"")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_see_all_conda_environments():
    """This function sends 'conda env list' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("conda env list")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_create_conda_environment(s_env_name,s_python_version):
    """This function sends 'conda create --name nomeDoAmbiente python=3.9' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"conda create --name {s_env_name} python={s_python_version}")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"







def clipboard_keygen(s_chosen_action,s_chosen_protocol):
    """This function sends a comand to the clipboard, depending on s_chosen_action and s_chosen_protocol.
    
    # Ed25519 (modern, shorter keys, more secure)
    cat ~/.ssh/id_ed25519.pub
    ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519

    # OR, RSA 4096-bit (older systems / some services still require RSA)
    cat ~/.ssh/id_rsa.pub
    ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa
    
    
    """
    
    # Copy text to the clipboard, depending on the value of s_chosen_action and s_chosen_protocol
    if s_chosen_action == "see":

        if s_chosen_protocol == "Ed25519 (modern)":
            pyperclip.copy(f"cat ~/.ssh/id_ed25519.pub")

        elif s_chosen_protocol == "RSA (older systems)":
            pyperclip.copy(f"cat ~/.ssh/id_rsa.pub")
        else:
            raise ValueError("Invalid value for s_chosen_protocol")

    elif s_chosen_action == "generate":

        if s_chosen_protocol == "Ed25519 (modern)":
            pyperclip.copy(f"ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519")

        elif s_chosen_protocol == "RSA (older systems)":
            pyperclip.copy(f"ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa")

        else:
            raise ValueError("Invalid value for s_chosen_protocol")

    else:
        raise ValueError("Invalid value for s_chosen_action")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_init_or_clone(s_chosen_action,s_repo_link):
    """This function sends a big commant to the clipboard. depending on the value of s_chosen_action."""
    



    # Copy text to the clipboard, depending on the value of s_chosen_action and s_chosen_action
    if s_chosen_action == "init (project started localy)":
        pyperclip.copy("git init --initial-branch=main && git remote add origin git@github.com:rigitano/$(basename \"$PWD\").git && git push -u origin main")

    elif s_chosen_action == "clone (project started at github)":
        pyperclip.copy(f"git clone {s_repo_link}")

    else:
        raise ValueError("Invalid value for s_chosen_action")




    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_pull():
    """This function sends 'git pull origin main' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("git pull origin main")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_add_commit(s_message):
    """This function sends git add . && git commit -m 'xxx' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"git add . && git commit -m '{s_message}'")


    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_add_commit_new_branch(s_new_branch_name,s_message):
    """This function sends git checkout -b 'xxx' && git add . && git commit -m 'xxx' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"git checkout -b '{s_new_branch_name}' && git add . && git commit -m '{s_message}'")


    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_push():
    """This function sends 'xxxxxxx' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("xxxxxxx")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_reset():
    """This function sends 'xxxxxxx' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("xxxxxxx")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_stash():
    """This function sends 'xxxxxxx' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("xxxxxxx")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_see_all_branches():
    """This function sends 'xxxxxxx' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("xxxxxxx")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_change_branch():
    """This function sends 'xxxxxxx' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("xxxxxxx")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_merge():
    """This function sends 'xxxxxxx' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("xxxxxxx")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"






def clipboard_list_enhanced():
    """This function sends 'ls -alhF --time-style=long-iso --color=auto' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("ls -alhF --time-style=long-iso --color=auto")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_search_filesystem(s_by_what,s_search_for_this):
    """This function sends codes to the clipboard, depending on the choice made on a droplist."""
    
    # Copy text to the clipboard, depending on the value of s_by_what
    if s_by_what == "in the file name":
        pyperclip.copy(rf"find . -type f -printf '%p\t%f\n' | awk -v pat='{s_search_for_this}' -F '\t' '$2 ~ pat {{print $1}}'")

    elif s_by_what == "entire path+name":
        pyperclip.copy(f"find . -type f -regextype posix-extended -regex \"{s_search_for_this}\"")

    elif s_by_what == "in the file content":
        pyperclip.copy(f"find . -type f -print | xargs egrep \"{s_search_for_this}\"")

    else:
        raise ValueError("Invalid value for s_by_what")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_compression(s_choice,s_file_name):
    """This function sends a command to the clipboard depending on s_file_name."""
    
    # Copy text to the clipboard, depending on the value of s_by_what
    if s_choice == ".tar.gz":
        pyperclip.copy(f"tar -xzvf {s_file_name}.tar.gz")

    elif s_choice == ".tar.bz2":
        pyperclip.copy(f"tar -xjvf {s_file_name}.tar.bz2")

    elif s_choice == ".tar.xz":
        pyperclip.copy(f"tar -xJvf {s_file_name}.tar.xz")

    elif s_choice == ".gz":
        pyperclip.copy(f"gunzip {s_file_name}.gz")

    elif s_choice == ".bz2":
        pyperclip.copy(f"bunzip2 {s_file_name}.bz2")

    elif s_choice == ".xz":
        pyperclip.copy(f"unxz {s_file_name}.xz")


    else:
        raise ValueError("Invalid value for s_choice")

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
