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



def clipboard_make_realistic(s_machine, s_gro, s_top, s_groups):
    """This function sends codes to the clipboard, depending on the choice made on a droplist."""
    
    # Copy text to the clipboard, depending on the value of s_by_what
    if s_machine == "local":
        pyperclip.copy(f"./runALL.sh cpr cpr cpr n {s_gro} {s_top} 0 \"{s_groups}\"")

    elif s_machine == "oxygen (torque)":
        pyperclip.copy(f"xxxxx")

    elif s_machine == "rome (moab on top of torque)":
        pyperclip.copy(f"xxxxx")

    else:
        raise ValueError("Invalid value for s_machine")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_run_prod(s_machine, s_gro, s_top, s_time, s_groups):
    """This function sends codes to the clipboard, depending on the choice made on a droplist."""
    
    # Copy text to the clipboard, depending on the value of s_by_what
    if s_machine == "local":
        pyperclip.copy(f"./runALL.sh n n n cpr {s_gro} {s_top} {s_time} \"{s_groups}\"")

    elif s_machine == "oxygen (torque)":
        pyperclip.copy(f"xxxxx")

    elif s_machine == "rome (moab on top of torque)":
        pyperclip.copy(f"xxxxx")

    else:
        raise ValueError("Invalid value for s_machine")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_freeze_dihedrals(s_potential_option, s_gro_file,s_top_file, restraining_force, s_molename, s_file_to_be_edited, s_out_file_name, s_which_dihedrals_option):
    """This function sends a cleanpipe function with arguments to the clipboard"""
    
    # Copy text to the clipboard, depending on the value of s_by_what
    if s_which_dihedrals_option == "all":
        pyperclip.copy(f"xxxx")

    elif s_which_dihedrals_option == "just phi and psi of protein":
        pyperclip.copy(f"cl.freeze_phi_psi_dihedrals(\"{s_gro_file}\", \"{s_top_file}\", {restraining_force}, \"{s_molename}\", \"{s_file_to_be_edited}\", \"{s_out_file_name}\")")

    else:
        raise ValueError("Invalid value for s_option")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_get_atom_global_id(s_top_file, s_molecule_name, n_molecule_instantiation, n_residue, s_atom):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"id_atom = cl.get_atom_global_id(\"{s_top_file}\", \"{s_molecule_name}\", {n_molecule_instantiation}, {n_residue}, \"{s_atom}\")")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"




def clipboard_basic_infos_of_molecules(s_top):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"dd_mols_basic_infos = cl.basic_infos_of_molecules(\"{s_top}\")")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_getMoleculeName(s_top, n_order):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"s_mol_name = cl.getMoleculeName(\"{s_top}\", order={n_order})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_getSystemName(s_top):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"s_system_name = cl.getSystemName(\"{s_top}\")")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"




def clipboard_parse_directive(s_top, s_directive_name):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"ll_parsed_directive = cl.parse_directive(\"{s_top}\", \"{s_directive_name}\")")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_parse_directives_inside_each_and_every_molecule(s_top):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"dd_mols = cl.parse_directives_inside_each_and_every_molecule(\"{s_top}\")")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_parse_directives_inside_intermolecular_interactions(s_top):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"dd_intermol = cl.parse_directives_inside_intermolecular_interactions(\"{s_top}\")")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_insert_text_before_directive(s_file_path, s_text_to_insert, s_directive):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.insert_text_before_directive(\"{s_file_path}\", \"{s_text_to_insert}\", \"{s_directive}\")")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_replace_all_lines_of_directive(s_top_file, s_top_file_out, s_directive, ll_lines_to_add):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.replace_all_lines_of_directive(\"{s_top_file}\", \"{s_top_file_out}\", \"{s_directive}\", {ll_lines_to_add}, directive_position='first')")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_add_lines_at_the_end_of_directive(s_top_file,s_top_file_out, s_directive, ll_lines_to_add):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.add_lines_at_the_end_of_directive(\"{s_top_file}\", \"{s_top_file_out}\", \"{s_directive}\", {ll_lines_to_add}, directive_position='first')")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_put_lines_at_the_proper_place_of_directive(s_file_to_be_edited, s_out_file_name, s_directive, ll_replacement):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.put_lines_at_the_proper_place_of_directive(\"{s_file_to_be_edited}\", \"{s_out_file_name}\", \"{s_directive}\", {ll_replacement})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_replaceMoleculeName(top_filename, old_molecule_name, new_molecule_name):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.replaceMoleculeName(\"{top_filename}\", \"{old_molecule_name}\", \"{new_molecule_name}\")")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_update_molecule_quantity(top_file, molecule_name, new_quantity):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.update_molecule_quantity(\"{top_file}\", \"{molecule_name}\", {new_quantity})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_setSystemName(top_filename, new_system_name):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.setSystemName(\"{top_filename}\", \"{new_system_name}\")")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_replaceWordInsideDirective(top_filename, target_directive, old_word, new_word):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.replaceWordInsideDirective(\"{top_filename}\", \"{target_directive}\", \"{old_word}\", \"{new_word}\")")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"







def clipboard_include_all_itps(s_top, s_option):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard, depending on option
    if s_option == "option 1: text output":
        pyperclip.copy(f"s_expanded_includes = cl.expand_includes(\"{s_top}\")")
    elif s_option == "option 2: temp file output":
        pyperclip.copy(f"s_temp_file_name = cl.expand_includes_to_temp_file(\"{s_top}\")")
    else:
        raise ValueError("Invalid value for s_option")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"




def clipboard_deconstruct_top_into_molecules(s_top):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"d_created_itps = cl.deconstruct_top_into_molecules(\"{s_top}\")")

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