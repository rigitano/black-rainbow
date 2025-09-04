import pyperclip
import os
from pathlib import Path
import platform


if platform.system() == "Windows":
    pass
else:
    pyperclip.set_clipboard("xclip") #please notice that in linux, xclip must be installed


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
    pyperclip.copy("du -hd1 . | sort -hr")


    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_ip():
    """This function sends 'echo -------Who am I on the network?------- && ip a && echo -------How do I reach other machines/networks?------- && ip route' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(r"""echo "";PUB="$((curl -4 -fsS icanhazip.com || curl -4 -fsS ifconfig.co || curl -4 -fsS api.ipify.org) | grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' | head -n1)"; [ -z "$PUB" ] && PUB="(unknown)"; printf "Public IP        : %s\n" "$PUB"; ip -o -4 addr show up scope global | while read -r _ IF _ IPCIDR _; do IP="${IPCIDR%/*}"; PFX="${IPCIDR#*/}"; NM="$(awk -v p="$PFX" 'BEGIN{split("0 128 192 224 240 248 252 254 255",A," ");k1=p;k1=(k1>8?8:(k1<0?0:k1));k2=p-8;k2=(k2>8?8:(k2<0?0:k2));k3=p-16;k3=(k3>8?8:(k3<0?0:k3));k4=p-24;k4=(k4>8?8:(k4<0?0:k4));print A[k1]"."A[k2]"."A[k3]"."A[k4]}')"; GW="$(ip -4 route get 1.1.1.1 from "$IP" 2>/dev/null | awk '/via/ {for(i=1;i<=NF;i++) if($i=="via"){print $(i+1); exit}}')"; [ -z "$GW" ] && GW="$(ip -4 route show default dev "$IF" 2>/dev/null | awk '/^default/ {print $3; exit}')" ; [ -z "$GW" ] && GW="(none)"; printf "Local IP (%s): %s  mask %s (/%s)  gateway %s\n" "$IF" "$IP" "$NM" "$PFX" "$GW"; done""")
    
    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_ips_to_ssh():
    """This function sends 'echo -------Who am I on the network?------- && ip a && echo -------How do I reach other machines/networks?------- && ip route' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(r"""echo "";while read -r ipcidr; do ip=${ipcidr%/*}; pfx=${ipcidr#*/}; IFS=. read -r a b c d <<<"$ip"; ipi=$(( (a<<24)+(b<<16)+(c<<8)+d )); mask=$(( pfx==0 ? 0 : (0xFFFFFFFF << (32-pfx)) & 0xFFFFFFFF )); net=$(( ipi & mask )); bcast=$(( net | (~mask & 0xFFFFFFFF) )); for ((n=net+1; n<bcast; n++)); do A=$(( (n>>24)&255 )); B=$(( (n>>16)&255 )); C=$(( (n>>8)&255 )); D=$(( n&255 )); tgt="$A.$B.$C.$D"; (echo >/dev/tcp/$tgt/22) >/dev/null 2>&1 && { hn=$(getent hosts "$tgt" | awk '{print $2}' | head -n1); printf "%-15s\t%s\n" "$tgt" "${hn:--}"; }; done; done < <(ip -o -4 addr show scope global | awk '{print $4}')""")
    
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
    """This function sends 'git push origin main' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("git push origin main")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_go_back(s_commit_hash,s_option):
    """This function goes back to a commit, it will erase the ones after it or not depending on the value of s_option."""
    
    # Copy text to the clipboard, depending on the value of s_option
    if s_option == "reset --hard (DANGER: all posterior changes and commits will be deleted!)":
        pyperclip.copy(f"git reset --hard '{s_commit_hash}'")

    elif s_option == "revert (posterior commits will be kept, a new commit will be created with the same code as the chosen commit)":
        pyperclip.copy(f"git revert '{s_commit_hash}'..HEAD")

    else:
        raise ValueError("Invalid value for s_option")


    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_stash(s_message):
    """This function sends git stash push -m 'xxxxxx' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"git stash push -m '{s_message}'")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_see_all_branches():
    """This function sends 'git branch' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("git branch")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_change_branch(s_branch_name):
    """This function sends 'git branch xxxx' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"git branch {s_branch_name}")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_merge(s_source_branch_with_extra_code,s_destination_branch):
    """This function sends 'git checkout xxx && git merge xxx --no-ff' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"git checkout {s_destination_branch} && git merge {s_source_branch_with_extra_code} --no-ff")

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
        pyperclip.copy(f"find . -type f -regextype posix-extended -regex \".*{s_search_for_this}.*\"")

    elif s_by_what == "in the file content":
        pyperclip.copy(f"find . -type f -print | xargs egrep \"{s_search_for_this}\"")

    else:
        raise ValueError("Invalid value for s_by_what")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_extraction(s_choice,s_file_name):
    """This function sends a command to the clipboard depending on s_file_name."""
    
    # Copy text to the clipboard, depending on the value of s_choice
    if s_choice == ".tar":
        pyperclip.copy(f"tar -xvf {s_file_name}")

    elif s_choice == ".tar.gz":
        pyperclip.copy(f"tar -xzvf {s_file_name}")

    elif s_choice == ".tar.bz2":
        pyperclip.copy(f"tar -xjvf {s_file_name}")

    elif s_choice == ".tar.xz":
        pyperclip.copy(f"tar -xJvf {s_file_name}")

    elif s_choice == ".gz":
        pyperclip.copy(f"gunzip {s_file_name}")

    elif s_choice == ".bz2":
        pyperclip.copy(f"bunzip2 {s_file_name}")

    elif s_choice == ".xz":
        pyperclip.copy(f"unxz {s_file_name}")


    else:
        raise ValueError("Invalid value for s_choice")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"





def clipboard_execute(s_choice):
    """This function sends a coomand to the clipboard depending on the choice on the dropbox."""

    # Copy text to the clipboard, depending on the value of s_choice
    if s_choice == "bash (./)":
        pyperclip.copy(f"./")

    elif s_choice == "nextflow (nextflow run)":
        pyperclip.copy(f"nextflow run ")

    elif s_choice == "docker (docker run -d)":
        pyperclip.copy(f"docker run -d ")

    elif s_choice == "slurm (sbatch)":
        pyperclip.copy(f"sbatch ")

    elif s_choice == "torque (qsub)":
        pyperclip.copy(f"qsub ")

    elif s_choice == "moab on top of torque (msub)":
        pyperclip.copy(f"msub ")

    elif s_choice == "kubernetes (kubectl apply -f)":
        pyperclip.copy(f"kubectl apply -f ") 

    elif s_choice == "yarn-hadoop (yarn jar)":
        pyperclip.copy(f"yarn jar ") 

    elif s_choice == "spark on top of yarn-hadoop (spark-submit --master yarn)":
        pyperclip.copy(f"spark-submit --master yarn ") 


    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_see_running_processes(s_choice):
    """This function sends a coomand to the clipboard depending on the choice on the dropbox."""
    


    # Copy text to the clipboard, depending on the value of s_choice
    if s_choice == "bash (top)":
        pyperclip.copy(f"top")

    elif s_choice == "nextflow (nextflow log)":
        pyperclip.copy(f"nextflow log")

    elif s_choice == "docker (docker ps)":
        pyperclip.copy(f"docker ps")

    elif s_choice == "slurm (squeue)":
        pyperclip.copy(f"squeue")

    elif s_choice == "torque (qstat)":
        pyperclip.copy(f"qstat")

    elif s_choice == "moab on top of torque (showq)":
        pyperclip.copy(f"showq")

    elif s_choice == "kubernetes (kubectl get pods)":
        pyperclip.copy(f"kubectl get pods") 

    elif s_choice == "yarn-hadoop (yarn application -list)":
        pyperclip.copy(f"yarn application -list") 

    elif s_choice == "spark on top of yarn-hadoop (use UI!)":
        pyperclip.copy(f"use UI!") 


    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_cancel_execution(s_choice):
    """This function sends a coomand to the clipboard depending on the choice on the dropbox."""
    


    # Copy text to the clipboard, depending on the value of s_choice
    if s_choice == "bash (kill)":
        pyperclip.copy(f"kill ")

    elif s_choice == "nextflow (nextflow kill)":
        pyperclip.copy(f"nextflow kill ")

    elif s_choice == "docker (docker stop)":
        pyperclip.copy(f"docker stop ")

    elif s_choice == "slurm (scancel)":
        pyperclip.copy(f"scancel ")

    elif s_choice == "torque (qdel)":
        pyperclip.copy(f"qdel ")

    elif s_choice == "moab on top of torque (mjobctl -c)":
        pyperclip.copy(f"mjobctl -c ")

    elif s_choice == "kubernetes (kubectl delet pod)":
        pyperclip.copy(f"kubectl delet pod ") 

    elif s_choice == "yarn-hadoop (yarn application -kill)":
        pyperclip.copy(f"yarn application -kill ") 

    elif s_choice == "spark on top of yarn-hadoop (yarn application -kill)":
        pyperclip.copy(f"yarn application -kill ") 


    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_find(s_word_to_find,s_file_to_be_searched):
    """This function sends 'grep -n 'henrique' file.txt' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"grep -n '{s_word_to_find}' {s_file_to_be_searched}")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_replace(s_old_value,s_new_value,s_file_with_text,s_new_file_name):
    """This function sends 'sed 's/old_value/new_value/g' file.txt > newfile.txt' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"sed 's/{s_old_value}/{s_new_value}/g' {s_file_with_text} > {s_new_file_name}")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_find_vim(s_word_to_find):
    """This function sends a text to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"/{s_word_to_find}")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_replace_vim(s_old_value,s_new_value):
    """This function sends a text  to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"%s/{s_old_value}/{s_new_value}/gc")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"




def clipboard_fiter_table_bash(s_value_to_be_filtered, s_file_name,s_column):
    """This function sends 'awk '$2=="value"' file.csv' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"awk '${s_column} == \"{s_value_to_be_filtered}\"' {s_file_name}")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_sort_table_bash(s_file_name,s_column):
    """This function sends 'sort -k2 file.csv' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"sort -k{s_column} {s_file_name}")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"





def clipboard_unique_lines_bash(s_file_name):
    """This function sends 'sort data.txt | uniq' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"sort {s_file_name} | uniq")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_pdb2molecule_in_solvent(s_pdbfile, s_outSytemName, s_solvent, s_forceField, s_boxSize):
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.pdb2molecule_in_solvent({s_pdbfile}, {s_outSytemName}, {s_solvent}, {s_forceField}, {s_boxSize})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_pdb2box_full_of_that(s_pdbfile, s_forceField, s_box_size, n_mol):
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.pdb2box_full_of_that({s_pdbfile}, {s_forceField}, {s_box_size}, {n_mol})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_pdb2gmx():
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"gmx pdb2gmx -f .pdb -o .gro -p .top -missing -ter -ignh -water none -ff ../charmm36-jul2022")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_editconf():
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f'gmx editconf -f .gro -o .gro -c -box "3 3 3" -bt cubic')

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_solvate():
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"gmx solvate -cp .gro -cs spc216.gro -maxsol 123 -p .top -o .gro")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_grompp():
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"gmx grompp -f .mdp -c .gro -r .gro -p .top -o .tpr -maxwarn 1")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_mdrun():
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"gmx mdrun -v -deffnm ")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_center():
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"gmx trjconv -s .tpr -f .xtc -o .centered.xtc -center -pbc mol")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_fit():
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"gmx trjconv -s .tpr -f .centered.xtc -o .fitted.xtc -fit progressive")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_energy():
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"gmx energy -f .edr -o .xvg")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"






