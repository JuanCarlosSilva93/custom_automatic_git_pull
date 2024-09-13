from updating_modules_package import updating_logic
from files_move_package import automatic_files

if __name__ == "__main__":
    print('Iniciando actualización, por favor espere...')
    updating_logic.updating_modules_from_github()
    print('Actualización terminada\n')
    print('Iniciando movimiento de módulos actualizados, por favor espere...')
    automatic_files.moving_directories_files()
    print('Ejecución terminada')
