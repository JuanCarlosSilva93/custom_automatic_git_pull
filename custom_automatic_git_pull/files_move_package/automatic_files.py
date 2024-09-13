from updating_modules_package import custom_paths
import shutil
import datetime
import os


def moving_directories_files():
    """
        Realiza el movimiento y tratamiento de los módulos que hayan sido actualizados a la rutas establecidas para el
        cargue de los mismos en los ambientes de QA, dejando trazabilidad en un .txt de cada uno de ellos
    """

    repo_paths = custom_paths.repo_paths()
    target_paths = custom_paths.target_paths()

    for target in target_paths.values():
        if not os.path.exists(target):
            os.makedirs(target)

    for target in target_paths:
        with open(repo_paths.get(target) + '.cambios.cvs', 'r') as open_file:
            updated_modules = open_file.readlines()
        for module in updated_modules:
            comma_index = module.index(':')
            origin_path = os.path.join(repo_paths.get(target), module.replace('\n','')[0:comma_index])
            target_path = os.path.join(target_paths.get(target), module.replace('\n','')[0:comma_index])
            if os.path.isdir(target_path):
                shutil.rmtree(target_path)
            shutil.copytree(origin_path, target_path)
            shutil.rmtree(target_path + '/.git')

        with open(target_paths.get(target) + 'seguimiento.txt', 'w') as write_file:
            updated_modules.insert(0, '--- Módulos actualizados ---\n\n')
            updated_modules.append(f"\n\nHora actualización: {datetime.datetime.now()}")
            write_file.writelines(updated_modules)

    print("Todo el contenido ha sido movido")