def clipboard_make_realistic(s_machine, s_gro, s_top, s_groups,n_temperature):
    """This function sends codes to the clipboard, depending on the choice made on a droplist."""
    
    # Copy text to the clipboard, depending on the value of s_by_what
    if s_machine == "local":
        pyperclip.copy(f"./runTRAJ-local.sh 123 {s_gro} {s_top} 1 {s_groups} {n_temperature}")

    elif s_machine == "slurm":
        pyperclip.copy(f"xxxxx")

    elif s_machine == "rome (moab wrapper with time limit)":
        pyperclip.copy(f"xxxxx")

    else:
        raise ValueError("Invalid value for s_machine")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_run_bench(s_machine, s_tpr):
    """This function sends codes to the clipboard, depending on the choice made on a droplist."""
    
    # Copy text to the clipboard, depending on the value of s_by_what
    if s_machine == "local":
        pyperclip.copy(f"./runBENCHMARK-local {s_tpr}")

    elif s_machine == "slurm":
        pyperclip.copy(f"xxxxx")

    elif s_machine == "rome (moab wrapper with time limit)":
        pyperclip.copy(f"./runBENCHMARK-rome {s_tpr}")

    else:
        raise ValueError("Invalid value for s_machine")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_run_traj(s_procedure_option, s_machine_option, s_gro, s_top, s_time, s_groups, n_temperature):
    """This function sends codes to the clipboard, depending on the choice made on a droplist."""
    
    # Copy text to the clipboard, depending on the value of s_by_what
    if s_machine_option == "local":
        if s_procedure_option == "from scratch (MAKEREALISTIC and PROD)":
            pyperclip.copy(f"./runTRAJ-local.sh 1234 {s_gro} {s_top} {s_time} {s_groups} {n_temperature}")
        elif s_procedure_option == "from realistic (just PROD)":
            pyperclip.copy(f"./runTRAJ-local.sh 4 {s_gro} {s_top} {s_time} {s_groups} {n_temperature}")
        else:
            raise ValueError("Invalid value for s_procedure_option")
        
    elif s_machine_option == "slurm":
        if s_procedure_option == "from scratch (MAKEREALISTIC and PROD)":
            pyperclip.copy(f"./xxxxxxxx.sh 1234 {s_gro} {s_top} {s_time} {s_groups} {n_temperature}")
        elif s_procedure_option == "from realistic (just PROD)":
            pyperclip.copy(f"./xxxxxxxx.sh 4 {s_gro} {s_top} {s_time} {s_groups} {n_temperature}")
        else:
            raise ValueError("Invalid value for s_procedure_option")

    elif s_machine_option == "rome (moab wrapper with time limit)":
        if s_procedure_option == "from scratch (MAKEREALISTIC and PROD)":
            pyperclip.copy(f"./xxxxxxxx.sh 1234 {s_gro} {s_top} {s_time} {s_groups} {n_temperature}")
        elif s_procedure_option == "from realistic (just PROD)":
            pyperclip.copy(f"./xxxxxxxx.sh 4 {s_gro} {s_top} {s_time} {s_groups} {n_temperature}")
        else:
            raise ValueError("Invalid value for s_procedure_option")

    else:
        raise ValueError("Invalid value for s_machine")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_livestream():
    """This function sends a text to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"ssh rome 'tail -c +0 -f vis.xtc' | vmd -e visualize.vmd")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_download_and_clean_pdb(s_molecule_name):
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.download_and_clean_pdb({s_molecule_name})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_create_peptide(s_aminoacids, l_phi, l_psi_im1, s_nTerminusCAP, s_cTerminusCAP, s_outName ):
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.create_peptide({s_outName}, {s_aminoacids}, {l_phi}, {l_psi_im1}, {s_nTerminusCAP}, {s_cTerminusCAP} )")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_insert_new_molecule_into_pdb(input_pdb, new_molecule_atoms, output_pdb):
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.insert_new_molecule_into_pdb({input_pdb}, {output_pdb}, {new_molecule_atoms})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_insert_residue_into_chain(s_input_pdb_file,s_chain,n_residue,s_new_residue_name, d_new_residue_atoms,s_replace_or_displace,s_output_pdb_file):
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.insert_residue_into_chain({s_input_pdb_file},{s_output_pdb_file},{s_chain},{n_residue},{s_new_residue_name}, {d_new_residue_atoms},{s_replace_or_displace})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_insert_atom_into_residue(s_input_pdb_file,s_chain,n_residue,s_atom_structural_name,s_atom_element_name,l_coord,s_output_pdb_file):
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.insert_atom_into_residue({s_input_pdb_file}, {s_output_pdb_file}, {s_chain}, {n_residue}, {s_atom_structural_name}, {s_atom_element_name}, {l_coord})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_add_truss(s_pdb_file, p1, p2, n_square_size, s_out_pdb_file):
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.add_truss({s_pdb_file}, {s_out_pdb_file}, {p1}, {p2}, {n_square_size})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"





def clipboard_freeze_dihedrals(s_potential_option, s_gro_file,s_top_file, restraining_force, s_molename, s_file_to_be_edited, s_out_file_name, s_which_dihedrals_option):
    """This function sends a cleanpipe function with arguments to the clipboard
    
    
    """
    
    # Copy text to the clipboard, depending on the value of s_potential_option and s_which_dihedrals_option
    if s_potential_option == "[ dihedrals ] type 2 (improper dihedral harmonic)" and s_which_dihedrals_option == "all":
        pyperclip.copy(f"xxxx")

    elif s_potential_option == "[ dihedrals ] type 2 (improper dihedral harmonic)" and s_which_dihedrals_option == "just phi and psi of protein":
        pyperclip.copy(f"cl.freeze_phi_psi_dihedrals({s_gro_file}, {s_top_file}, {restraining_force}, {s_molename}, {s_file_to_be_edited}, {s_out_file_name})")

    elif s_potential_option == "[ dihedrals ] type 4 (improper dihedral periodic)" and s_which_dihedrals_option == "all":
        pyperclip.copy(f"xxxx")

    elif s_potential_option == "[ dihedrals ] type 4 (improper dihedral periodic)" and s_which_dihedrals_option == "just phi and psi of protein":
        pyperclip.copy(f"xxxx")

    elif s_potential_option == "[ dihedral_restraints ] type 1 (a potential similar to improper dihedral)" and s_which_dihedrals_option == "all":
        pyperclip.copy(f"xxxx")

    elif s_potential_option == "[ dihedral_restraints ] type 1 (a potential similar to improper dihedral)" and s_which_dihedrals_option == "just phi and psi of protein":
        pyperclip.copy(f"xxxx")

    else:
        raise ValueError("Invalid values of s_potential_option or s_which_dihedrals_option")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_get_atom_global_id(s_top_file, s_molecule_name, n_molecule_instantiation, n_residue, s_atom):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"id_atom = cl.get_atom_global_id({s_top_file}, {s_molecule_name}, {n_molecule_instantiation}, {n_residue}, {s_atom})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"




def clipboard_basic_infos_of_molecules(s_top):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"dd_mols_basic_infos = cl.basic_infos_of_molecules({s_top})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_getMoleculeName(s_top, n_order):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"s_mol_name = cl.getMoleculeName({s_top}, order={n_order})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_getSystemName(s_top):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"s_system_name = cl.getSystemName({s_top})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"




def clipboard_parse_directive(s_top, s_directive_name):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"ll_parsed_directive = cl.parse_directive({s_top}, {s_directive_name})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_parse_directives_inside_each_and_every_molecule(s_top):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"dd_mols = cl.parse_directives_inside_each_and_every_molecule({s_top})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_parse_directives_inside_intermolecular_interactions(s_top):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"dd_intermol = cl.parse_directives_inside_intermolecular_interactions({s_top})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_insert_text_before_directive(s_file_path, s_text_to_insert, s_directive):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.insert_text_before_directive({s_file_path}, {s_text_to_insert}, {s_directive})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_replace_all_lines_of_directive(s_top_file, s_directive, ll_lines_to_add,directive_position, s_top_file_out):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.replace_all_lines_of_directive({s_top_file}, {s_top_file_out}, {s_directive}, {ll_lines_to_add}, {directive_position})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_add_lines_at_the_end_of_directive(s_top_file, s_directive, ll_lines_to_add, directive_position, s_top_file_out):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.add_lines_at_the_end_of_directive({s_top_file}, {s_top_file_out}, {s_directive}, {ll_lines_to_add}, {directive_position})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_put_lines_at_the_proper_place_of_directive(s_file_to_be_edited, s_directive, ll_replacement, s_out_file_name):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.put_lines_at_the_proper_place_of_directive({s_file_to_be_edited}, {s_out_file_name}, {s_directive}, {ll_replacement})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_replaceMoleculeName(top_filename, old_molecule_name, new_molecule_name):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.replaceMoleculeName({top_filename}, {old_molecule_name}, {new_molecule_name})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_update_molecule_quantity(top_file, molecule_name, new_quantity):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.update_molecule_quantity({top_file}, {molecule_name}, {new_quantity})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_setSystemName(top_filename, new_system_name):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.setSystemName({top_filename}, {new_system_name})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_replaceWordInsideDirective(top_filename, target_directive, old_word, new_word):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.replaceWordInsideDirective({top_filename}, {target_directive}, {old_word}, {new_word})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"







def clipboard_include_all_itps(s_top, s_option):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard, depending on option
    if s_option == "option 1: text output":
        pyperclip.copy(f"s_expanded_includes = cl.expand_includes({s_top})")
    elif s_option == "option 2: temp file output":
        pyperclip.copy(f"s_temp_file_name = cl.expand_includes_to_temp_file({s_top})")
    else:
        raise ValueError("Invalid value for s_option")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"




def clipboard_deconstruct_top_into_molecules(s_top):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"d_created_itps = cl.deconstruct_top_into_molecules({s_top})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def call_open_vmd_with_socket():
    """This function calls a function in cleanpipe directly"""
    import cleanpipe as cl

    # call function
    cl.open_vmd_with_socket()


    return "cl.open_vmd_with_socket() was called directly"












def send_tcl_to_VMD_default_cartoon_and_licorice():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "default_cartoon_and_licorice.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'


def send_tcl_to_VMD_goodsell_blob():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "goodsell_blob.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'

def send_tcl_to_VMD_chewing_gum():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "chewing_gum.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'

def send_tcl_to_VMD_secondary_structure():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "secondary_structure.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'


def send_tcl_to_VMD_eletrostatic_surface_using_just_aminoacid_info():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "eletrostatic_surface_using_just_aminoacid_info.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'


def send_tcl_to_VMD_fobic_are_yellow_and_philic_are_purple():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "fobic_are_yellow_and_philic_are_purple.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'


def send_tcl_to_VMD_hbond_between_proteins_and_solvent():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "hbond_between_proteins_and_solvent.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'



def call_see_interactions(s_top, s_gro, s_mol_name):
    """This function calls a function in cleanpipe directly"""

    import cleanpipe as cl
    
    # call function
    cl.see_interactions(s_top, s_gro, s_mol_name)

    return f"cl.see_interactions({s_top}, {s_gro}, {s_mol_name}) was called directly"


#trr forces



def send_tcl_to_VMD_MARTINI_jackson():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "MARTINI_jackson.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'



def send_tcl_to_VMD_MARTINI_henrique():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "MARTINI_henrique.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'

def send_tcl_to_VMD_MARTINI_brasnett():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "MARTINI_brasnett.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'


def send_tcl_to_VMD_MARTINI_bylipidtype():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "MARTINI_bylipidtype.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'

def send_tcl_to_VMD_MARTINI_technical():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "MARTINI_technical.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'



def send_tcl_to_VMD_MARTINI_cg_bonds():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "cg_bonds-v6.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    #############################################################################
    # after sourcing, Ill send some commands that are particular to that script #
    #############################################################################

    cl.send_command_to_vmd(r"pwd")

    cl.send_command_to_vmd(r"cd /data1/henrique/martinitutorial/bilayer-lipidome-tutorial-II/worked/complex-bilayers")


    # cg_bonds -top ./dspc.top -topoltype "elastic"
    cl.send_command_to_vmd(r"cg_bonds -top ./topol.top -topoltype \"elastic\"")

    # cg_bonds -gmx /home/hrigitano/miniconda3/envs/bio/bin.AVX2_256/gmx -tpr ./dspc-md.tpr -net "elastic" -cutoff 12.0 -color "orange" -mat "AOChalky" -res 12 -rad 0.1 -topoltype "elastic"
    cl.send_command_to_vmd(r"cg_bonds -tpr /data1/henrique/martinitutorial/bilayer-lipidome-tutorial-I/minimal/spontaneous-assembly/phase_sep.tpr -gmx /home/hrigitano/miniconda3/envs/bio/bin.AVX2_256/gmx")

    # these are not normal representations. to delete them, use:
    # cg_delete_all_graphics

    return f'a couple of commands were sent to VMD'



def send_tcl_to_VMD_MARTINI_cg_bonds_delete():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    

    final_command = f'cg_delete_all_graphics'
    cl.send_command_to_vmd(final_command)



    return f'a couple of commands were sent to VMD'



def send_tcl_to_VMD_selection_highlight():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "selection_highlight.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'



def send_tcl_to_VMD_inspect_file():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "inspect_file.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'



